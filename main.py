# <----------------------------------MainImports---------------------------------------->
import discord
from discord.ext import commands
# <----------------------------------FileImports---------------------------------------->
from tokens import token, mycol
from commandss.mod import welcome as w
from commandss.mod import mods as m
from commandss import events as e
# <----------------------------------Bot---------------------------------------->
intents = discord.Intents.default()
intents.message_content = True
intents.members = True


def prefix(bot, message):
    result = mycol.find_one({"key": f"prefix_{message.guild.id}"})
    if result is not None:
                ll = result["data"]
                return ll
    else:
            ll = "t!"
            return ll


bot = commands.Bot(command_prefix=(prefix), case_insensitive=True, intents=intents, help_command=None)


@bot.event
async def on_ready():
    print(f"Ready on {bot.user}")


@bot.command()
async def test(ctx):
    find = mycol.find_one({"key": f"accepted_{ctx.author.id}"})
    if find is None:
        await ctx.send("This person hasn't accepted")
    else:
        await ctx.send('This person has accepted')
        await ctx.send(find)


def run():
    bot.add_cog(w.Welcome(bot))
    bot.add_cog(m.Mods(bot))
    bot.add_cog(e.Events(bot))
    bot.run(token)


run()
