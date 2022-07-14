# <----------------------------------MainImports---------------------------------------->
import asyncio
import discord
from discord.ext import commands
from tokens import mycol, warning, perms, color


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
                            message += f" {i}"
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
                            message += f"{i}"
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

    @commands.command(aliases=["wt", "welcome-title"])
    async def welcome_title(self, ctx):
        def check(msg):
            if msg.author.id == ctx.author.id and msg.channel.id == ctx.channel.id:
                return True

        if ctx.author.guild_permissions.manage_guild:
            if mycol.find_one({"key": f"accepted_{ctx.author.id}"}) is not None:
                if mycol.find_one({'key': f"welcTitle_{ctx.guild.id}"}) is not None:
                    ll = await ctx.send("What do you want your title to be?")
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
                            message += f"{i}"
                    q = {"key": f"welcTitle_{ctx.guild.id}"}
                    mycol.update_one(q, {"$set": {"data": f"{message}"}})
                    embed = discord.Embed(title="Successful!",
                                          description="You have successfully set the welcome title",
                                          color=0xffb6c1)
                    await ctx.send(embed=embed)

                else:
                    ll = await ctx.send("What do you want your title to be?")
                    try:
                        footer = await self.bot.wait_for("message", check=check, timeout=300)
                    except asyncio.TimeoutError:
                        await ll.delete()
                        await ctx.send("You took to long to respond!")
                        return
                    message = ""
                    for i in footer.content:
                        if i == "\n":
                            message += f" {i}"
                        elif i == " ":
                            message += " "
                        else:
                            message += f"{i}"
                    server = {
                        "key": f"welcTitle_{ctx.guild.id}",
                        'data': f"{message}"
                    }
                    mycol.insert_one(server)
                    embed = discord.Embed(title="Successful!",
                                          description="You have successfully set the welcome title",
                                          color=0xffb6c1)
                    await ctx.send(embed=embed)
            else:
                await ctx.send(embed=warning)
        else:
            await ctx.send(perms)

    @commands.command(aliases=["wm", "welcome-message"])
    async def welcome_message(self, ctx):
        def check(msg):
            if msg.author.id == ctx.author.id and msg.channel.id == ctx.channel.id:
                return True

        if ctx.author.guild_permissions.manage_guild:
            if mycol.find_one({"key": f"accepted_{ctx.author.id}"}) is not None:
                if mycol.find_one({'key': f"welcMessage_{ctx.guild.id}"}) is not None:
                    ll = await ctx.send("What do you want your welcome message to be?")
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
                            message += f"{i}"
                    q = {"key": f"welcMessage_{ctx.guild.id}"}
                    mycol.update_one(q, {"$set": {"data": f"{message}"}})
                    embed = discord.Embed(title="Successful!",
                                          description="You have successfully set the welcome message",
                                          color=0xffb6c1)
                    await ctx.send(embed=embed)

                else:
                    ll = await ctx.send("What do you want your welcome message to be?")
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
                            message += f"{i}"
                    server = {
                        "key": f"welcMessage_{ctx.guild.id}",
                        'data': f"{message}"
                    }
                    mycol.insert_one(server)
                    embed = discord.Embed(title="Successful!",
                                          description="You have successfully set the welcome message",
                                          color=0xffb6c1)
                    await ctx.send(embed=embed)
            else:
                await ctx.send(embed=warning)
        else:
            await ctx.send(perms)

    @commands.command(aliases=["wi", "welcome-image"])
    async def welcome_image(self, ctx, image_link):
        if ctx.author.guild_permissions.manage_guild:
            if mycol.find_one({"key": f"accepted_{ctx.author.id}"}) is not None:
                if mycol.find_one({'key': f"welcImage_{ctx.guild.id}"}) is not None:
                    embed = discord.Embed(title="Successful!",
                                          description=f"Successfully changed welcome image!",
                                          color=color)
                    q = {"key": f"welcImage_{ctx.guild.id}"}
                    mycol.update_one(q, {"$set": {"data": f"{image_link}"}})
                    await ctx.send(embed=embed)
                else:
                    server = {
                        "key": f"welcImage_{ctx.guild.id}",
                        "data": f"{image_link}"
                    }
                    mycol.insert_one(server)
                    embed = discord.Embed(title="Successful!",
                                          description=f"Successfully changed welcome image!",
                                          color=color)
                    await ctx.send(embed=embed)
            else:
                await ctx.send(embed=warning)
        else:
            await ctx.send(perms)

    @commands.command(aliases=["tw"])
    async def test_welcome(self, ctx):
        request = mycol.find_one({"key": f"welcColor_{ctx.guild.id}"})
        title = mycol.find_one({"key": f"welcTitle_{ctx.guild.id}"})
        footer = mycol.find_one({"key": f"welcFooter_{ctx.guild.id}"})
        image = mycol.find_one({"key": f"welcImage_{ctx.guild.id}"})
        description = mycol.find_one({"key": f"welcMessage_{ctx.guild.id}"})
        color = await commands.ColorConverter().convert(ctx, request["data"])
        channel = mycol.find_one({"key": f'welcchan_{ctx.guild.id}'})
        channel = int(channel["data"])
        channel = self.bot.get_channel(channel)
        if ctx.author.guild_permissions.manage_guild:
            if mycol.find_one({"key": f"accepted_{ctx.author.id}"}) is not None:
                if title is None:
                    await ctx.send("You need to set a title")
                    return
                if description is None:
                    await ctx.send("You need to set a description")
                    return
                if "{membercount}" in title["data"] or "{username}" in title["data"] or "{user.mention}" in title["data"] or "{servername}" in title["data"]:
                    title = title["data"].replace("{membercount}", str(ctx.guild.member_count)).replace("{username}", str(ctx.author.name)).replace(
                        "{user.mention}", str(ctx.author.mention)).replace("{servername}", str(ctx.guild.name))
                else:
                    title = title["data"]
                if "{membercount}" in description["data"] or "{username}" in description["data"] or "{user.mention}" in description["data"] or "{servername}" in description["data"]:
                    description = description["data"].replace("{membercount}", str(ctx.guild.member_count)).replace("{username}",
                                                                                                                    str(ctx.author.name)).replace(
                        "{user.mention}", str(ctx.author.mention)).replace("{servername}", str(ctx.guild.name))
                else:
                    description = description["data"]
                embed = discord.Embed(title=title,
                                      description=description,
                                      color=color)
                if footer is not None:
                    footer = footer["data"].replace("{membercount}", str(ctx.guild.member_count)).replace("{username}", str(ctx.author.name)).replace(
                        "{user.mention}", str(ctx.author.mention)).replace("{servername}", str(ctx.guild.name))
                    embed.set_footer(text=footer)
                if image is not None:
                    embed.set_image(url=image["data"])
                await channel.send(embed=embed)
                await ctx.send("Test Welcome has been sent")

            else:
                await ctx.send(warning)
        else:
            await ctx.send(perms)

    @commands.command(aliases=["we", "welcome-enable"])
    async def enable(self, ctx):
        if mycol.find_one({"key": f"accepted_{ctx.author.id}"}) is None:
            await ctx.send(warning)
            return
        enabled = mycol.find_one({"key": f"welcEnabled_{ctx.guild.id}"})
        if ctx.author.guild_permissions.manage_guild:
            if enabled is not None:
                if enabled["data"] == "true":
                    await ctx.send("Welcome messages are already enabled!")
                q = {"key": f"welcEnabled_{ctx.guild.id}"}
                mycol.update_one(q, {"$search": {"data": "true"}})
                await ctx.send("Enabled the welcome message!")
            else:
                server = {
                    "key": f"welcEnabled_{ctx.guild.id}",
                    "data": "true"
                }
                mycol.insert_one(server)
                await ctx.send("Enabled the welcome message!")
        else:
            await ctx.send(perms)

    @commands.command(aliases=['wd', "welcome-disable"])
    async def disable(self, ctx):
        if mycol.find_one({"key": f"accepted_{ctx.author.id}"}) is None:
            await ctx.send(warning)
            return
        enabled = mycol.find_one({"key": f"welcEnabled_{ctx.guild.id}"})
        if ctx.author.guild_permissions.manage_guild:
            if enabled is not None:
                if enabled["data"] == "false":
                    await ctx.send("Welcome messages are already disabled!")
                q = {"key": f"welcEnabled_{ctx.guild.id}"}
                mycol.update_one(q, {"$search": {"data": "false"}})
                await ctx.send("Disabled the welcome message!")
            else:
                server = {
                    "key": f"welcEnabled_{ctx.guild.id}",
                    "data": "false"
                }
                mycol.insert_one(server)
                await ctx.send("Disabled the welcome message!")
        else:
            await ctx.send(perms)
