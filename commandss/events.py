# <----------------------------------MainImports---------------------------------------->
import discord
from discord.ext import commands
from tokens import token, mycol, warning, perms, color
# <----------------------------------Bot---------------------------------------->

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, ctx):
        request = mycol.find_one({"key": f"welcColor_{ctx.guild.id}"})
        title = mycol.find_one({"key": f"welcTitle_{ctx.guild.id}"})
        footer = mycol.find_one({"key": f"welcFooter_{ctx.guild.id}"})
        image = mycol.find_one({"key": f"welcImage_{ctx.guild.id}"})
        description = mycol.find_one({"key": f"welcMessage_{ctx.guild.id}"})
        if request is not None:
            color = await commands.ColorConverter().convert(ctx, request["data"])
        else:
            color = await commands.ColorConverter().convert(ctx, color)
        channel = mycol.find_one({"key": f'welcchan_{ctx.guild.id}'})
        channel = int(channel["data"])
        channel = self.bot.get_channel(channel)
        enabled = mycol.find_one({"key": f"welcEnabled_{ctx.guild.id}"})
        if enabled is None:
            return
        elif enabled["data"] == "false":
            return
        else:
            if title is None:
                await ctx.send("You need to set a title")
                return
            if description is None:
                await ctx.send("You need to set a description")
                return
            if "{membercount}" in title["data"] or "{username}" in title["data"] or "{user.mention}" in title["data"] or "{servername}" in title[
                "data"]:
                title = title["data"].replace("{membercount}", str(ctx.guild.member_count)).replace("{username}", str(ctx.name)).replace(
                    "{user.mention}", str(ctx.mention)).replace("{servername}", str(ctx.guild.name))
            else:
                title = title["data"]
            if "{membercount}" in description["data"] or "{username}" in description["data"] or "{user.mention}" in description[
                "data"] or "{servername}" in description["data"]:
                description = description["data"].replace("{membercount}", str(ctx.guild.member_count)).replace("{username}",
                                                                                                                str(ctx.name)).replace(
                    "{user.mention}", str(ctx.mention)).replace("{servername}", str(ctx.guild.name))
            else:
                description = description["data"]
            embed = discord.Embed(title=title,
                                  description=description,
                                  color=color)
            if footer is not None:
                footer = footer["data"].replace("{membercount}", str(ctx.guild.member_count)).replace("{username}", str(ctx.name)).replace(
                    "{user.mention}", str(ctx.mention)).replace("{servername}", str(ctx.guild.name))
                embed.set_footer(text=footer)
            if image is not None:
                embed.set_image(url=image["data"])
            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content == self.bot.user.mention:
            find = mycol.find_one({"key": f"prefix_{message.guild.id}"})
            if find is not None:
                prefix = find["data"]
            else:
                prefix = "t!"
            await message.channel.send(f"The prefix for this server is **{prefix}**")
