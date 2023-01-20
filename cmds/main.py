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
    async def 功能(self,ctx):
        #崁入功能-> https://cog-creators.github.io/discord-embed-sandbox/
        embed=discord.Embed(title="功能", color=0x2fe7f4,
        timestamp=datetime.datetime.now())
        embed.set_author(name="本機器人由3.14159265358#6111創建")
        embed.add_field(name="$help", value="顯示可輸入的指令", inline=True)
        embed.add_field(name="$功能", value="顯示此畫面", inline=True)
        embed.add_field(name="$ping", value="查詢延遲", inline=True)
        embed.add_field(name="$圖片", value="BOT圖片", inline=True)
        embed.add_field(name="$web", value="網路圖片", inline=True)
        embed.add_field(name="$say [內容]", value="使用機器人講話", inline=True)
        embed.add_field(name="$clean [數量]", value="移除訊息[數量]則", inline=True)
        embed.add_field(name="$原神圖片", value="顯示原神圖片", inline=True)
        embed.add_field(name="$回覆", value="顯示所有回覆訊息", inline=True)
        embed.add_field(name="其他", value="其實還有其他內容，等你去發現🤣", inline=False)
        await ctx.send(embed=embed)
        print("有人召喚了功能說明")

    @commands.command()
    async def 回覆(self,ctx):
        #崁入功能-> https://cog-creators.github.io/discord-embed-sandbox/
        embed=discord.Embed(title="回覆", color=0x2fe7f4,
        timestamp=datetime.datetime.now())
        embed.set_author(name="本機器人由3.14159265358#6111創建")
        embed.add_field(name="apple", value="歡迎", inline=True)
        embed.add_field(name="早安", value="問候", inline=True)
        embed.add_field(name="午安", value="問候", inline=True)
        embed.add_field(name="晚安", value="問候", inline=True)
        embed.add_field(name="你好", value="問候", inline=True)
        embed.add_field(name="確實", value="梗圖", inline=True)
        embed.add_field(name="不知道", value="梗圖", inline=True)
        embed.add_field(name="你犯法", value="梗圖", inline=True)
        embed.add_field(name="我沒錢", value="梗圖", inline=True)
        embed.add_field(name="你有強迫症", value="梗圖", inline=True)
        embed.add_field(name="TNT拿來", value="梗圖", inline=True)
        embed.add_field(name="氣死", value="梗圖", inline=False)
        await ctx.send(embed=embed)
        print("有人召喚了回覆說明")

    @commands.command()
    async def say(self,ctx,*,msg):
            #使用機器人講話
        #刪訊息
        await ctx.message.delete()
        #複誦
        await ctx.send(msg)
        print("被逼說：",msg)

    @commands.command()
    async def clean(self,ctx,num:int,reason1):
      await ctx.channel.purge(limit=num+1,reason=reason1)
      print("清理了",num,"則訊息,因為",reason1)

    @commands.command()
    async def random(self,ctx):
        print(ctx.guild.members)
        #await ctx.send(ctx.guild.members)

async def setup(bot):
    await bot.add_cog(Main(bot))