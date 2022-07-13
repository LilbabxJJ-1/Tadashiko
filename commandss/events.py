# <----------------------------------MainImports---------------------------------------->
import discord
from discord.ext import commands
from tokens import token, mycol
# <----------------------------------Bot---------------------------------------->

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        pass # For now

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content == self.bot.user.mention:
            find = mycol.find_one({"key":f"prefix_{message.guild.id}"})
            if find is not None:
                prefix = find["data"]
            else:
                prefix = "t!"
            await message.channel.send(f"The prefix for this server is **{prefix}**")