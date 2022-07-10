# <----------------------------------MainImports---------------------------------------->
import discord
from discord.ext import commands
from tokens import mycol, warning
# <----------------------------------Bot---------------------------------------->


class Mods(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def prefix(self, ctx, prefix):
        if ctx.author.guild_permissions.manage_guild:
            if mycol.find_one({"key": f"accepted_{ctx.author.id}"}) is not None:
                if mycol.find_one({'key': f"prefix_{ctx.guild.id}"}) is not None:
                    if prefix == "@everyone" or prefix == "@here":
                        await ctx.send("You cannot set the prefix to a ping!")
                        return
                    q = {"key": f"prefix_{ctx.guild.id}"}
                    mycol.update_one(q, {"$set": {"data": f"{prefix}"}})
                    embed = discord.Embed(title="Successful!",
                                          description=f"The prefix for {ctx.guild.name} is now {prefix}!",
                                          color=0xffb6c1)
                    await ctx.send(embed=embed)
                else:
                    if prefix == "@everyone" or prefix == "@here":
                        await ctx.send("You cannot set the prefix to a ping!")
                        return
                    prefixes = {
                        "key": f"prefix_{ctx.guild.id}",
                        "data": f"{prefix}"
                    }
                    mycol.insert_one(prefixes)
                    embed = discord.Embed(title="Successful!",
                                          description=f"The prefix for {ctx.guild.name} is now {prefix}!",
                                          color=0xffb6c1)
                    await ctx.send(embed=embed)
            else:
                await ctx.send(embed=warning)
        else:
            await ctx.send("You don't have permissions to do that!")
