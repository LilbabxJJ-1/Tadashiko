# <----------------------------------MainImports---------------------------------------->
import discord
from discord.ext import commands
from tokens import mycol, warning


# <----------------------------------Bot---------------------------------------->

class Welcome(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["welcome-channel", "wc"])
    async def welcome_channel(self, ctx, chn: discord.TextChannel):
        if ctx.author.guild_permissions.manage_guild:
            if mycol.find_one({"key": f"accepted_{ctx.author.id}"}) is not None:
                if mycol.find_one({'key': f"welcchan_{ctx.guild.id}"}) is not None:
                    q = {"key": f"welcchan_{ctx.guild.id}"}
                    mycol.update_one(q, {"$set": {"data": f"{chn.id}"}})
                    embed = discord.Embed(title="Welcome Channel Updated!",
                                          description=f"You have updated your welcome channel to <#{chn.id}>",
                                          color=0xffb6c1)
                    await ctx.send(embed=embed)
                else:
                    server = {
                        "key": f"welcchan_{ctx.guild.id}",
                        "data": f"{chn.id}"
                    }
                    mycol.insert_one(server)
                    embed = discord.Embed(title="Welcome Channel Updated!",
                                          description=f"You have updated your welcome channel to <#{chn.id}>",
                                          color=0xffb6c1)
                    await ctx.send(embed=embed)
            else:
                await ctx.send(embed=warning)
        else:
            await ctx.send("You don't have the permissions to do this!")

    @welcome_channel.error
    async def welcome_channel_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            find = mycol.find_one({"key": f"prefix_{ctx.guild.id}"})
            if find is not None:
                prefix = find["data"]
            else:
                prefix = "t!"
            embed = discord.Embed(title="Error!",
                                  description=f"You forgot an argument! Use like: {prefix}wc #channel",
                                  color=0xffb6c1)
            await ctx.send(embed=embed)

    @commands.command(aliases=["wel-col", "wcolor", "welcome-channel"])
    async def welcome_color(self, ctx, hex: discord.Color):
        if ctx.author.guild_permissions.manage_guild:
            if mycol.find_one({"key": f"accepted_{ctx.author.id}"}) is not None:
                if mycol.find_one({'key': f"welc_color{ctx.guild.id}"}) is not None:
                    embed = discord.Embed(title="Successful!",
                                          description=f"Welcome color is now `{hex}`",
                                          color=hex)
                    q = {"key": f"welcColor_{ctx.guild.id}"}
                    mycol.update_one(q, {"$set": {"data": f"{hex}"}})
                    await ctx.send(embed=embed)
                else:
                    server = {
                        "key": f"welcColor_{ctx.guild.id}",
                        "data": f"{hex}"
                    }
                    mycol.insert_one(server)
                    embed = discord.Embed(title="Successful!",
                                          description=f"Welcome color is now `{hex}`",
                                          color=hex)
                    await ctx.send(embed=embed)
            else:
                await ctx.send(embed=warning)
        else:
            await ctx.send("You do not have permissions to do this!")
            # FINISH HERE DUMMY

    @welcome_color.error
    async def wc_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            find = mycol.find_one({"key": f"prefix_{ctx.guild.id}"})
            if find is not None:
                prefix = find["data"]
            else:
                prefix = "t!"
            embed = discord.Embed(title="Error!",
                                  description=f"You forgot an argument! Use like: {prefix}wc #ffb6c1",
                                  color=0xffb6c1)
            await ctx.send(embed=embed)
        elif isinstance(error, commands.BadColourArgument):
            await ctx.send("Make sure to either use `#` **or** `0x` in front of the hex code!")
