import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open("Setting.json","r",encoding='utf8') as jFile:
    jdata = json.load(jFile)

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self,member):
        #成員加入
        print(f'{member}加入!')
        channel = self.bot.get_channel(int(jdata["join_channel"]))
        await channel.send(f'@{member}加入水果伺服器!')

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        #成員離開
        print(f'{member}離開!')
        channel = self.bot.get_channel(int(jdata["leave_channel"]))
        await channel.send(f'@{member}離開了水果伺服器!')

    @commands.Cog.listener()
    async def on_message(self,msg):
        #多關鍵字回覆
        keyword = ['apple','pie','pen']
        if msg.content in keyword and msg.author != self.bot.user:
            print ("有人輸入多關鍵字的其一")
            await msg.channel.send("hi")

    @commands.Cog.listener()
    async def on_message(self,msg):
        #特定關鍵字回覆
        if msg.content == ("apple")and msg.author != self.bot.user: #前者->關鍵字、後者->要是非機器人傳送的
            print ("有人輸入apple")
            await msg.channel.send("hi") #回覆字元

async def setup(bot):
    await bot.add_cog(Event(bot))