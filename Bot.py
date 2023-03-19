import discord
from discord.ext import commands
import json
import random
import os
import asyncio
import datetime





os.chdir("C:\\Users\\user\\OneDrive\\文件\\GitHub\\Arnold_Bot")

with open("Setting.json","r",encoding='utf8') as jFile:
    jdata = json.load(jFile)


intents = discord.Intents.all()
intents.members = True
    #1.5後的權限設置

bot = commands.Bot(command_prefix='$',intents=intents)
    #機器人符號(指令前的符號)





@bot.event
async def on_ready():
    with open("Setting.json","r",encoding='utf8') as jFile:
        jdata = json.load(jFile)
    print("-------->>機器人已上線<<--------")
    for filename in os.listdir('./cmds'):
        if filename.endswith('.py'):
            try:
                await bot.load_extension(f'cmds.{filename[:-3]}')
                print(f'✅   已加載 {filename}')
            except Exception as error:
                print(f'❎   {filename} 發生錯誤  {error}')
    channel = bot.get_channel(int(jdata["後台"]))
    await channel.send(f"✅   機器人開始運行   ✅")

    channel1 = bot.get_channel(1065030744315002940)
    while not bot.is_closed():
        now_time = int(datetime.datetime.now().strftime('%H%M')) #%H%M 時+分
        with open("Setting.json","r",encoding='utf8') as jFile:
            jdata = json.load(jFile)
        if now_time == int(jdata['time']) and counter == 0: 
            await channel1.send("大家早安!\n快來聊天吧!")
            counter = 1
            await asyncio.sleep(1)
        else:
            await asyncio.sleep(1)
            counter = 0
            pass



@bot.command(help="載入某文件", brief="載入某文件")
async def load(ctx,extension):
    await bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'已載入{extension}!')
    print(f"已載入{extension}!")
    channel = bot.get_channel(int(jdata["後台"]))
    await channel.send(f"{ctx.author} 載入 {extension}")

@bot.command(help="卸載某文件", brief="卸載某文件")
async def unload(ctx,extension):
    await bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'已卸載{extension}!')
    print(f'已卸載{extension}!')
    channel = bot.get_channel(int(jdata["後台"]))
    await channel.send(f"{ctx.author} 卸載 {extension}")

@bot.command(help="重載某文件", brief="重載某文件")
async def reload(ctx,extension):
    await bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'已重新載入{extension}!')
    print(f'已重新載入{extension}!')
    channel = bot.get_channel(int(jdata["後台"]))
    await channel.send(f"{ctx.author} 重新載入 {extension}")
    
async def load_extensions(): 
    for filename in os.listdir("./cmds"):
        if filename.endswith(".py"):
            await bot.load_extension(f'cmds.{filename[:-3]}')



if __name__ == "__main__":
    bot.run(jdata["TOKEN"])