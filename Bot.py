import discord
from discord.ext import commands
from discord import app_commands
import json
import random
import os
import asyncio
import datetime
#from discord_slash import cog_ext, SlashContext
#os.chdir("C:\\Users\\user\\OneDrive\\文件\\GitHub\\Arnold_Bot")

with open("Setting.json","r",encoding='utf8') as jFile:
    jdata = json.load(jFile)


intents = discord.Intents.all()
intents.members = True
    #1.5後的權限設置

bot = commands.Bot(command_prefix='$',intents=intents)
    #機器人符號(指令前的符號)
#bot.slash = cog_ext.SlashCommandBot(bot)

activities = [
    discord.Game(name="星落伺服器"),
    discord.Game(name="Minecraft"),
    discord.Activity(type=discord.ActivityType.listening, name="貓月講故事"),
    discord.Activity(type=discord.ActivityType.watching, name="小諾愛貓月"),
]

@bot.event
async def on_ready():
    with open("Setting.json","r",encoding='utf8') as jFile:
        jdata = json.load(jFile)
    print(f"-------->>機器人已上線<<--------\n 目前登入：{bot.user}。目前服務群組數：{len(bot.guilds)}。目前服務人數：{len(bot.users)} \n {datetime.datetime.now().hour}:{datetime.datetime.now().minute}")
    for filename in os.listdir('./cmds'):
        if filename.endswith('.py'):
            try:
                await bot.load_extension(f'cmds.{filename[:-3]}')
                print(f'✅   已加載 {filename}')
            except Exception as error:
                print(f'❎   {filename} 發生錯誤  {error}')
    try:
        synced = await bot.tree.sync()
        print(f"{len(synced)}個斜線命令")
    except Exception as e:
        print(e)
    await bot.change_presence(activity = discord.Activity(type=discord.ActivityType.listening, name="貓月說故事"))
    channel = bot.get_channel(int(jdata["start"]))
    await channel.send(f"✅   機器人開始運行   ✅ \n 目前登入：{bot.user}。目前服務群組數：{len(bot.guilds)}。目前服務人數：{len(bot.users)}。{len(synced)}個斜線命令")
    channel = bot.get_channel(int(jdata["Maoyue_start"]))
    await channel.send(f"✅   機器人開始運行   ✅ \n 目前登入：{bot.user}。目前服務群組數：{len(bot.guilds)}。目前服務人數：{len(bot.users)}。{len(synced)}個斜線命令")

    
    while True:
        if (datetime.datetime.now().hour== 12 & datetime.datetime.now().minute== 13):
            print("提醒")
            #channel = bot.get_channel(1081530379212685383)
            #await channel.send("測試一下下就好")
            #await bot.change_presence(activity=random.choice(activities))
        await asyncio.sleep(60) 
    
        
@bot.tree.command(name="hello")
async def hello(ctx):
    await ctx.response.send_message(f"嗨~你好{ctx.user.mention}",ephemeral = True)
    
@bot.tree.command(name="say")
@app_commands.describe(thing_to_say = "What should I say?")
async def say(interaction: discord. Interaction, thing_to_say: str):
    await interaction.response.send_message(f"{interaction.user.name} said:{thing_to_say}")

@bot.tree.command(name="load")
@app_commands.describe(extension = "要載入的文件")
async def load(ctx:discord. Interaction,extension:str):
    await bot.load_extension(f'cmds.{extension}')
    await ctx.response.send_message(f'已載入{extension}!')
    print(f"已載入{extension}!")
    channel = bot.get_channel(int(jdata["後台"]))
    await channel.send(f"{ctx.author} 載入 {extension}")

@bot.tree.command(name="unload")
@app_commands.describe(extension = "要卸載的文件")
async def unload(ctx:discord. Interaction,extension:str):
    await bot.unload_extension(f'cmds.{extension}')
    await ctx.response.send_message(f'已卸載{extension}!')
    print(f'已卸載{extension}!')
    channel = bot.get_channel(int(jdata["後台"]))
    await channel.send(f"{ctx.author} 卸載 {extension}")

@bot.tree.command(name="reload")
@app_commands.describe(extension = "要重載的文件")
async def reload(ctx:discord. Interaction,extension:str):
    await bot.reload_extension(f'cmds.{extension}')
    await ctx.response.send_message(f'已重新載入{extension}!')
    print(f'已重新載入{extension}!')
    channel = bot.get_channel(int(jdata["後台"]))
    await channel.send(f"{ctx.author} 重新載入 {extension}")
    
async def load_extensions(): 
    for filename in os.listdir("./cmds"):
        if filename.endswith(".py"):
            await bot.load_extension(f'cmds.{filename[:-3]}')
           

if __name__ == "__main__":
    bot.run(jdata["TOKEN"])