import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import random
import asyncio
import datetime

with open("Setting.json","r",encoding='utf8') as jFile:
    jdata = json.load(jFile)

async def get_participants(message):
    participants = []
    async for user in message.reactions[0].users():
        if not user.bot:
            participants.append(user)
    return participants

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self,member):
        #成員加入
        if int(member.guild.id)==int(1091920457189572778):
            print(f'{member} 加入 {member.guild} !')
            channel = self.bot.get_channel(int(jdata["join_channel"]))
            await channel.send(f'{member.mention} 加入 {member.guild} !')
        elif int(member.guild.id)==int(1078082303256969317):
            print(f'{member} 加入 {member.guild} !')
            channel = self.bot.get_channel(int(jdata["bird_channel"]))
            await channel.send(f'{member.mention} 加入 {member.guild} !')
            role_ids = [1094181672708214824, 1094031097517580308, 1094030992311853117, 1094031438418022460]
            for role_id in role_ids:
                role = discord.utils.get(member.guild.roles, id=role_id)
                await member.add_roles(role)

        elif int(member.guild.id)==int(1061070549566103622):
            print(f'{member} 加入 {member.guild} !')
            channel = self.bot.get_channel(int(jdata["Star"]))
            await channel.send(f'{member.mention} 加入 {member.guild} !')
        else:
            print(f'{member} 加入 {member.guild} !')
            channel = self.bot.get_channel(int(jdata["後台"]))
            await channel.send(f'{member.mention} 加入 {member.guild} !')
            
    @commands.Cog.listener()
    async def on_member_remove(self,member):
        #成員離開
        if int(member.guild.id)==int(1091920457189572778):
            print(f'{member}離開了{member.guild}!')
            channel = self.bot.get_channel(int(jdata["join_channel"]))
            await channel.send(f'{member.mention} 離開了 {member.guild} !')
        elif int(member.guild.id)==int(1078082303256969317):
            print(f'{member}離開了{member.guild}!')
            channel = self.bot.get_channel(int(jdata["bird_channel"]))
            await channel.send(f'{member.mention} 離開了 {member.guild} !')
        elif int(member.guild.id)==int(1061070549566103622):
            print(f'{member}離開了{member.guild}伺服器!')
            channel = self.bot.get_channel(int(jdata["Star"]))
            await channel.send(f'{member.mention} 離開了 {member.guild} !')
        else:
            print(f'{member}離開了{member.guild}伺服器!')
            channel = self.bot.get_channel(int(jdata["後台"]))
            await channel.send(f'{member.mention} 離開了 {member.guild} !')

    @commands.Cog.listener()
    async def on_member_ban(self,guild,member):
        #成員離開 
        if int(member.guild.id)==int(1091920457189572778):
            print(f'{member} 被BAN離了 {member.guild}伺服器!')
            channel = self.bot.get_channel(int(jdata["join_channel"]))
            await channel.send(f'{member.mention} 被BAN離了 {member.guild} !')
        elif int(member.guild.id)==int(1078082303256969317):
            print(f'{member} 被BAN離了 {member.guild}伺服器!')
            channel = self.bot.get_channel(int(jdata["bird_channel"]))
            await channel.send(f'{member.mention} 被BAN離了 {member.guild} !')
        elif int(member.guild.id)==int(1061070549566103622):
            print(f'{member} 被BAN離了 {member.guild}伺服器!')
            channel = self.bot.get_channel(int(jdata["Star"]))
            await channel.send(f'{member.mention} 被BAN離了 {member.guild} !')
        else:
            print(f'{member} 被BAN離了 {member.guild}伺服器!')
            channel = self.bot.get_channel(int(jdata["後台"]))
            await channel.send(f'{member.mention} 被BAN離了 {member.guild} !')

    @commands.Cog.listener()
    async def on_member_unban(self,guild,member):
        #成員離開
        if int(member.guild.id)==int(1091920457189572778):
            print(f'{member} 在 {member.guild} UNBAN!')
            channel = self.bot.get_channel(int(jdata["join_channel"]))
            await channel.send(f'在 {guild}  {member.mention} 終於被解BAN了!')
        elif int(member.guild.id)==int(1078082303256969317):
            print(f'{member} 在 {member.guild} UNBAN!')
            channel = self.bot.get_channel(int(jdata["bird_channel"]))
            await channel.send(f'在 {guild}  {member.mention} 終於被解BAN了!')
        elif int(member.guild.id)==int(1061070549566103622):
            print(f'{member} 在 {member.guild} UNBAN!')
            channel = self.bot.get_channel(int(jdata["Star"]))
            await channel.send(f'在 {guild}  {member.mention} 終於被解BAN了!')
        else:
            print(f'{member} 在 {member.guild} UNBAN!')
            channel = self.bot.get_channel(int(jdata["後台"]))
            await channel.send(f'在 {guild.mention}  {member} 終於被解BAN了!')

    @commands.Cog.listener()
    async def on_raw_reaction_add(self,data):
        #1.新增反應 --> data
        print(data.member,data.emoji)
        if str(data.emoji) == '💀' and str(data.message_id) == str(1086515736723337237) and str(data.guild_id) == str(1078082303256969317): #2.確認圖案
            print('輸入💀')
            channel = self.bot.get_channel(int(jdata["後台"]))
            await channel.send(f"{data.member.mention} 輸入 {data.emoji}")
            guild = self.bot.get_guild(data.guild_id)
            role = guild.get_role(1078082303256969318)
            #3.給予身分
            await data.member.add_roles(role,reason="新增反映後台身分")
            await data.member.send(f"你取得了 {role} 這個身分組!")

        if str(data.emoji) == '🔹' and str(data.message_id) == str(1086515736723337237) and str(data.guild_id) == str(1078082303256969317): #2.確認圖案
            print('輸入🔹')
            channel = self.bot.get_channel(int(jdata["後台"]))
            await channel.send(f"{data.member.mention} 輸入 {data.emoji}")
            guild = self.bot.get_guild(data.guild_id)
            role = guild.get_role(1078082303256969320)
            #3.給予身分
            await data.member.add_roles(role,reason="新增反映原神身分")
            await data.member.send(f"你取得了 {role} 這個身分組!")

        if str(data.emoji) == '🈲' and str(data.message_id) == str(1086515736723337237) and str(data.guild_id) == str(1078082303256969317): #2.確認圖案
            print('輸入 🈲')
            channel = self.bot.get_channel(int(jdata["後台"]))
            await channel.send(f"{data.member.mention} 輸入 {data.emoji}")
            guild = self.bot.get_guild(data.guild_id)
            role = guild.get_role(1078082303256969319)
            #3.給予身分
            await data.member.add_roles(role,reason="新增反映18+身分")
            await data.member.send(f"你取得了 {role} 這個身分組!")
        if str(data.emoji) == '🇨' and str(data.message_id) == str(1086515736723337237) and str(data.guild_id) == str(1078082303256969317): 
            print('輸入 🇨')
            channel = self.bot.get_channel(int(jdata["後台"]))
            await channel.send(f"{data.member.mention} 輸入 {data.emoji}")
            guild = self.bot.get_guild(data.guild_id)
            role = guild.get_role(1093223889234051173)
            #3.給予身分
            await data.member.add_roles(role,reason="新增反映ChatGPT身分")
            await data.member.send(f"你取得了 {role} 這個身分組!")

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self,data):
        #1.新增反應 --> data
        print(data.member,data.emoji)
        if str(data.emoji) == '💀' and str(data.message_id) == str(1086515736723337237) and str(data.guild_id) == str(1078082303256969317): #2.確認圖案
            print('移除💀')
            channel = self.bot.get_channel(int(jdata["後台"]))
            guild = self.bot.get_guild(data.guild_id)
            user = guild.get_member(data.user_id)
            role = guild.get_role(1078082303256969318)
            #3.給予身分
            await channel.send(f"{user.mention} 移除 {data.emoji}")
            await user.remove_roles(role,reason="移除反映後台身分")
            await user.send(f"你移除了 {role} 這個身分組!")

        if str(data.emoji) == '🔹' and str(data.message_id) == str(1086515736723337237) and str(data.guild_id) == str(1078082303256969317): #2.確認圖案
            print('移除🔹')
            channel = self.bot.get_channel(int(jdata["後台"]))
            guild = self.bot.get_guild(data.guild_id)
            user = guild.get_member(data.user_id)
            role = guild.get_role(1078082303256969320)
            #3.給予身分
            await channel.send(f"{user.mention} 移除 {data.emoji}")
            await user.remove_roles(role,reason="移除反映原神身分")
            await user.send(f"你移除了 {role} 這個身分組!")

        if str(data.emoji) == '🈲' and str(data.message_id) == str(1086515736723337237) and str(data.guild_id) == str(1078082303256969317): #2.確認圖案
            print('移除🈲')
            channel = self.bot.get_channel(int(jdata["後台"]))
            guild = self.bot.get_guild(data.guild_id)
            user = guild.get_member(data.user_id)
            role = guild.get_role(1078082303256969319)
            #3.給予身分
            await channel.send(f"{user.mention} 移除 {data.emoji}")
            await user.remove_roles(role,reason="移除反映18+身分")
            await user.send(f"你移除了 {role} 這個身分組!")
        if str(data.emoji) == '🇨' and str(data.message_id) == str(1086515736723337237) and str(data.guild_id) == str(1078082303256969317): 
            print('🇨')
            channel = self.bot.get_channel(int(jdata["後台"]))
            guild = self.bot.get_guild(data.guild_id)
            user = guild.get_member(data.user_id)
            role = guild.get_role(1093223889234051173)
            #3.給予身分
            await channel.send(f"{user.mention} 移除 {data.emoji}")
            await user.remove_roles(role,reason="移除反映ChatGPT身分")
            await user.send(f"你移除了 {role} 這個身分組!")

    @commands.Cog.listener()
    async def on_message_delete(self,msg):
        counter = 1
        async for audilog in msg.guild.audit_logs(action=discord.AuditLogAction.message_delete):
            if counter == 1:
                if msg.guild.id == int(1064894808419737640):
                        self.channel = self.bot.get_channel(1066150094790992033)
                        embed=discord.Embed(title="訊息刪除", color=0xff0000)
                        embed.add_field(name="被刪除訊息", value=msg.content, inline=False)
                        embed.add_field(name="原作者", value=msg.author, inline=True)
                        embed.add_field(name="刪除者", value=audilog.user.name, inline=True)
                        await self.channel.send(embed=embed)
                counter += 1
    
    #'''
    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        if isinstance(error,commands.errors.MissingRequiredAttachment):
            await ctx.send("遺失參數，如右問題請至：https://discord.gg/NdqxvRgGyf 詢問(需領取身分)")
            channel = self.bot.get_channel(int(jdata["後台"]))
            await channel.send(f'{ctx.author.mention} 在 {ctx.guild} 的 {ctx.channel.mention} 發生"遺失參數"的錯誤! 運行指令：{ctx.message.content}')
        elif isinstance(error,commands.errors.CommandNotFound):
            await ctx.send("指令不存在")
            channel = self.bot.get_channel(int(jdata["後台"]))
            await channel.send(f'{ctx.author.mention} 在 {ctx.guild} 的 {ctx.channel.mention} 發生"指令不存在"的錯誤! 運行指令：{ctx.message.content}')
        else:
            await ctx.send("發生錯誤，請向製作者回報(https://discord.gg/NdqxvRgGyf 需領取身分)")
            channel = self.bot.get_channel(int(jdata["後台"]))
            await channel.send(f'{ctx.author.mention} 在 {ctx.guild} 的 {ctx.channel.mention} 發生錯誤! 運行指令：{ctx.message.content}')
    #'''

    @commands.Cog.listener()
    async def on_message(self,msg):
        #on_message必須寫在一個def裡
        guildlist = []
        if msg.channel.id == int(1078082303294705714)and msg.author != self.bot.user:
            if msg.content == ("加入公會"):
                my_id = "876035367348867102"
                await msg.channel.send(f"如果您要加入公會，請輸入\n1.Minecraft的ID：\n2.Discord名稱，須包含 #後4位數(請用tag)：\n3.有加入的其他公會：\n並用「，」分隔\n例如：ChenArnold，<@{my_id}>，鷹之國、蘋果村\n備註：填錯格式沒加入不要來找我(沒用逗點分隔)\n\n只是想聊天請打「我只是來聊天」")
            elif msg.content == ("我只是來聊天"):
                guild = self.bot.get_guild(msg.guild.id)
                role = guild.get_role(1086798962180235296)
                await msg.author.add_roles(role,reason="填寫資料加入聊天")
                await msg.add_reaction("✅")
                await msg.author.send(f"你加入了鷹之國公會(聊天)")
                await msg.channel.send("輸入成功，已給予身分")
                channel = self.bot.get_channel(int(jdata["後台"]))
                await channel.send(str(msg.author.mention)+"加入鷹之國(聊天)")
                print(str(msg.author)+"加入鷹之國(聊天)")
            else:
                try:
                    guildlist = msg.content.split("，")
                    embed=discord.Embed(title="加入公會", color=0x2febf9,
                    timestamp=datetime.datetime.now())
                    embed.add_field(name="Minecraft ID", value=guildlist[0], inline=True)
                    embed.add_field(name="Discord ID", value=guildlist[1], inline=True)
                    embed.add_field(name="加入的其他公會", value=guildlist[2], inline=False)
                    embed.add_field(name="填寫者", value=msg.author.mention, inline=False)
                except IndexError:
                    await msg.channel.send("填入的逗點過少，請更正並檢查後再傳送")
                    await msg.add_reaction("❌")
                except:
                    await msg.channel.send("發生錯誤，請檢查後再發送")
                    await msg.add_reaction("❌")
                else:
                    guild = self.bot.get_guild(msg.guild.id)
                    role = guild.get_role(1078082303256969325)
                    channel = self.bot.get_channel(int(jdata["加入公會"]))
                    await channel.send(embed=embed)
                    await msg.author.add_roles(role,reason="填寫資料加入公會")
                    await msg.add_reaction("✅")
                    rule_channel = "1078082303294705711"
                    await msg.author.send(f"歡迎加入鷹之國公會，記得去得規定，犯錯不要來怪別人喔 <#{rule_channel}>")
                    #await msg.channel.send("輸入成功，已給予身分")
                    await msg.author.edit(nick=f'[成員]{guildlist[0]}')
                    channel = self.bot.get_channel(int(jdata["後台"]))
                    await channel.send(str(msg.author.mention)+"加入鷹之國")
                    print(str(msg.author)+"加入鷹之國")
        else:
            if msg.content.startswith('!抽獎'):
                # 取得抽獎訊息的資訊
                content = msg.content.split()
                if len(content) < 3:
                    await msg.channel.send('請輸入正確的指令格式: `!抽獎 獎品 結束時間(秒)`')
                    return

                prize = content[1]
                end_time = int(content[2])

                # 發送抽獎訊息並設置反應
                giveaway_message = await msg.channel.send(f'🎉 **抽獎** 🎉\n\n獎品: {prize}\n結束時間: {end_time} 秒\n\n按下 👉 參加抽獎 👈')
                await giveaway_message.add_reaction('👉')

                # 等待設置時間到達並選擇獲勝者
                await asyncio.sleep(end_time)
                participants = await get_participants(giveaway_message)
                winner = random.choice(participants)

                # 發送獲勝者訊息
                await msg.channel.send(f'恭喜 {winner.mention} 獲得抽獎獎品: {prize}！')
            if msg.content == ("apple") : #關鍵字
                #特定關鍵字回覆
                print ("有人輸入apple")
                channel = self.bot.get_channel(int(jdata["後台"]))
                await channel.send(f"{msg.author.mention} 在 {msg.guild} 的 {msg.channel.mention} 輸入 {msg.content}")
                await msg.channel.send("水果伺服器歡迎你") #回覆字元
            
            if msg.content == ("早安"): #前者->關鍵字、後者->要是非機器人傳送的
                print ("早安")
                channel = self.bot.get_channel(int(jdata["後台"]))
                await channel.send(f"{msg.author.mention} 在 {msg.guild} 的 {msg.channel.mention} 輸入 {msg.content}")
                await msg.channel.send("早上好啊" )

            if msg.content == ("午安"): #前者->關鍵字、後者->要是非機器人傳送的
                print ("午安")
                channel = self.bot.get_channel(int(jdata["後台"]))
                await channel.send(f"{msg.author.mention} 在 {msg.guild} 的 {msg.channel.mention} 輸入 {msg.content}")
                await msg.channel.send("吃午餐了嗎?" )

            if msg.content == ("晚安"): #前者->關鍵字、後者->要是非機器人傳送的
                print ("晚安")
                channel = self.bot.get_channel(int(jdata["後台"]))
                await channel.send(f"{msg.author.mention} 在 {msg.guild} 的 {msg.channel.mention} 輸入 {msg.content}")
                await msg.channel.send("晚安，去睡覺了" )

            if msg.content == ("凌晨安"): #前者->關鍵字、後者->要是非機器人傳送的
                print ("凌晨安")
                channel = self.bot.get_channel(int(jdata["後台"]))
                await channel.send(f"{msg.author.mention} 在 {msg.guild} 的 {msg.channel.mention} 輸入 {msg.content}")
                await msg.channel.send("閉嘴，你凌晨起來幹嘛 ||打炮?||" )

            if msg.content == ("你好"): #前者->關鍵字、後者->要是非機器人傳送的
                print ("你好")
                channel = self.bot.get_channel(int(jdata["後台"]))
                await channel.send(f"{msg.author.mention} 在 {msg.guild} 的 {msg.channel.mention} 輸入 {msg.content}")
                await msg.channel.send("你好啊" )

            if msg.content == ("確實"): #前者->關鍵字、後者->要是非機器人傳送的
                print ("確實")
                channel = self.bot.get_channel(int(jdata["後台"]))
                await channel.send(f"{msg.author.mention} 在 {msg.guild} 的 {msg.channel.mention} 輸入 {msg.content}")
                pic = discord.File(jdata['確實'])
                await msg.channel.send(file=pic)

            if msg.content == ("不知道"): #and msg.author != self.bot.user: #前者->關鍵字、後者->要是非機器人傳送的
                print ("不知道")
                channel = self.bot.get_channel(int(jdata["後台"]))
                await channel.send(f"{msg.author.mention} 在 {msg.guild} 的 {msg.channel.mention} 輸入 {msg.content}")
                pic = discord.File(jdata['不知道'])
                await msg.channel.send(file=pic)

            if msg.content == ("你犯法"): #前者->關鍵字、後者->要是非機器人傳送的
                print ("犯法")
                channel = self.bot.get_channel(int(jdata["後台"]))
                await channel.send(f"{msg.author.mention} 在 {msg.guild} 的 {msg.channel.mention} 輸入 {msg.content}")
                pic = discord.File(jdata['犯法'])
                await msg.channel.send(file=pic)
                await msg.channel.send("不知道")

            if msg.content == ("我沒錢"): #前者->關鍵字、後者->要是非機器人傳送的
                print ("我沒錢")
                channel = self.bot.get_channel(int(jdata["後台"]))
                await channel.send(f"{msg.author.mention} 在 {msg.guild} 的 {msg.channel.mention} 輸入 {msg.content}")
                pic = discord.File(jdata['沒錢'])
                await msg.channel.send(file=pic)

            if msg.content == ("氣死"): #前者->關鍵字、後者->要是非機器人傳送的
                print ("氣死")
                channel = self.bot.get_channel(int(jdata["後台"]))
                await channel.send(f"{msg.author.mention} 在 {msg.guild} 的 {msg.channel.mention} 輸入 {msg.content}")
                pic = discord.File(jdata['氣死'])
                await msg.channel.send("起司??")
                await msg.channel.send(file=pic)

            if msg.content == ("你有強迫症"): #前者->關鍵字、後者->要是非機器人傳送的
                print ("強迫症")
                channel = self.bot.get_channel(int(jdata["後台"]))
                await channel.send(f"{msg.author.mention} 在 {msg.guild} 的 {msg.channel.mention} 輸入 {msg.content}")
                pic = discord.File(jdata['強迫症'])
                await msg.channel.send(file=pic)

            if msg.content == ("TNT拿來"): #前者->關鍵字、後者->要是非機器人傳送的
                print ("TNT")
                channel = self.bot.get_channel(int(jdata["後台"]))
                await channel.send(f"{msg.author.mention} 在 {msg.guild} 的 {msg.channel.mention} 輸入 {msg.content}")
                pic = discord.File(jdata['TNT'])
                await msg.channel.send(file=pic)
            
            if msg.content == ("NoTag"): #前者->關鍵字、後者->要是非機器人傳送的
                print ("NoTag")
                channel = self.bot.get_channel(int(jdata["後台"]))
                await channel.send(f"{msg.author.mention} 在 {msg.guild} 的 {msg.channel.mention} 輸入 {msg.content}")
                pic = discord.File(jdata['NoTag'])
                await msg.channel.send(file=pic)

            if msg.content == ("好問題"): #前者->關鍵字、後者->要是非機器人傳送的
                print ("好問題")
                channel = self.bot.get_channel(int(jdata["後台"]))
                await channel.send(f"{msg.author.mention} 在 {msg.guild} 的 {msg.channel.mention} 輸入 {msg.content}")
                pic = discord.File(jdata['好問題'])
                await msg.channel.send(file=pic)

            if msg.content == ("XD") or msg.content ==("xd"): #前者->關鍵字、後者->要是非機器人傳送的
                print ("XD")
                channel = self.bot.get_channel(int(jdata["後台"]))
                await channel.send(f"{msg.author.mention} 在 {msg.guild} 的 {msg.channel.mention} 輸入 {msg.content}")
                pic = discord.File(jdata['XD'])
                await msg.channel.send(file=pic)

            if msg.content == ("R.I.P."): #前者->關鍵字、後者->要是非機器人傳送的
                print ("R.I.P.")
                channel = self.bot.get_channel(int(jdata["後台"]))
                await channel.send(f"{msg.author.mention} 在 {msg.guild} 的 {msg.channel.mention} 輸入 {msg.content}")
                pic = discord.File(jdata['simon'])
                await msg.channel.send(file=pic)
                await msg.channel.send("好可惜，他死了")
            
            if msg.content == ("gay"): #前者->關鍵字、後者->要是非機器人傳送的
                print (msg.content)
                channel = self.bot.get_channel(int(jdata["後台"]))
                await channel.send(f"{msg.author.mention} 在 {msg.guild} 的 {msg.channel.mention} 輸入 {msg.content}")
                pic = discord.File(jdata['gay-1'])
                await msg.channel.send(file=pic)
                pic1 = discord.File(jdata['gay-2'])
                await msg.channel.send(file=pic1)
                pic2 = discord.File(jdata['gay-3'])
                await msg.channel.send(file=pic2)
            
            if msg.content == ("我來負責"): #前者->關鍵字、後者->要是非機器人傳送的
                print (msg.content)
                channel = self.bot.get_channel(int(jdata["後台"]))
                await channel.send(f"{msg.author.mention} 在 {msg.guild} 的 {msg.channel.mention} 輸入 {msg.content}")
                pic = discord.File(jdata['負責'])
                await msg.channel.send(file=pic)

            if msg.content == ("你在偷看"): #前者->關鍵字、後者->要是非機器人傳送的
                print (msg.content)
                channel = self.bot.get_channel(int(jdata["後台"]))
                await channel.send(f"{msg.author.mention} 在 {msg.guild} 的 {msg.channel.mention} 輸入 {msg.content}")
                pic = discord.File(jdata['偷看'])
                await msg.channel.send(file=pic)
            
            if msg.content == ("可以色色"): #前者->關鍵字、後者->要是非機器人傳送的
                print (msg.content)
                channel = self.bot.get_channel(int(jdata["後台"]))
                await channel.send(f"{msg.author.mention} 在 {msg.guild} 的 {msg.channel.mention} 輸入 {msg.content}")
                pic = discord.File(jdata['可以色色'])
                await msg.channel.send(file=pic)

            if msg.content == ("ㄍㄢˋ"): #前者->關鍵字、後者->要是非機器人傳送的
                print (msg.content)
                channel = self.bot.get_channel(int(jdata["後台"]))
                await channel.send(f"{msg.author.mention} 在 {msg.guild} 的 {msg.channel.mention} 輸入 {msg.content}")
                pic = discord.File(jdata['幹'])
                await msg.channel.send(file=pic)
            
            if msg.content == ("打"): #前者->關鍵字、後者->要是非機器人傳送的
                print (msg.content)
                channel = self.bot.get_channel(int(jdata["後台"]))
                await channel.send(f"{msg.author.mention} 在 {msg.guild} 的 {msg.channel.mention} 輸入 {msg.content}")
                pic = discord.File(jdata['打木頭'])
                await msg.channel.send(file=pic)

            if msg.content == ("我愛貓月"): #前者->關鍵字、後者->要是非機器人傳送的
                print (msg.content)
                channel = self.bot.get_channel(int(jdata["後台"]))
                await channel.send(f"{msg.author.mention} 在 {msg.guild} 的 {msg.channel.mention} 輸入 {msg.content}")
                pic = discord.File(jdata['愛貓月'])
                await msg.channel.send(file=pic)

            if msg.content == ("孤兒"): #前者->關鍵字、後者->要是非機器人傳送的
                print (msg.content)
                channel = self.bot.get_channel(int(jdata["後台"]))
                await channel.send(f"{msg.author.mention} 在 {msg.guild} 的 {msg.channel.mention} 輸入 {msg.content}")
                pic = discord.File(jdata['孤兒院'])
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