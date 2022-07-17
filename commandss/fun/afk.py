# <----------------------------------MainImports---------------------------------------->
import discord
from discord.ext import commands
from tokens import mycol, warning, color


# <----------------------------------Bot---------------------------------------->

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def afk(self, ctx):
        if ctx.author.id == self.bot.user.id:
            verified = mycol.find_one({"key": f"accepted_{ctx.author.id}"})
            afk = mycol.find_one({"key": f"afks_{ctx.author.id}"})
            prefix = mycol.find_one({"key": f"prefix_{ctx.guild.id}"})
            if verified is None:
                await ctx.send(embed=warning)
            if afk is not None:
                q = {"key": f"afks_{ctx.author.id}"}
                mycol.update_one(q, {"$search": {"data": "true"}})
                if prefix is not None:
                    msg = str(ctx.message.content)
                    msg = msg.replace(f"{prefix['data']}afk ", "")
                    if msg == "":
                        mycol.update_one()
                    print(msg)
                else:
                    msg = str(ctx.message.content)
                    msg = msg.replace("t!afk ", "")
        # NOT FINISHED

    @commands.command()
    async def gay(self, ctx, user: discord.Member = None):
        if mycol.find_one({"key": f"accepted_{ctx.author.id}"}) is None:
            await ctx.send(warning)
            return
        if user is not None:
            embed = discord.Embed(title="Gayyyy🌈", color=color)
            embed.set_image(url=f"https://vslapi.cf/api/gay?avatar={user.display_avatar}")
            await ctx.send(embed=embed)
        elif user is None:
            embed = discord.Embed(title="Gayyyy🌈", color=color)
            embed.set_image(url=f"https://vslapi.cf/api/gay?avatar={ctx.author.display_avatar}")
            await ctx.send(embed=embed)

    @commands.command()
    async def criminal(self, ctx, user: discord.Member = None):
        if mycol.find_one({"key": f"accepted_{ctx.author.id}"}) is None:
            await ctx.send(warning)
            return
        if user is not None:
            embed = discord.Embed(title="Wanted criminal!", color=color)
            embed.set_image(url=f"https://hunterapi.sytes.net/wanted?img={user.display_avatar}")
            await ctx.send(embed=embed)
        elif user is None:
            embed = discord.Embed(title="Wanted criminal!", color=color)
            embed.set_image(url=f"https://hunterapi.sytes.net/wanted?img={ctx.author.display_avatar}")
            await ctx.send(embed=embed)
