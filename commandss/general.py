# <----------------------------------MainImports---------------------------------------->
import discord
from discord.ext import commands
from tokens import mycol, warning
# <----------------------------------Bot---------------------------------------->

class Mods(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        if mycol.find_one({"key": f"accepted_{ctx.author.id}"}) is not None:
            embed = discord.Embed(title="Success",
                                  description="Pong! 🏓\nThe bot is online and running!",
                                  color=0xffb6c1)
            await ctx.send(embed=embed)
            print("Ping command was used!")
        else:
            await ctx.send(embed=warning)
