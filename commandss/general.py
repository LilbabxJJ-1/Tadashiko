# <----------------------------------MainImports---------------------------------------->
import asyncio
import discord
from discord.ext import commands
import discord.ui
from tokens import mycol, warning
from commandss.helps import Actionhelp, Funhelp, Confighelp, Utilhelp, unverified, MusicHelp


# <----------------------------------Bot---------------------------------------->


class DropDown(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Actions👋"),
            discord.SelectOption(label="Fun🎉"),
            discord.SelectOption(label="Utility⚙"),
            discord.SelectOption(label="Config⚒"),
            discord.SelectOption(label="Music🎶")
        ]
        super().__init__(placeholder="Select..", max_values=1, min_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "Actions👋":
            ll = mycol.find_one({"key": f"prefix_{interaction.guild.id}"})
            if ll is not None:
                prefix = ll["data"]
            else:
                prefix = "t!"
            Actionhelp.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/991779249004482600/8aab812fb41ade4e6c05686543a982c5.png")
            await interaction.response.send_message(f"Server Prefix: {prefix}", embed=Actionhelp, ephemeral=True)

        elif self.values[0] == "Fun🎉":
            ll = mycol.find_one({"key": f"prefix_{interaction.guild.id}"})
            if ll is not None:
                prefix = ll["data"]
            else:
                prefix = "t!"
            Funhelp.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/991779249004482600/8aab812fb41ade4e6c05686543a982c5.png")
            await interaction.response.send_message(f"Server Prefix: {prefix}", embed=Funhelp, ephemeral=True)

        elif self.values[0] == "Utility⚙":
            ll = mycol.find_one({"key": f"prefix_{interaction.guild.id}"})
            if ll is not None:
                prefix = ll["data"]
            else:
                prefix = "t!"
            Utilhelp.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/991779249004482600/8aab812fb41ade4e6c05686543a982c5.png")
            await interaction.response.send_message(f"Server Prefix: {prefix}", embed=Utilhelp, ephemeral=True)

        elif self.values[0] == "Config⚒":
            ll = mycol.find_one({"key": f"prefix_{interaction.guild.id}"})
            if ll is not None:
                prefix = ll["data"]
            else:
                prefix = "t!"
            Confighelp.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/991779249004482600/8aab812fb41ade4e6c05686543a982c5.png")
            await interaction.response.send_message(f"Server Prefix: {prefix}", embed=Confighelp, ephemeral=True)

        elif self.values[0] == "Music🎶":
            ll = mycol.find_one({"key": f"prefix_{interaction.guild.id}"})
            if ll is not None:
                prefix = ll["data"]
            else:
                prefix = "t!"
            MusicHelp.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/991779249004482600/8aab812fb41ade4e6c05686543a982c5.png")
            await interaction.response.send_message(f"Server Prefix: {prefix}", embed=MusicHelp, ephemeral=True)


class DropDownView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(DropDown())


class Gen(commands.Cog):
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

    @commands.Command
    async def help(self, ctx: discord.Interaction):
        def check(msg):
            if msg.author.id == ctx.author.id and ctx.channel.id == msg.channel.id:
                return True

        if mycol.find_one({"key": f"accepted_{ctx.author.id}"}) is None:
            await ctx.send(embed=unverified)
            try:
                accept = await self.bot.wait_for("message", timeout=180, check=check)
            except asyncio.TimeoutError:
                await ctx.send(f"{ctx.author.mention} you ran out of time to accept the rules")
                return
            if accept.content.lower() == f"accept":
                rules = {
                    "key": f"accepted_{ctx.author.id}",
                    "data": "true"
                }
                mycol.insert_one(rules)
                await ctx.send("Successfully accepted")
            else:
                await ctx.send(f"Please try again and send `accept`")
        else:
            view = DropDownView()
            await ctx.send("Choose a help menu!", view=view)
