import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Main(Cog_Extension):
    

    @commands.command()
    async def ping(self,ctx): #ctx (上下文，回覆的上下關係) 
        #A：嗨(上文)(使用者，ID，伺服器，頻道)
        #B：安安(下文)
        await ctx.send(f'{round(self.bot.latency*1000)}(ms)') #預設單位為秒

def setup(bot):
    bot.add_cog(Main(bot))