import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix='$',intents=intents)

@bot.event
async def on_readey():
    print(">>機器人在線<<")

@bot.event
async def on_member_join(member):
    print(f'{member}join!')
    channel = bot.get_channel(1038586584708173844)
    await channel.send(f'{member}jain!')

@bot.event
async def on_member_remove(member):
    print(f'{member}leave!')
    channel = bot.get_channel(1038586584708173844)
    await channel.send(f'{member}leave!')

@bot.command()
async def ping(ctx): #ctx (上下文，回覆的上下關係) 
    #A：嗨(上文)(使用者，ID，伺服器，頻道)
    #B：安安(下文)
    await ctx.send(f'{round(bot.latency*1000)}(ms)') #預設單位為秒

bot.run("MTA1MDUyNDEzMTEzMDYwOTc5NQ.G86OLA.86u79f6mEj1t70woUwObkgPPNIpwcHpdwAcv3k")