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
        pic = discord.File(jdata['pic'])
        await ctx.send(file=pic)

    @commands.command()
    async def 圖片(self, ctx):
        random_pic = random.choice(jdata['randompic'])
        rpic = discord.File(random_pic)
        await ctx.send(file=rpic)

    @commands.command()
    async def web(self, ctx):
        random_pic = random.choice(jdata['url_pic'])
        await ctx.send(random_pic)

async def setup(bot):
    await bot.add_cog(React(bot))