# <----------------------------------MainImports---------------------------------------->
import asyncio
import discord
from discord.ext import commands
from tokens import mycol, warning, perms

# <----------------------------------Bot---------------------------------------->


class Welcome(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["welcome-channel", "wc"])
    async def welcome_channel(self, ctx, channel: discord.TextChannel):
        if ctx.author.guild_permissions.manage_guild:
            if mycol.find_one({"key": f"accepted_{ctx.author.id}"}) is not None:
                if mycol.find_one({'key': f"welcchan_{ctx.guild.id}"}) is not None:
                    q = {"key": f"welcchan_{ctx.guild.id}"}
                    mycol.update_one(q, {"$set": {"data": f"{channel.id}"}})
                    embed = discord.Embed(title="Welcome Channel Updated!",
                                          description=f"You have updated your welcome channel to <#{channel.id}>",
                                          color=0xffb6c1)
                    await ctx.send(embed=embed)
                else:
                    server = {
                        "key": f"welcchan_{ctx.guild.id}",
                        "data": f"{channel.id}"
                    }
                    mycol.insert_one(server)
                    embed = discord.Embed(title="Welcome Channel Updated!",
                                          description=f"You have updated your welcome channel to <#{channel.id}>",
                                          color=0xffb6c1)
                    await ctx.send(embed=embed)
            else:
                await ctx.send(embed=warning)
        else:
            await ctx.send(perms)

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

    @commands.command(aliases=["wel-col", "wcolor", "welcome-color"])
    async def welcome_color(self, ctx, hex: discord.Color):
        if ctx.author.guild_permissions.manage_guild:
            if mycol.find_one({"key": f"accepted_{ctx.author.id}"}) is not None:
                if mycol.find_one({'key': f"welcColor_{ctx.guild.id}"}) is not None:
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
            await ctx.send(perms)
           

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

    @commands.command(aliases=["welcome-footer", "wf"])
    async def welcome_footer(self, ctx):
        def check(msg):
            if msg.author.id == ctx.author.id and msg.channel.id == ctx.channel.id:
                return True

        if ctx.author.guild_permissions.manage_guild:
            if mycol.find_one({"key": f"accepted_{ctx.author.id}"}) is not None:
                if mycol.find_one({'key': f"welcFooter_{ctx.guild.id}"}) is not None:
                    ll = await ctx.send("What do you want your footer to be?")
                    try:
                        footer = await self.bot.wait_for("message", check=check, timeout=300)
                    except asyncio.TimeoutError:
                        await ll.delete()
                        await ctx.send("You took to long to respond!")
                        return
                    message = " "
                    for i in footer.content:
                        if i == "\n":
                            message += f"{i}"
                        elif i == " ":
                            message += " "
                        else:
                            message += f"{i}"
                    q = {"key": f"welcFooter_{ctx.guild.id}"}
                    mycol.update_one(q, {"$set": {"data": f"{message}"}})
                    embed = discord.Embed(title="Successful!",
                                          description="You have successfully set the footer message",
                                          color=0xffb6c1)
                    await ctx.send(embed=embed)

                else:
                    ll = await ctx.send("What do you want your footer to be?")
                    try:
                        footer = await self.bot.wait_for("message", check=check, timeout=300)
                    except asyncio.TimeoutError:
                        await ll.delete()
                        await ctx.send("You took to long to respond!")
                        return
                    message = " "
                    for i in footer.content:
                        if i == "\n":
                            message += f" {i}"
                        elif i == " ":
                            message += " "
                        else:
                            message += f" {i}"
                    server = {
                        "key": f"welcFooter_{ctx.guild.id}",
                        'data': f"{message}"
                    }
                    mycol.insert_one(server)
                    embed = discord.Embed(title="Successful!",
                                          description="You have successfully set the footer message",
                                          color=0xffb6c1)
                    await ctx.send(embed=embed)
            else:
                await ctx.send(embed=warning)
        else:
            await ctx.send(perms)
        # FINISH HERE

    @commands.command(aliases=["tw"])
    async def test_welcome(self, ctx):
        request = mycol.find_one({"key": f"welcColor_{ctx.guild.id}"})
        title = mycol.find_one({"key": f"welcTitle_{ctx.guild.id}"})
        footer = mycol.find_one({"key": f"welcFooter_{ctx.guild.id}"})
        description = "Welcome {user.mention}!"
        color = await commands.ColorConverter().convert(ctx, request["data"])
        if ctx.author.guild_permissions.manage_guild:
            if mycol.find_one({"key": f"accepted_{ctx.author.id}"}) is not None:
                if "{membercount}" in title:
                    title = title.replace("{membercount}", str(ctx.guild.member_count))
                if "{user.mention}" in description:
                    description = description.replace("{user.mention}", self.bot.user.mention)
                embed = discord.Embed(title=title,
                                      description=description,
                                      color=color)
                if footer is not None:
                    embed.set_footer(text=footer["data"])
                await ctx.send(embed=embed)

            else:
                await ctx.send(warning)
        else:
            await ctx.send(perms)
