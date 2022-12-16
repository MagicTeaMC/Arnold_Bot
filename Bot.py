import discord
from discord.ext import commands
import json
import random
import os

with open("Setting.json","r",encoding='utf8') as jFile:
    jdata = json.load(jFile)

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix='$',intents=intents)

@bot.event
async def on_readey():
    print(">>機器人在線<<")

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

for filename in os.listdir("./cmds"):
    if filename.endswith(".py"):
        bot.load_extension(f'cmds.{filename[:-3]}')


bot.run(jdata["TOKEN"])