import discord
from discord.ext import commands
from core.classes import Cog_Extension
import datetime

class Main(Cog_Extension):

    @commands.command()
    async def ping(self,ctx): 
        #ctx (上下文，回覆的上下關係) 
        #A：嗨(上文)(使用者，ID，伺服器，頻道)
        #B：安安(下文)
        await ctx.send(f'{round(self.bot.latency*1000)}(ms)') #預設單位為秒

    @commands.command()
    async def em(self,ctx):
        #崁入功能-> https://cog-creators.github.io/discord-embed-sandbox/
        embed=discord.Embed(title="功能", color=0x2fe7f4,
        timestamp=datetime.datetime.now())
        embed.set_author(name="由3.14159265358#6111創建")
        embed.add_field(name="$ping", value="查詢延遲", inline=True)
        embed.add_field(name="$圖片", value="BOT圖片", inline=True)
        embed.add_field(name="$web", value="網路圖片", inline=True)
        embed.add_field(name="4", value="44", inline=True)
        await ctx.send(embed=embed)

    @commands.command()
    async def say(self,ctx,msg):
            #使用機器人講話
        #刪訊息
        await ctx.message.delete()
        #複誦
        await ctx.send(msg)

async def setup(bot):
    await bot.add_cog(Main(bot))