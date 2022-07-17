import discord
from discord.ext import commands
from tokens import mycol, color

unverified = discord.Embed(title="Rules and Conditions", description="""
**:exclamation: Rules and Conditions agreement :exclamation:**
 
   **--** Commands may **NOT** be used for malicious intents!
   **--** Using unfair tactics, such as scripts or multiple accounts are **NOT** allowed
   **--** Any abuse of commands through loopholes is **NOT** allowed
   **--** No one is allowed to copy or steal aspects of tadashiko that may suggest that the bot was cloned
  
  *Anyone found to be using Tadashiko for bad reasons or breaking any rules, will have their account banned from using commands*
  
  Please use type `accept` to accept the rules and conditions for Tadashiko Bot:tm: then you can use my commands freely as you like!""",
                           color=color)

Actionhelp = discord.Embed(title="Action Page",
                           description=f"***<Required>*** | ***[Optional]***\n**Commands:**\n\n```Bite "
                                       f"<@user>\nBlush\nCry\nCuddle <@user>\nDance\nHug <@user>\n"
                                       f"Kiss <@user>\nLick <@user>\nPat <@user>\nPoke <@user>\nSlap <@user>\nTickle <@user>```",
                           color=0xffb6c1)

Funhelp = discord.Embed(title="Fun Page",
                        description=f"***<Required>*** | ***[Optional]***\n**Commands:**\nUpdate Still in progress\n\n```FUN PLACEHOLDER```",
                        color=0xffb6c1)

Utilhelp = discord.Embed(title="Utilities Page",
                         description=f"***<Required>*** | ***[Optional]***\n**Commands:**\nUpdate Still in progress\n\n```Nickname <new nick>```",
                         color=0xffb6c1)

Confighelp = discord.Embed(title="Config Page",
                           description=f"***<Required>*** | ***[Optional]***\n**Commands:**\n\n```Welcome-message\nWelcome-title\nWelcome-Image"
                                       f"\nWelcome-footer\nWelcome-color\nWelcome-channel\nWelcome-enable/diable\nTest-welcome\nPrefix <new "
                                       f"prefix>```",
                           color=0xffb6c1)

MusicHelp = discord.Embed(title="Music Page",
                          description=f"***<Required>*** | ***[Optional]***\n**Commands:**\nUpdate Still in progress\n\n```Play "
                                      f"<song>\nPause\nResume\nLyrics <Song>\nQueue\nJoin```",
                          color=color)
