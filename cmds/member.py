import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import asyncio

with open("Setting.json","r",encoding='utf8') as jFile:
    jdata = json.load(jFile)

class Member(Cog_Extension):
        @commands.command()
        async def kick(self,user1:discord.User,*reason1:str):
            await user1.kick(user=user1,  reason=reason1)

        @commands.command()
        async def timeout(self,user1:discord.User,until,*reason1:str):
            await user1.timeout(user=user1,until=until,reason=reason1)
            
        @commands.command()
        @commands.has_permissions(manage_messages=True) # 檢查用戶是否有管理訊息的權限
        async def mute(ctx, duration: int = 300, *, reason: str = None, member: discord.Member):
            if duration is None:
                await member.edit(mute=True, reason=reason)
                await ctx.send(f'{member.mention} 已經被禁言了。')
            else:
                await member.edit(mute=True, reason=reason)
                await ctx.send(f'{member.mention} 已經被禁言了，禁言時間為 {duration} 秒。，管理員{ctx.author.mention}')
                await asyncio.sleep(duration)
                await member.edit(mute=False)
                await ctx.send(f'{member.mention} 的禁言已經解除了。')
            
        @commands.command()
        async def give_role(self,ctx,user:discord.User):
            for i in range(0,len(ctx.member.roles)):
                guild = ctx.guild
                role1 = guild.get_role(1094203836467511328)
                if role1 == member.role[i]:

                    role = guild.get_role(1081307034923827313)
                    await user.add_roles(role,reason="企業指令")
                    await ctx.channel.send("成功")



async def setup(bot):
    await bot.add_cog(Member(bot))