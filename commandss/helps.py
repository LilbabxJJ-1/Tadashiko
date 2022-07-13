import discord
from discord.ext import commands
from tokens import mycol

Actionhelp = discord.Embed(title="Action Page",
                           description=f"***<Required>*** | ***[Optional]***\n**Commands:**\n\n```Bite "
                                       f"<@user>\nBlush\nCry\nCuddle <@user>\nDance\nHug <@user>\n"
                                       f"Kiss <@user>\nLick <@user>\nPat <@user>\nPoke <@user>\nSlap <@user>\nTickle <@user>```",
                           color=0xffb6c1)

Funhelp = discord.Embed(title="Fun Page",
                           description=f"***<Required>*** | ***[Optional]***\n**Commands:**\n\n```FUN PLACEHOLDER```",
                           color=0xffb6c1)

Utilhelp = discord.Embed(title="Utilities Page",
                           description=f"***<Required>*** | ***[Optional]***\n**Commands:**\n\n```Nickname <new nick>```",
                           color=0xffb6c1)

Confighelp = discord.Embed(title="Help Page",
                           description=f"***<Required>*** | ***[Optional]***\n**Commands:**\n\n```Prefix <new prefix>```",
                           color=0xffb6c1)

