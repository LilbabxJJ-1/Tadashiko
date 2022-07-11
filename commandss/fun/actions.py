# <----------------------------------MainImports---------------------------------------->
import discord
from discord.ext import commands
from tokens import mycol, warning
import requests
# <----------------------------------Bot---------------------------------------->


class Actions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dance(self, ctx):
        url = "https://purrbot.site/api/img/sfw/dance/gif/"
        get = requests.get(url)
        send = get.json()
        embed = discord.Embed(title=f"{ctx.author.name} is grooving!",
                              color=0xffb6c1)
        embed.set_image(url=send["link"])
        await ctx.send(embed=embed)