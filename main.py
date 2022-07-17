# <----------------------------------MainImports---------------------------------------->
import discord
from discord.ext import commands
# <----------------------------------FileImports---------------------------------------->
from tokens import token, mycol
from commandss.mod import welcome as w
from commandss.mod import mods as m
from commandss import events as e
from commandss.fun import actions as a
from commandss import general as g
from commandss import utilities as u
from commandss.fun import afk as af
from commandss.fun import music as ms
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


activity = discord.Activity(type=discord.ActivityType.watching, name='Myself be rebuilt 💮')
bot = commands.Bot(command_prefix=prefix, case_insensitive=True, intents=intents, help_command=None, activity=activity, chunk_guilds_at_startup=False)


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


async def run():
    await bot.wait_until_ready()
    bot.add_cog(w.Welcome(bot))
    bot.add_cog(a.Actions(bot))
    bot.add_cog(g.Gen(bot))
    bot.add_cog(m.Mods(bot))
    bot.add_cog(e.Events(bot))
    bot.add_cog(u.Utils(bot))
    bot.add_cog(af.Fun(bot))
    bot.add_cog(ms.Music(bot))

bot.loop.create_task(run())
bot.run(token)