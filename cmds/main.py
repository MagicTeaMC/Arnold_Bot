import discord
from discord.ext import commands
from core.classes import Cog_Extension
import datetime
import json
import random
import asyncio
#from discord_ui import InputText, Modal

with open("Setting.json","r",encoding='utf8') as jFile:
    jdata = json.load(jFile)


class Main(Cog_Extension):

    @commands.command(help="顯示延遲", brief="顯示延遲")
    async def ping(self,ctx): 
        #ctx (上下文，回覆的上下關係) 
        #A：嗨(上文)(使用者，ID，伺服器，頻道)
        #B：安安(下文)
        await ctx.send(f'{round(self.bot.latency*1000)}(ms)') #預設單位為秒
        channel = self.bot.get_channel(int(jdata["後台"]))
        await channel.send(f"{ctx.author.mention}在{ctx.guild}的{ctx.channel.mention}查詢ping")

    @commands.command(help="顯示功能說明(基本沒用)", brief="顯示功能(不完整)")
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
        channel = self.bot.get_channel(int(jdata["後台"]))
        await channel.send(f'{ctx.author.mention} 在 {ctx.guild} 的 {ctx.channel.mention} 召喚了功能說明!')

    @commands.command(help="顯示會回覆的字詞清單", brief="顯示會回覆的字詞清單")
    async def 回覆(self,ctx):
        #崁入功能-> https://cog-creators.github.io/discord-embed-sandbox/
        embed=discord.Embed(title="回覆", color=0x2fe7f4,
        timestamp=datetime.datetime.now())
        embed.set_author(name="本機器人由3.14159265358#6111創建")
        embed.add_field(name="apple", value="", inline=True)
        embed.add_field(name="早安", value="", inline=True)
        embed.add_field(name="午安", value="", inline=True)
        embed.add_field(name="晚安", value="", inline=True)
        embed.add_field(name="你好", value="", inline=True)
        embed.add_field(name="確實", value="", inline=True)
        embed.add_field(name="不知道", value="", inline=True)
        embed.add_field(name="你犯法", value="", inline=True)
        embed.add_field(name="我沒錢", value="", inline=True)
        embed.add_field(name="你有強迫症", value="", inline=True)
        embed.add_field(name="TNT拿來", value="", inline=True)
        embed.add_field(name="氣死", value="", inline=False)
        embed.add_field(name="NoTag", value="", inline=False)
        embed.add_field(name="好問題", value="", inline=False)
        embed.add_field(name="XD、xd", value="", inline=False)
        embed.add_field(name="R.I.P.", value="", inline=False)
        embed.add_field(name="gay", value="", inline=False)
        embed.add_field(name="我來負責", value="", inline=False)
        embed.add_field(name="你在偷看", value="", inline=False)
        embed.add_field(name="可以色色", value="", inline=False)
        embed.add_field(name="ㄍㄢˋ", value="", inline=False)
        embed.add_field(name="打", value="", inline=False)
        embed.add_field(name="我愛貓月", value="", inline=False)
        embed.add_field(name="孤兒", value="", inline=False)
        await ctx.send(embed=embed)
        print("有人召喚了回覆說明")
        channel = self.bot.get_channel(int(jdata["後台"]))
        await channel.send(f'{ctx.author.mention} 在 {ctx.guild} 的 {ctx.channel.mention} 召喚了回覆說明!')

    @commands.command(help="讓機器人說話，用法 $say [內文]，例如： $say Hi您好我叫Arnold_Bot", brief="讓(逼)機器人說話")
    async def say(self,ctx,*,msg):
            #使用機器人講話
        #刪訊息
        await ctx.message.delete()
        #複誦
        await ctx.send(msg)
        print("被逼說：",msg)
        channel = self.bot.get_channel(int(jdata["後台"]))
        await channel.send(f'{ctx.author.mention} 在 {ctx.guild} 的 {ctx.channel.mention} 逼我說 {msg} !')
    

    @commands.command(help="批量清除訊息，用法： $clean [數量]，例如： $clean 10", brief="批量刪除訊息")
    async def clean(self,ctx,num:int,reason1):
        await ctx.channel.purge(limit=num+1,reason=reason1)
        print("清理了",num,"則訊息,因為",reason1)
        channel = self.bot.get_channel(int(jdata["後台"]))
        await channel.send(f'{ctx.author.mention} 在 {ctx.guild} 的 {ctx.channel.mention} 清除了 {num} 則訊息，因為 {reason1} !')

    @commands.command()
    async def random(self,ctx):
        online = []
        for member in ctx.guild.members:
            if str(member.status) == 'online':
                online.append(member)

        random_online = []
        for x in random.sample(online,k=5):
            await ctx.send(x)

    @commands.command(help="顯示伺服器資訊", brief="顯示伺服器資訊")
    async def server(self,ctx):
        now_time = ctx.guild.created_at
        embed=discord.Embed(title="伺服器資訊", color=0x47f0b8,
        timestamp=datetime.datetime.now())
        embed.add_field(name="🟢名稱", value=ctx.guild.name, inline=True)
        embed.add_field(name="🆔伺服器ID", value =ctx.guild.id, inline = True)
        embed.add_field(name="👑擁有者", value=ctx.guild.owner.mention, inline=True)
        embed.add_field(name="📆創建時間", value=now_time.strftime("%m/%d/%Y, %H:%M:%S"), inline=True)
        embed.add_field(name="🌐描述", value=ctx.guild.description, inline=True)
        embed.add_field(name="👥成員數", value=ctx.guild.member_count, inline=True)
        embed.add_field(name="💬頻道", value = f'{len(ctx.guild.text_channels)} 個文字頻道 | {len(ctx.guild.voice_channels)} 個語音頻道', inline = True)
        embed.add_field(name="📚規則頻道", value=ctx.guild.rules_channel.mention, inline=True)
        async with ctx.typing():
            await asyncio.sleep(2)
        await ctx.send(embed=embed)
        channel = self.bot.get_channel(int(jdata["後台"]))
        await channel.send(f"{ctx.author.mention}在{ctx.guild}的{ctx.channel.mention}查詢該伺服器資訊")

    @commands.command(help="顯示個人資訊，用法：$userinfo @someone", brief="顯示特定使用者資訊資訊")
    async def userinfo(self,ctx,member:discord.Member):
        create_time = member.created_at
        join_time = member.joined_at
        embed=discord.Embed(title="ℹ️使用者資訊",description=member.mention,color=0x00ffee)
        embed.add_field(name="🐬名稱", value=member, inline=True)
        embed.add_field(name="🆔ID", value=member.id, inline=True)
        if str(member.display_name) == str(member.name):
            embed.add_field(name="🖌️暱稱", value="未修改", inline=True)
        else:
            embed.add_field(name="暱稱", value=member.display_name, inline=True)
        if str(member.status) == "online":
            embed.add_field(name="💡上線狀態", value="🟢線上", inline=True)
        elif str(member.status) == "dnd":
            embed.add_field(name="💡上線狀態", value="⛔勿擾", inline=True)
        elif str(member.status) == "idle":
            embed.add_field(name="💡上線狀態", value="🌛閒置", inline=True)
        else:
            embed.add_field(name="💡上線狀態", value="⚫隱形或離線", inline=True)
        embed.add_field(name="✡️帳號創建時間", value=create_time.strftime("%m/%d/%Y, %H:%M:%S"), inline=True)
        embed.add_field(name="➡️加入時間", value=join_time.strftime("%m/%d/%Y, %H:%M:%S"), inline=True)
        if member.timed_out_until == None:
            embed.add_field(name="🈲禁言時間", value="❌無禁言狀態", inline=True)
        else:
            timeout_time = member.timed_out_until
            embed.add_field(name="🈲禁言時間", value=timeout_time.strftime("%m/%d/%Y, %H:%M:%S"), inline=True)
        if member.bot:
            embed.add_field(name="🤖機器人", value="✅是", inline=True)
        else:
            embed.add_field(name="🤖機器人", value="❌否", inline=True)
        embed.set_footer(text=f"查詢者{ctx.author.mention}")
        await ctx.send(embed=embed)
        roles = " ".join([role.mention for role in member.roles if role.name != "@everyone"])
        embed.add_field(name="👥身分", value=f"{roles}", inline=False)
        channel = self.bot.get_channel(int(jdata["後台"]))
        await channel.send(f"{ctx.author.mention}在{ctx.guild}的{ctx.channel.mention}查詢{member.mention}的資訊")


    @commands.command(help="顯示伺服器身分組資訊", brief="顯示身分組資訊")
    async def roles(self,ctx):
        embed=discord.Embed(title="身分組一覽", color=0xc13de6)
        roles = ",".join([role.mention for role in ctx.guild.roles])
        roles_list = roles.split(",")
        roles_list.reverse()
        roles_list_reverse = "\n".join(roles_list)
        embed.add_field(name="身分", value=roles_list_reverse, inline=False)
        await ctx.send(embed=embed)
        channel = self.bot.get_channel(int(jdata["後台"]))
        await channel.send(f"{ctx.author.mention}在{ctx.guild}的{ctx.channel.mention}查詢伺服器身分組資訊")

    @commands.command(help="顯示身分組資訊，用法： $role [身分組ID]", brief="顯示身分組資訊")
    async def role(self,ctx,ID:int):
        guild = self.bot.get_guild(ctx.guild.id)
        role = guild.get_role(ID)
        create_time = role.created_at
        embed=discord.Embed(title="身分組資訊", description=role.mention, color=0xc13de6)
        embed.add_field(name="創建時間", value=create_time.strftime("%m/%d/%Y, %H:%M:%S"), inline=True)
        embed.add_field(name="ID", value=role.id, inline=True)
        embed.add_field(name="成員數", value=len(role.members), inline=True)
        if role.permissions.administrator:
            embed.add_field(name="管理權", value="✅是", inline=True)
        else:
            embed.add_field(name="管理權", value="❌否", inline=True)
        if role.permissions.mention_everyone:
            embed.add_field(name="Tag_everyone", value="✅是", inline=True)
        else:
            embed.add_field(name="Tag_everyone", value="❌否", inline=True)
        if role.permissions.ban_members:
            embed.add_field(name="Ban", value="✅是", inline=True)
        else:
            embed.add_field(name="Ban", value="❌否", inline=True)
        if role.permissions.kick_members:
            embed.add_field(name="Kick", value="✅是", inline=True)
        else:
            embed.add_field(name="Kick", value="❌否", inline=True)
        await ctx.send(embed=embed)
        channel = self.bot.get_channel(int(jdata["後台"]))
        await channel.send(f"{ctx.author.mention}在{ctx.guild}的{ctx.channel.mention}查詢 {role.mention} 的資訊")

    @commands.command(help="顯示身分組成員，用法： $rolemember [身分組ID]", brief="顯示身分組成員")
    async def rolemember(self,ctx,ID:int):
        guild = self.bot.get_guild(ctx.guild.id)
        role = guild.get_role(ID)
        roles = ",".join([member.mention for member in role.members])
        embed=discord.Embed(title="身分組成員", description="role.mention", color=0x3d9de6)
        embed.add_field(name="成員名單", value=roles, inline=True)
        await ctx.send(embed=embed)




#group群組
#subcommand 子命令
    @commands.group()
    async def codetest(self,ctx):
        await ctx.send("Group")

    @codetest.command()
    async def python(self,ctx):
        await ctx.send("python")


async def setup(bot):
    await bot.add_cog(Main(bot))