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
        await channel.send(f'@{member}加入伺服器!')

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        #成員離開
        print(f'{member}離開!')
        channel = self.bot.get_channel(int(jdata["leave_channel"]))
        await channel.send(f'@{member}離開了伺服器!')

    @commands.Cog.listener()
    async def on_message(self,msg):
        #on_message必須寫在一個def裡
        
        if msg.content == ("apple") : #關鍵字
            #特定關鍵字回覆
            print ("有人輸入apple")
            await msg.channel.send("水果伺服器歡迎你") #回覆字元
        
        if msg.content == ("早安") and msg.author != self.bot.user: #前者->關鍵字、後者->要是非機器人傳送的
            print ("早安")
            await msg.channel.send("早上好啊" )

        if msg.content == ("午安") and msg.author != self.bot.user: #前者->關鍵字、後者->要是非機器人傳送的
            print ("午安")
            await msg.channel.send("吃午餐了嗎?" )

        if msg.content == ("晚安") and msg.author != self.bot.user: #前者->關鍵字、後者->要是非機器人傳送的
            print ("晚安")
            await msg.channel.send("晚安，去睡覺了" )

        if msg.content == ("你好") and msg.author != self.bot.user: #前者->關鍵字、後者->要是非機器人傳送的
            print ("你好")
            await msg.channel.send("你好啊" )

        if msg.content == ("確實") and msg.author != self.bot.user: #前者->關鍵字、後者->要是非機器人傳送的
            print ("確實")
            pic = discord.File(jdata['確實'])
            await msg.channel.send(file=pic)
'''
    @commands.Cog.listener()
    async def on_message(self,msg):
        #特定關鍵字回覆
        if msg.content == ("apple") and msg.author != self.bot.user: #前者->關鍵字、後者->要是非機器人傳送的
            print ("有人輸入apple")
            await msg.channel.send("hi") #回覆字元

        keyword = ['banana','pie','pen']
        if (msg.content in keyword) and (msg.author != self.bot.user):
            #多關鍵字回覆
            print ("有人輸入多關鍵字的其一")
            await msg.channel.send("hi1")#回覆字元
'''

async def setup(bot):
    await bot.add_cog(Event(bot))