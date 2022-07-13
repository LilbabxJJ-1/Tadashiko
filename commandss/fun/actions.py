# <----------------------------------MainImports---------------------------------------->
import discord
from discord.ext import commands
from tokens import mycol, warning, color
import requests
# <----------------------------------Bot---------------------------------------->


class Actions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dance(self, ctx):
        if mycol.find_one({"key": f"accepted_{ctx.author.id}"}) is None:
            await ctx.send(warning)
        url = "https://purrbot.site/api/img/sfw/dance/gif/"
        get = requests.get(url)
        send = get.json()
        embed = discord.Embed(title=f"{ctx.author.name} is grooving!",
                              color=color)
        embed.set_image(url=send["link"])
        embed.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{ctx.id}/{ctx.avatar}.png")
        await ctx.send(embed=embed)

    @commands.command()
    async def bite(self, ctx, user: discord.Member):
        if mycol.find_one({"key": f"accepted_{ctx.author.id}"}) is None:
            await ctx.send(warning)
            return
        url = "https://purrbot.site/api/img/sfw/bite/gif/"
        get = requests.get(url)
        send = get.json()
        embed = discord.Embed(title=f"{ctx.author.name} bit {user.name}",
                              color=color)
        embed.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{ctx.id}/{ctx.avatar}.png")
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
        embed.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{ctx.id}/{ctx.avatar}.png")
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
        embed.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{ctx.id}/{ctx.avatar}.png")
        embed.set_image(url=send["link"])
        await ctx.send(embed=embed)
