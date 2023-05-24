import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import random
import asyncio
import datetime
import time

with open("Setting.json","r",encoding='utf8') as jFile:
    jdata = json.load(jFile)

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self,member):
        #成員加入
        channels = {1061070549566103622:1108387516836479126,1078082303256969317:1078082303294705712}
        #1.星落 2.鷹之國
        if member.guild.id in channels:
            channel_id = channels[member.guild.id]
            channel = self.bot.get_channel(channel_id)
            if member.guild.id == 1078082303256969317:
                join = 1078082303294705714
                await channel.send(f'{member.mention} 加入 {member.guild} ，請至 <#{join}> 輸入 「加入公會」 以得知加入方案! 目前成員數：{len(member.guild.members)}')
                role_ids = [1094181672708214824, 1094031097517580308, 1094030992311853117, 1094031438418022460]
                for role_id in role_ids:
                    role = discord.utils.get(member.guild.roles, id=role_id)
                    await member.add_roles(role)
            else:
                await channel.send(f'歡迎{member.mention} 加入 {member.guild} 目前成員數：{len(member.guild.members)}!!')
        else:
            channel = self.bot.get_channel(int(jdata["後台"]))
            await channel.send(f'{member.mention} 加入 {member.guild} ! 該伺服器目前成員數：{len(member.guild.members)}')
          
    @commands.Cog.listener()
    async def on_member_remove(self,member):
        #成員離開
        channels = {1061070549566103622:1108387516836479126,1078082303256969317:1078082303294705712}
        #1.星落 2.鷹之國
        if member.guild.id in channels:
            channel_id = channels[member.guild.id]
            channel = self.bot.get_channel(channel_id)
            await channel.send(f'{member.mention} 離開 {member.guild} 目前成員數：{len(member.guild.members)}!!')
        else:
            channel = self.bot.get_channel(int(jdata["後台"]))
            await channel.send(f'{member.mention} 離開 {member.guild} ! 該伺服器剩於成員數：{len(member.guild.members)}')

    @commands.Cog.listener()
    async def on_member_ban(self,guild,member):
        #成員離開
        channels = {1061070549566103622:1108387516836479126,1078082303256969317:1078082303294705712}
        #1.星落 2.鷹之國
        if member.guild.id in channels:
            channel_id = channels[member.guild.id]
            channel = self.bot.get_channel(channel_id)
            await channel.send(f'{member.mention} 被 {member.guild} 停權了!目前成員數：{len(member.guild.members)}!!')
        else:
            channel = self.bot.get_channel(int(jdata["後台"]))
            await channel.send(f'{member.mention} 被 {member.guild} 停權了! 該伺服器剩於成員數：{len(member.guild.members)}')
            
    @commands.Cog.listener()
    async def on_member_unban(self,guild,member):
        #成員離開
        channels = {1061070549566103622:1108387516836479126,1078082303256969317:1078082303294705712}
        #1.星落 2.鷹之國
        if member.guild.id in channels:
            channel_id = channels[member.guild.id]
            channel = self.bot.get_channel(channel_id)
            await channel.send(f'{member.mention} 被 {member.guild} 解除停權了!')
        else:
            channel = self.bot.get_channel(int(jdata["後台"]))
            await channel.send(f'{member.mention} 被 {member.guild} 解除停權了! 該伺服器剩於成員數：{len(member.guild.members)}')
            
    @commands.Cog.listener()
    async def on_raw_reaction_add(self,data):
        #1.新增反應 --> data
        channel = self.bot.get_channel(int(jdata["後台"]))
        guild = self.bot.get_guild(data.guild_id)
        print(data.member,guild,data.emoji)
        if str(data.emoji) == '💀' and str(data.message_id) == str(1086515736723337237) and str(data.guild_id) == str(1078082303256969317): #2.確認圖案
            print('輸入💀')
            role = guild.get_role(1078082303256969318)
            await channel.send(f"{data.member.mention} 輸入 {data.emoji}")

            #3.給予身分
            await data.member.add_roles(role,reason="新增反映後台身分")
            await data.member.send(f"你取得了 {role} 這個身分組!")

        if str(data.emoji) == '🔹' and str(data.message_id) == str(1086515736723337237) and str(data.guild_id) == str(1078082303256969317): #2.確認圖案
            print('輸入🔹')
            role = guild.get_role(1078082303256969320)
            await channel.send(f"{data.member.mention} 輸入 {data.emoji}")
            #3.給予身分
            await data.member.add_roles(role,reason="新增反映原神身分")
            await data.member.send(f"你取得了 {role} 這個身分組!")

        if str(data.emoji) == '🈲' and str(data.message_id) == str(1086515736723337237) and str(data.guild_id) == str(1078082303256969317): #2.確認圖案
            print('輸入 🈲')
            role = guild.get_role(1078082303256969319)
            await channel.send(f"{data.member.mention} 輸入 {data.emoji}")
            #3.給予身分
            await data.member.add_roles(role,reason="新增反映18+身分")
            await data.member.send(f"你取得了 {role} 這個身分組!")
        if str(data.emoji) == '🇨' and str(data.message_id) == str(1086515736723337237) and str(data.guild_id) == str(1078082303256969317): 
            print('輸入 🇨')
            role = guild.get_role(1093223889234051173)
            await channel.send(f"{data.member.mention} 輸入 {data.emoji}")
            #3.給予身分
            await data.member.add_roles(role,reason="新增反映ChatGPT身分")
            await data.member.send(f"你取得了 {role} 這個身分組!")

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self,data):
        #1.新增反應 --> data
        channel = self.bot.get_channel(int(jdata["後台"]))
        guild = self.bot.get_guild(data.guild_id)
        user = guild.get_member(data.user_id)
        print(f'移除{data.member},{guild},{data.emoji}')
        if str(data.emoji) == '💀' and str(data.message_id) == str(1086515736723337237) and str(data.guild_id) == str(1078082303256969317): #2.確認圖案
            print('移除💀')
            role = guild.get_role(1078082303256969318)
            #3.給予身分
            await channel.send(f"{user.mention} 移除 {data.emoji}")
            await user.remove_roles(role,reason="移除反映後台身分")
            await user.send(f"你移除了 {role} 這個身分組!")

        if str(data.emoji) == '🔹' and str(data.message_id) == str(1086515736723337237) and str(data.guild_id) == str(1078082303256969317): #2.確認圖案
            print('移除🔹')
            role = guild.get_role(1078082303256969320)
            #3.給予身分
            await channel.send(f"{user.mention} 移除 {data.emoji}")
            await user.remove_roles(role,reason="移除反映原神身分")
            await user.send(f"你移除了 {role} 這個身分組!")

        if str(data.emoji) == '🈲' and str(data.message_id) == str(1086515736723337237) and str(data.guild_id) == str(1078082303256969317): #2.確認圖案
            print('移除🈲')
            role = guild.get_role(1078082303256969319)
            #3.給予身分
            await channel.send(f"{user.mention} 移除 {data.emoji}")
            await user.remove_roles(role,reason="移除反映18+身分")
            await user.send(f"你移除了 {role} 這個身分組!")
        if str(data.emoji) == '🇨' and str(data.message_id) == str(1086515736723337237) and str(data.guild_id) == str(1078082303256969317): 
            print('🇨')
            role = guild.get_role(1093223889234051173)
            #3.給予身分
            await channel.send(f"{user.mention} 移除 {data.emoji}")
            await user.remove_roles(role,reason="移除反映ChatGPT身分")
            await user.send(f"你移除了 {role} 這個身分組!")

    @commands.Cog.listener()
    async def on_raw_message_delete(self,msg):
        if msg.guild_id == int(1061070549566103622):
            channel_d = self.bot.get_channel(msg.channel_id)
            self.channel = self.bot.get_channel(1095943588694736907)
            embed=discord.Embed(title="訊息刪除", color=0xff5c5c,
            timestamp=datetime.datetime.now())
            embed.add_field(name="原訊息", value=msg.cached_message.content, inline=False)
            embed.add_field(name="原作者", value=msg.cached_message.author.mention, inline=True)
            embed.add_field(name="頻道", value=channel_d.mention, inline=True)
            await self.channel.send(embed=embed)
            
    @commands.Cog.listener()
    async def on_raw_message_edit(self,msg):
        if msg.guild_id == int(1061070549566103622):
            channel_e = self.bot.get_channel(msg.channel_id)
            self.channel = self.bot.get_channel(1095943588694736907)
            message = await channel_e.fetch_message(msg.message_id)
            embed=discord.Embed(title="訊息編輯", color=0x63f8ab,
            timestamp=datetime.datetime.now())
            embed.add_field(name="編輯前的訊息", value=msg.cached_message.content, inline=False)
            embed.add_field(name="編輯後的訊息", value=message.content, inline=False)
            embed.add_field(name="原作者", value=msg.cached_message.author.mention, inline=True)
            embed.add_field(name="頻道", value=channel_e.mention, inline=True)
            embed.add_field(name="訊息連結", value=message.jump_url, inline=True)
            await self.channel.send(embed=embed)
    
    #'''
    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        tag = 877103068498522143
        if isinstance(error,commands.errors.MissingRequiredAttachment):
            await ctx.send("遺失參數，如右問題請至：https://discord.gg/NdqxvRgGyf 詢問(需領取身分)")
            channel = self.bot.get_channel(int(jdata["錯誤"]))
            await channel.send(f'{ctx.author.mention} 在 {ctx.guild} 的 {ctx.channel.mention} 發生"遺失參數"的錯誤! 運行指令：{ctx.message.content} ，錯誤：{error}')
            channel = self.bot.get_channel(int(jdata["Maoyue錯誤"]))
            await channel.send(f'{ctx.author} 在 {ctx.guild} 的 {ctx.channel.mention} 發生"遺失參數"的錯誤! 運行指令：{ctx.message.content} ，錯誤：{error}')
        elif isinstance(error,commands.errors.CommandNotFound):
            await ctx.send("指令不存在")
            channel = self.bot.get_channel(int(jdata["錯誤"]))
            await channel.send(f'{ctx.author.mention} 在 {ctx.guild} 的 {ctx.channel.mention} 發生"指令不存在"的錯誤! 運行指令：{ctx.message.content}，錯誤：{error}')
            channel = self.bot.get_channel(int(jdata["Maoyue錯誤"]))
            await channel.send(f'{ctx.author} 在 {ctx.guild} 的 {ctx.channel.mention} 發生"指令不存在"的錯誤! 運行指令：{ctx.message.content} ，錯誤：{error}')
        else:
            await ctx.send("發生錯誤，請向製作者回報(https://discord.gg/NdqxvRgGyf 需領取身分)")
            channel = self.bot.get_channel(int(jdata["錯誤"]))
            await channel.send(f'{ctx.author.mention} 在 {ctx.guild} 的 {ctx.channel.mention} 發生錯誤! 運行指令：{ctx.message.content}，錯誤：{error}')
            channel = self.bot.get_channel(int(jdata["Maoyue錯誤"]))
            await channel.send(f'<@{tag}>來解決!  {ctx.author} 在 {ctx.guild} 的 {ctx.channel.mention} 發生錯誤! 運行指令：{ctx.message.content}，錯誤：{error}')

    #'''
    
    @commands.Cog.listener()
    async def on_guild_join(self,guild):
        create_time = guild.created_at
        now_time = time.mktime(create_time.timetuple())
        embed=discord.Embed(title="機器人加入!!", color=0x47f0b8,
        timestamp=datetime.datetime.now())
        embed.add_field(name="🟢名稱", value=guild.name, inline=True)
        embed.add_field(name="🆔伺服器ID", value =guild.id, inline = True)
        embed.add_field(name="👑擁有者", value=guild.owner.mention, inline=True)
        embed.add_field(name="📆創建時間", value=f"<t:{int(now_time)}>", inline=True)
        embed.add_field(name="👥成員數", value=guild.member_count, inline=True)
        embed.add_field(name="🛂服務群組數", value=len(self.bot.guilds), inline=True)
        role_ch = guild.rules_channel
        invite = await role_ch.create_invite()
        embed.add_field(name="該群組邀請連結", value=(invite), inline=True)
        
        channel = self.bot.get_channel(int(jdata["Maoyue後台"]))
        await channel.send(embed=embed)
        await channel.send(invite)
        channel = self.bot.get_channel(int(jdata["機器人加入"]))
        await channel.send(embed=embed)
        await channel.send(invite)
        
    @commands.Cog.listener()
    async def on_guild_remove(self,guild):
        create_time = guild.created_at
        now_time = time.mktime(create_time.timetuple())
        embed=discord.Embed(title="機器人離開!!", color=0x47f0b8,
        timestamp=datetime.datetime.now())
        embed.add_field(name="🟢名稱", value=guild.name, inline=True)
        embed.add_field(name="🆔伺服器ID", value =guild.id, inline = True)
        embed.add_field(name="👑擁有者", value=guild.owner.mention, inline=True)
        embed.add_field(name="📆創建時間", value=f"<t:{int(now_time)}>", inline=True)
        embed.add_field(name="👥成員數", value=guild.member_count, inline=True)
        embed.add_field(name="🛂服務群組數", value=len(self.bot.guilds), inline=True)
        channel = self.bot.get_channel(int(jdata["Maoyue後台"]))
        await channel.send(embed=embed)
        channel = self.bot.get_channel(int(jdata["機器人加入"]))
        await channel.send(embed=embed)
        
    #'''
    @commands.Cog.listener()
    async def on_member_update(self,before, after):
        if before.premium_since is None and after.premium_since is not None:
            if  str(after.guild.id) == str(1061070549566103622):
                role_id = 1099669431136829502
                channel = self.bot.get_channel(1084439377696014398)
                embed=discord.Embed(title="<a:heart:1085403808181526558>感謝加成伺服器<a:heart:1085403808181526558>")
                embed.add_field(name="<a:emoji_1:1085403330152509520>加成成員", value={after.mention}, inline=False)
                embed.add_field(name=f"{after.guild} 全體職員感謝您的加成", value=f"已給予 <@&{role_id}> 身分", inline=False)
                await channel.send(embed=embed)
    #'''
            

    @commands.Cog.listener()
    async def on_message(self,msg):
        #on_message必須寫在一個def裡
        guildlist = []
        if msg.channel.id == int(1078082303294705714)and msg.author != self.bot.user:
            if msg.content == ("加入"):
                await msg.channel.send(f"> 如果您要加入公會，請輸入\n1.Minecraft的ID：\n2.有加入的其他公會：\n並用「，」分隔\n例如：`ChenArnold，鷹之國、蘋果村`\n備註：填錯格式沒加入不要來找我(沒用逗點分隔)\n\n> 只是想聊天請打「我只是來聊天」")
            elif msg.content == ("我只是來聊天"):
                guild = self.bot.get_guild(msg.guild.id)
                role = guild.get_role(1086798962180235296)
                await msg.author.add_roles(role,reason="填寫資料加入聊天")
                await msg.add_reaction("✅")
                await msg.author.send(f"你加入了鷹之國公會(聊天)")
                channel = self.bot.get_channel(int(jdata["後台"]))
                await channel.send(str(msg.author.mention)+"加入鷹之國(聊天)")
                print(str(msg.author)+"加入鷹之國(聊天)")
                
            else:
                try:
                    guildlist = msg.content.split("，")
                    embed=discord.Embed(title="加入公會", color=0x2febf9,
                    timestamp=datetime.datetime.now())
                    embed.add_field(name="Minecraft ID", value=guildlist[0], inline=True)
                    embed.add_field(name="Discord ID", value=msg.author, inline=True)
                    embed.add_field(name="加入的其他公會", value=guildlist[1], inline=False)
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
                    await msg.author.send(f"歡迎加入鷹之國公會，記得去看規定，犯錯不要來怪別人喔 <#{rule_channel}>，如您的MinecraftID在奶茶伺服器找不到，將會撤銷您的身分")
                    #await msg.channel.send("輸入成功，已給予身分")
                    await msg.author.edit(nick=f'[成員]{guildlist[0]}')
                    channel = self.bot.get_channel(int(jdata["後台"]))
                    await channel.send(str(msg.author.mention)+"加入鷹之國")
                    print(str(msg.author)+"加入鷹之國")
        else:
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
                await msg.channel.send("好可惜，他死了||，請上三柱香||")
            
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