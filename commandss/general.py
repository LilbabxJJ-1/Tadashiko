# <----------------------------------MainImports---------------------------------------->
import discord
from discord.ext import commands
from tokens import mycol, warning
from commandss.helps import mainhelp
# <----------------------------------Bot---------------------------------------->

class DropDown(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Actions 👋"),
            discord.SelectOption(label="Fun🎉"),
            discord.SelectOption(label="Utility⚙"),
            discord.SelectOption(label="Config⚒")
        ]
        super().__init__(placeholder="Select", max_values=1, min_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "Config⚒":
            await interaction.response.send_message(embed=mainhelp, ephemeral=True)
        else:
            await interaction.response.send_message("Success")

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
        view = DropDownView()
        await ctx.send("Choose a help menu!", view=view)




