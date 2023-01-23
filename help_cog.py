import discord
from discord.ext import commands

class help_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.help_message = """
```
一般命令：
/help - 顯示所有可用命令
/p <keywords> - 在 youtube 上找到歌曲並在您當前的頻道中播放。 如果暫停，將繼續播放當前歌曲
/q - 顯示當前音樂隊列
/skip - 跳過當前正在播放的歌曲
/clear - 停止音樂並清空隊列
/leave - 斷開機器人與語音通道的連接
/pause - 暫停當前正在播放的歌曲，如果已經暫停則繼續播放
/resume - 恢復播放當前歌曲
```
"""
        self.text_channel_list = []

    #some debug info so that we know the bot has started    
    @commands.Cog.listener()
    async def on_ready(self):
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                self.text_channel_list.append(channel)

        await self.send_to_all(self.help_message)        

    @commands.command(name="help", help="顯示所有可用命令")
    async def help(self, ctx):
        await ctx.send(self.help_message)

    async def send_to_all(self, msg):
        for text_channel in self.text_channel_list:
            await text_channel.send(msg)