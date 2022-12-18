import discord
from discord.ext import commands
import json
import random
import os

os.chdir("C:\\Users\\user\\OneDrive\\文件\\GitHub\\Arnold_Bot")

with open("Setting.json","r",encoding='utf8') as jFile:
    jdata = json.load(jFile)

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix='$',intents=intents)

@bot.event
async def on_ready():
    print(">>Bot is online<<")
    await bot.load_extension("cmds.main")
    await bot.load_extension("cmds.react")

@bot.event
async def on_member_join(member):
    print(f'{member}join!')
    channel = bot.get_channel(int(jdata["join_channel"]))
    await channel.send(f'{member}join!')

@bot.event
async def on_member_remove(member):
    print(f'{member}leave!')
    channel = bot.get_channel(int(jdata["leave_channel"]))
    await channel.send(f'{member}leave!')

@bot.command()
async def load(ctx,extension):
    await bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'已載入{extension}!')

@bot.command()
async def unload(ctx,extension):
    await bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'已卸載{extension}!')

@bot.command()
async def reload(ctx,extension):
    await bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'從新載入{extension}!')
    
async def load_extensions(): 
    for filename in os.listdir("./cmds"):
        if filename.endswith(".py"):
            await bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
    bot.run(jdata["TOKEN"])