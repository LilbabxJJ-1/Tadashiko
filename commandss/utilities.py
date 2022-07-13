# <----------------------------------MainImports---------------------------------------->
import discord
from discord.ext import commands
from tokens import mycol, warning
# <----------------------------------Bot---------------------------------------->


class Utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["nick"])
    async def nickname(self, ctx, nick):
        l = ["<", "@", "#", ">"]
        if PermissionError:
            await ctx.send("Cannot change Owners nickname")
        for i in l:
            if i in nick:
                await ctx.send("Nickname cannot contain these symbols: **<, @, #, >**")
                return
        if nick == "":
            await ctx.send("Nickname is empty")
        elif len(nick) > 32:
            await ctx.send("Nickname is too long")
        elif len(nick) < 2:
            await ctx.send("Nickname is too short")
        else:
            await ctx.message.author.edit(nick=nick)
            await ctx.send(f"{ctx.message.author.name}'s nickname has been changed to {nick}")

    @nickname.error
    async def nickname_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please Provide a nickname")
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send("I don't have the perms to do this")
        else:
            print(error)