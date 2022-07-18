# <----------------------------------MainImports---------------------------------------->
import asyncio
import discord
from discord.ext import commands
from tokens import mycol, warning, color
import requests
import youtube_dl
import pafy
import bs4 as b
from async_timeout import timeout


# <----------------------------------Bot---------------------------------------->
class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.song_queue = {}
        for guild in self.bot.guilds:
            self.song_queue[f"{guild.id}"] = []
        self.FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        self.vc = None

    async def search_song(self, amount, song, get_url=False):
        info = await self.bot.loop.run_in_executor(None, lambda: youtube_dl.YoutubeDL(
            {"format": "bestaudio", "quiet": True, "noplaylist": True}).extract_info(f"ytsearch{amount}:{song}", download=False,
                                                                                       ie_key="YoutubeSearch"))
        if info["entries"] is None: return None

        return [entry["webpage_url"] for entry in info["entries"]] if get_url else info

    @commands.command()
    async def lyrics(self, ctx, *song):
        songs = ''
        for i in song:
            songs += f" {i}"
        url = f"https://hunterapi.sytes.net/lyrics?song={songs}"
        get = requests.get(url)
        send = get.json()
        embed = discord.Embed(title=f"Lyrics for{songs.title()}",
                              description=send["lyrics"],
                              color=color)
        await ctx.send(embed=embed)

    @commands.command()
    async def join(self, ctx):
        guild = self.bot.get_guild(ctx.guild.id) or await self.bot.fetch_guild(ctx.guild.id)
        self.vc = guild
        if ctx.author.voice is None:
            return await ctx.send("You are not in a vc channel, please join one")

        if ctx.voice_client is not None:
            await ctx.voice_client.disconnect()
        await ctx.author.voice.channel.connect()

    @commands.command()
    async def leave(self, ctx):
        if ctx.voice_client is not None:
            await self.vc.voice_client.disconnect()
            return await ctx.send("Left the voice channel")

        await ctx.send("I'm not connected to a voice channel")

    async def play_song(self, ctx, song):
        guild = self.bot.get_guild(ctx.guild.id) or await self.bot.fetch_guild(ctx.guild.id)
        url = pafy.new(song).getbestaudio().url
        self.vc.voice_client.play(discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(url, **self.FFMPEG_OPTIONS)),
                              after=lambda error: self.bot.loop.create_task(self.check_queue(ctx)))
        self.vc.voice_client.source.volume = 0.5

    @commands.command()
    async def play(self, ctx, *, song=None):
        guild = self.bot.get_guild(ctx.guild.id) or await self.bot.fetch_guild(ctx.guild.id)
        self.vc = guild
        if song is None:
            return await ctx.send("Must say what song")

        if ctx.voice_client is None:
            try:
                await ctx.author.voice.channel.connect()
            except Exception as e:
                print(e)
                return await ctx.send("Please join a voice channel first")
        if not ("youtube.come/watch?" in song or "https:youtu.be/" in song):
            await ctx.send("Searching for song.. please wait a moment")
            result = await self.search_song(1, song, get_url=True)

            if result is None:
                return await ctx.send("Sorry couldn't find it!")
            song = result[0]
        if ctx.voice_client.source is not None:
            queue_len = len(self.song_queue[str(ctx.guild.id)])

            if queue_len < 15:
                self.song_queue[str(ctx.guild.id)].append(song)
                return await ctx.send(f"Added to the queue | Position {queue_len + 1}")

            else:
                return await ctx.send("I can only hold up to 15 songs")

        await self.play_song(ctx, song)
        r = requests.get(song)
        s = b.BeautifulSoup(r.text, "html.parser")
        title = s.find("title").text.replace("\n", "").replace("- YouTube", "")
        embed = discord.Embed(title="New Song", description=f"Now playing: {title}", color=color)
        await ctx.send(embed=embed)
        timeout(6)

    async def check_queue(self, ctx):
        if len(self.song_queue[str(ctx.guild.id)]) > 0:
            if self.vc.voice_client.is_playing():
                pass
            r = requests.get(self.song_queue[str(ctx.guild.id)][0])
            s = b.BeautifulSoup(r.text, "html.parser")
            title = s.find("title").text.replace("\n", "").replace("- YouTube", "")
            await self.play_song(ctx, self.song_queue[str(ctx.guild.id)][0])
            embed = discord.Embed(title="New Song", description=f"Now playing: {title}", color=color)
            await ctx.send(embed=embed)
            self.song_queue[str(ctx.guild.id)].pop(0)
        else:
            await self.vc.voice_client.disconnect()
            await ctx.send("No more songs to play!")

    @commands.command()
    async def queue(self, ctx):
        if len(self.song_queue[str(ctx.guild.id)]) == 0:
            return await ctx.send("There are no songs in the queue")

        hold = await ctx.send("Just a second..")
        embed = discord.Embed(title="Music Queue", description="", color=color)
        i = 1
        for url in self.song_queue[str(ctx.guild.id)]:
            r = requests.get(url)
            s = b.BeautifulSoup(r.text, "html.parser")
            title = s.find("title").text.replace("\n", "").replace("- YouTube", "")
            embed.description += f"{i}) {title}\n"
            i += 1

        embed.set_footer(text="Groovin with Tadashiko")
        await hold.delete()
        await ctx.send(embed=embed)

    @commands.command()
    async def pause(self, ctx):
        guild = self.bot.get_guild(ctx.guild.id) or await self.bot.fetch_guild(ctx.guild.id)
        if guild.voice_client.is_paused():
            return await ctx.send("Music is already paused!")
        guild.voice_client.pause()
        await ctx.send("Music has been paused")

    @commands.command()
    async def resume(self, ctx):
        guild = self.bot.get_guild(ctx.guild.id) or await self.bot.fetch_guild(ctx.guild.id)
        if guild.voice_client.is_playing():
            return await ctx.send("Music is already playing!")
        guild.voice_client.resume()
        await ctx.send("Music has been paused")

    @commands.command()
    async def skip(self, ctx):
        guild = self.bot.get_guild(ctx.guild.id) or await self.bot.fetch_guild(ctx.guild.id)
        self.vc.voice_client.stop()
        await ctx.send("Skipping...")


