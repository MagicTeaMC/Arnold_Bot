import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import random

with open("Setting.json","r",encoding='utf8') as jFile:
    jdata = json.load(jFile)

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self,member):
        #成員加入
        print(f'{member} 加入 {member.guild} 伺服器!')
        channel = self.bot.get_channel(int(jdata["join_channel"]))
        await channel.send(f'{member} 加入 {member.guild} 伺服器!')

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        #成員離開
        print(f'{member}離開了{member.guild}伺服器!')
        channel = self.bot.get_channel(int(jdata["leave_channel"]))
        await channel.send(f'{member} 離開了 {member.guild} 伺服器!')

    @commands.Cog.listener()
    async def on_member_ban(self,guild,member):
        #成員離開 
        print(f'{member} 被BAN離了 {guild} 伺服器!')
        channel = self.bot.get_channel(int(jdata["leave_channel"]))
        await channel.send(f'{member} 被BAN離了 {guild} 伺服器!')

    @commands.Cog.listener()
    async def on_member_unban(self,guild,member):
        #成員離開
        print(f'{member}UNBAN!')
        channel = self.bot.get_channel(int(jdata["leave_channel"]))
        await channel.send(f'在 {guild} 伺服器 {member} 終於被解BAN了!')

    @commands.Cog.listener()
    async def on_raw_reaction_add(self,data):
        #1.新增反應 --> data
        print(data.member,data.emoji)
        if str(data.emoji) == '<:white_check_mark:>' and str(data.message_id) == str(1065035240298528909) and str(data.guild_id) == str(1064894808419737640): #2.確認圖案
            guild = self.get_guild(data.guild_id)
            role = guild.get_role(1065019704999153684)
            #3.給予身分
            await data.member.add_roles(role)
    


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

        if msg.content == ("凌晨安") and msg.author != self.bot.user: #前者->關鍵字、後者->要是非機器人傳送的
            print ("凌晨安")
            await msg.channel.send("閉嘴，你凌晨起來幹嘛 ||打炮?||" )

        if msg.content == ("你好") and msg.author != self.bot.user: #前者->關鍵字、後者->要是非機器人傳送的
            print ("你好")
            await msg.channel.send("你好啊" )

        if msg.content == ("確實") and msg.author != self.bot.user: #前者->關鍵字、後者->要是非機器人傳送的
            print ("確實")
            pic = discord.File(jdata['確實'])
            await msg.channel.send(file=pic)

        if msg.content == ("不知道"): #and msg.author != self.bot.user: #前者->關鍵字、後者->要是非機器人傳送的
            print ("不知道")
            pic = discord.File(jdata['不知道'])
            await msg.channel.send(file=pic)

        if msg.content == ("你犯法") and msg.author != self.bot.user: #前者->關鍵字、後者->要是非機器人傳送的
            print ("犯法")
            pic = discord.File(jdata['犯法'])
            await msg.channel.send(file=pic)
            await msg.channel.send("不知道")

        if msg.content == ("我沒錢") and msg.author != self.bot.user: #前者->關鍵字、後者->要是非機器人傳送的
            print ("我沒錢")
            pic = discord.File(jdata['沒錢'])
            await msg.channel.send(file=pic)

        if msg.content == ("氣死") and msg.author != self.bot.user: #前者->關鍵字、後者->要是非機器人傳送的
            print ("氣死")
            pic = discord.File(jdata['氣死'])
            await msg.channel.send("起司??")
            await msg.channel.send(file=pic)

        if msg.content == ("你有強迫症") and msg.author != self.bot.user: #前者->關鍵字、後者->要是非機器人傳送的
            print ("強迫症")
            pic = discord.File(jdata['強迫症'])
            await msg.channel.send(file=pic)

        if msg.content == ("TNT拿來") and msg.author != self.bot.user: #前者->關鍵字、後者->要是非機器人傳送的
            print ("TNT")
            pic = discord.File(jdata['TNT'])
            await msg.channel.send(file=pic)
        
        if msg.content == ("NoTag") and msg.author != self.bot.user: #前者->關鍵字、後者->要是非機器人傳送的
            print ("NoTag")
            pic = discord.File(jdata['NoTag'])
            await msg.channel.send(file=pic)

        if msg.content == ("好問題") and msg.author != self.bot.user: #前者->關鍵字、後者->要是非機器人傳送的
            print ("好問題")
            pic = discord.File(jdata['好問題'])
            await msg.channel.send(file=pic)

        if msg.content == ("XD"or"xd") and msg.author != self.bot.user: #前者->關鍵字、後者->要是非機器人傳送的
            print ("XD")
            pic = discord.File(jdata['XD'])
            await msg.channel.send(file=pic)
'''
        # 預設錯誤訊息
        error = []

        # 處理輸入文字
        content = msg.content.replace(' ', '').lower()

        # 如果是「!roll」開頭的訊息
        if msg.content.startswith('!roll') and msg.author != self.bot.user:
            content = content.replace('!roll', '')

            # 骰子數量計算
            dice_cont = content.split('d')[0]

            try:
                dice_cont = int(dice_cont)

            except ValueError:
                error.append('擲出多少個骰子必須是整數！')

            # 骰子類型判斷
            content = content.split('d')[1]
            dice_type = content.split('>')[0]
            try:
                dice_type = int(dice_type)

            except ValueError:
                error.append('骰子類型必須是整數！')

            # 成功判斷
            if '>' in content:
                success = content.split('>')[1]
                try:
                    success = int(success)    
                except ValueError:
                    error.append('成功條件必須是整數！')

            else:
                success = 0

            if len(error) == 0:
                success_count = 0
                result_msg = ''

                # 擲骰子
                results = [random.randint(1, dice_type) for _ in range(dice_cont)]

                for result in results:
                    if success > 0 and result >= success:
                        success_count += 1
                    result_msg += f'`{result}`, '
                
                await message.channel.send(result_msg)

                if success > 0:
                    await message.channel.send(f'Success: `{success_count}`')
            else:
                await message.channel.send(error)
'''
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