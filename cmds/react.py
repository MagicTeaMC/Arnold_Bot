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

    @commands.command()
    async def 圖片(self, ctx):
            #多種圖片隨機傳送
        random_pic = random.choice(jdata['randompic'])
        rpic = discord.File(random_pic)
        await ctx.send(file=rpic)

    @commands.command()
    async def 原神圖片(self, ctx):
            #多種圖片隨機傳送
        random_pic = random.choice(jdata['原神隨機圖'])
        rpic = discord.File(random_pic)
        await ctx.send(file=rpic)

    @commands.command()
    async def web(self, ctx):
            #網路圖片->去setting設定
        random_pic = random.choice(jdata['url_pic'])
        await ctx.send(random_pic)

async def setup(bot):
    await bot.add_cog(React(bot))