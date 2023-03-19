import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open("Setting.json","r",encoding='utf8') as jFile:
    jdata = json.load(jFile)

class Member(Cog_Extension):
        @commands.command()
        async def kick(self,user1:discord.User,reason1:str):
            await user1.kick(user=user1,  reason=reason1)

        @commands.command()
        async def timeout(self,user1:discord.User,until,reason1:str):
            await user1.timeout(user=user1,until=until,reason=reason1)



async def setup(bot):
    await bot.add_cog(Member(bot))