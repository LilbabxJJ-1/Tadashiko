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


bot = commands.Bot(command_prefix=prefix, case_insensitive=True, intents=intents, help_command=None)


@bot.event
async def on_ready():
    print(f"Ready on {bot.user}")


@bot.event
async def on_command_error(ctx, error):
    for i in bot.get_cog("Welcome").walk_commands():
        if str(ctx.command.name) == str(i):
            return
    try:
        ll = ""
        for i in ctx.command.clean_params:
            ll += f"{i} "
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="Error!",
                                  description=f"You are missing a required argument when using the `{ctx.command.name.title()}` command\nArguments "
                                              f"are: `{ll}`",
                                  color=0xff0000)
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send("I cannot find that member!")
        else:
            print(error)
    except Exception:
        return


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
    bot.add_cog(a.Actions(bot))
    bot.add_cog(g.Gen(bot))
    bot.add_cog(m.Mods(bot))
    bot.add_cog(e.Events(bot))
    bot.run(token)


run()
