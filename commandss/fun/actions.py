# <----------------------------------MainImports---------------------------------------->
import discord
from discord.ext import commands
from tokens import mycol, warning, color
import requests
import random
# <----------------------------------Bot---------------------------------------->


class Actions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.respond = ["Hey! Why me??", "Stop that!", "Wait what?", "Stop pinging me please-", "I will fight you >.<", "Stopppppp", "....",
                   "||Stop this madness||",
                   "ughhhhh"]


    @commands.command()
    async def dance(self, ctx):
        if mycol.find_one({"key": f"accepted_{ctx.author.id}"}) is None:
            await ctx.send(warning)
            return
        url = "https://purrbot.site/api/img/sfw/dance/gif/"
        get = requests.get(url)
        send = get.json()
        embed = discord.Embed(title=f"{ctx.author.name} is grooving!",
                              color=color)
        embed.set_image(url=send["link"])
        await ctx.send(embed=embed)

    @commands.command()
    async def bite(self, ctx, user: discord.Member):
        response = random.choice(self.respond)
        if mycol.find_one({"key": f"accepted_{ctx.author.id}"}) is None:
            await ctx.send(warning)
            return
        if user.mention == self.bot.user.mention:
            await ctx.send(response)
            return
        if user.mention == ctx.author.mention:
            await ctx.send("You can't do that!")
        url = "https://purrbot.site/api/img/sfw/bite/gif/"
        get = requests.get(url)
        send = get.json()
        embed = discord.Embed(title=f"{ctx.author.name} bit {user.name}",
                              color=color)
        embed.set_image(url=send["link"])
        await ctx.send(embed=embed)

    @commands.command()
    async def blush(self, ctx):
        if mycol.find_one({"key": f"accepted_{ctx.author.id}"}) is None:
            await ctx.send(warning)
            return
        url = "https://purrbot.site/api/img/sfw/blush/gif/"
        get = requests.get(url)
        send = get.json()
        embed = discord.Embed(title=f"{ctx.author.name} blushed!",
                              color=color)
        embed.set_image(url=send["link"])
        await ctx.send(embed=embed)

    @commands.command()
    async def cry(self, ctx):
        if mycol.find_one({"key": f"accepted_{ctx.author.id}"}) is None:
            await ctx.send(warning)
            return
        url = "https://purrbot.site/api/img/sfw/cry/gif/"
        get = requests.get(url)
        send = get.json()
        embed = discord.Embed(title=f"{ctx.author.name} is crying...",
                              color=color)
        embed.set_image(url=send["link"])
        await ctx.send(embed=embed)

    @commands.command()
    async def cuddle(self, ctx, user: discord.Member):
        response = random.choice(self.respond)
        if mycol.find_one({"key": f"accepted_{ctx.author.id}"}) is None:
            await ctx.send(warning)
            return
        if user.mention == self.bot.user.mention:
            await ctx.send(response)
            return
        if user.mention == ctx.author.mention:
            await ctx.send("You can't do that!")
        url = "https://purrbot.site/api/img/sfw/cuddle/gif/"
        get = requests.get(url)
        send = get.json()
        embed = discord.Embed(title=f"{ctx.author.name} cuddled {user.name}",
                              color=color)
        embed.set_image(url=send["link"])
        await ctx.send(embed=embed)

    @commands.command()
    async def hug(self, ctx, user: discord.Member):
        response = random.choice(self.respond)
        if mycol.find_one({"key": f"accepted_{ctx.author.id}"}) is None:
            await ctx.send(warning)
            return
        if user.mention == self.bot.user.mention:
            await ctx.send(response)
            return
        if user.mention == ctx.author.mention:
            await ctx.send("You can't do that!")
        url = "https://purrbot.site/api/img/sfw/hug/gif/"
        get = requests.get(url)
        send = get.json()
        embed = discord.Embed(title=f"{ctx.author.name} hugged {user.name}",
                              color=color)
        embed.set_image(url=send["link"])
        await ctx.send(embed=embed)

    @commands.command()
    async def kiss(self, ctx, user: discord.Member):
        response = random.choice(self.respond)
        if mycol.find_one({"key": f"accepted_{ctx.author.id}"}) is None:
            await ctx.send(warning)
            return
        if user.mention == self.bot.user.mention:
            await ctx.send(response)
            return
        if user.mention == ctx.author.mention:
            await ctx.send("You can't do that!")
        url = "https://purrbot.site/api/img/sfw/kiss/gif/"
        get = requests.get(url)
        send = get.json()
        embed = discord.Embed(title=f"{ctx.author.name} kissed {user.name}",
                              color=color)
        embed.set_image(url=send["link"])
        await ctx.send(embed=embed)

    @commands.command()
    async def lick(self, ctx, user: discord.Member):
        response = random.choice(self.respond)
        if mycol.find_one({"key": f"accepted_{ctx.author.id}"}) is None:
            await ctx.send(warning)
            return
        if user.mention == self.bot.user.mention:
            await ctx.send(response)
            return
        if user.mention == ctx.author.mention:
            await ctx.send("You can't do that!")
        url = "https://purrbot.site/api/img/sfw/lick/gif/"
        get = requests.get(url)
        send = get.json()
        embed = discord.Embed(title=f"{ctx.author.name} licked {user.name}",
                              color=color)
        embed.set_image(url=send["link"])
        await ctx.send(embed=embed)

    @commands.command()
    async def pat(self, ctx, user: discord.Member):
        response = random.choice(self.respond)
        if mycol.find_one({"key": f"accepted_{ctx.author.id}"}) is None:
            await ctx.send(warning)
            return
        if user.mention == self.bot.user.mention:
            await ctx.send(response)
            return
        if user.mention == ctx.author.mention:
            await ctx.send("You can't do that!")
        url = "https://purrbot.site/api/img/sfw/pat/gif/"
        get = requests.get(url)
        send = get.json()
        embed = discord.Embed(title=f"{ctx.author.name} patted {user.name}",
                              color=color)
        embed.set_image(url=send["link"])
        await ctx.send(embed=embed)

    @commands.command()
    async def poke(self, ctx, user: discord.Member):
        response = random.choice(self.respond)
        if mycol.find_one({"key": f"accepted_{ctx.author.id}"}) is None:
            await ctx.send(warning)
            return
        if user.mention == self.bot.user.mention:
            await ctx.send(response)
            return
        if user.mention == ctx.author.mention:
            await ctx.send("You can't do that!")
        url = "https://purrbot.site/api/img/sfw/poke/gif/"
        get = requests.get(url)
        send = get.json()
        embed = discord.Embed(title=f"{ctx.author.name} poked {user.name}",
                              color=color)
        embed.set_image(url=send["link"])
        await ctx.send(embed=embed)

    @commands.command()
    async def slap(self, ctx, user: discord.Member):
        response = random.choice(self.respond)
        if mycol.find_one({"key": f"accepted_{ctx.author.id}"}) is None:
            await ctx.send(warning)
            return
        if user.mention == self.bot.user.mention:
            await ctx.send(response)
            return
        if user.mention == ctx.author.mention:
            await ctx.send("You can't do that!")
        url = "https://purrbot.site/api/img/sfw/slap/gif/"
        get = requests.get(url)
        send = get.json()
        embed = discord.Embed(title=f"{ctx.author.name} slapped {user.name}",
                              color=color)
        embed.set_image(url=send["link"])
        await ctx.send(embed=embed)

    commands.command()
    async def tickle(self, ctx, user: discord.Member):
        response = random.choice(self.respond)
        if mycol.find_one({"key": f"accepted_{ctx.author.id}"}) is None:
            await ctx.send(warning)
            return
        if user.mention == self.bot.user.mention:
            await ctx.send(response)
            return
        if user.mention == ctx.author.mention:
            await ctx.send("You can't do that!")
        url = "https://purrbot.site/api/img/sfw/tickle/gif/"
        get = requests.get(url)
        send = get.json()
        embed = discord.Embed(title=f"{ctx.author.name} tickled {user.name}",
                              color=color)
        embed.set_image(url=send["link"])
        await ctx.send(embed=embed)