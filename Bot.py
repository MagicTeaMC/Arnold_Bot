import discord
from discord.ext import commands
import json
import random

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

@bot.command()
async def ping(ctx): #ctx (上下文，回覆的上下關係) 
    #A：嗨(上文)(使用者，ID，伺服器，頻道)
    #B：安安(下文)
    await ctx.send(f'{round(bot.latency*1000)}(ms)') #預設單位為秒

@bot.command()
async def 單一圖片(ctx):
    pic = discord.File(jdata['pic'])
    await ctx.send(file=pic)

@bot.command()
async def 圖片(ctx):
    random_pic = random.choice(jdata['randompic'])
    rpic = discord.File(random_pic)
    await ctx.send(file=rpic)

@bot.command()
async def web(ctx):
    random_pic = random.choice(jdata['url_pic'])
    await ctx.send(random_pic)

bot.run(jdata["TOKEN"])