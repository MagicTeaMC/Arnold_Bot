import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open("Setting.json","r",encoding='utf8') as jFile:
    jdata = json.load(jFile)

class React(Cog_Extension):
    @commands.command()
    async def 單一圖片(self, ctx):
            #如指令所示
        pic = discord.File(jdata['pic'])
        await ctx.send(file=pic)
        channel = self.bot.get_channel(int(jdata["後台"]))
        await channel.send(f'{ctx.author} 在 {ctx.guild} 的 {ctx.channel} 召喚單一圖片!')

    @commands.command()
    async def 圖片(self, ctx):
            #多種圖片隨機傳送
        random_pic = random.choice(jdata['randompic'])
        rpic = discord.File(random_pic)
        await ctx.send(file=rpic)
        channel = self.bot.get_channel(int(jdata["後台"]))
        await channel.send(f'{ctx.author} 在 {ctx.guild} 的 {ctx.channel} 召喚隨機圖片!')

    @commands.command()
    async def 原神圖片(self, ctx):
            #多種圖片隨機傳送
        random_pic = random.choice(jdata['原神隨機圖'])
        rpic = discord.File(random_pic)
        await ctx.send(file=rpic)
        channel = self.bot.get_channel(int(jdata["後台"]))
        await channel.send(f'{ctx.author} 在 {ctx.guild} 的 {ctx.channel} 召喚隨機原神圖片!')

    @commands.command()
    async def web(self, ctx):
            #網路圖片->去setting設定
        random_pic = random.choice(jdata['url_pic'])
        await ctx.send(random_pic)
        channel = self.bot.get_channel(int(jdata["後台"]))
        await channel.send(f'{ctx.author} 在 {ctx.guild} 的 {ctx.channel} 召喚網路隨機圖片!')



'''
    @commands.command()
    async def giverole(self, ctx, member: discord.Member):
        guild=self.bot.get_guild(你的伺服器id)
        role =guild.get_role(身分組id)
        await member.add_roles(role)
'''


async def setup(bot):
    await bot.add_cog(React(bot))