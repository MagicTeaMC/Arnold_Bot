import discord
from discord.ext import commands
import json
import random
import os


#from help_cog import help_cog
#from music_cog import music_cog


os.chdir("C:\\Users\\user\\OneDrive\\文件\\GitHub\\Arnold_Bot")

with open("Setting.json","r",encoding='utf8') as jFile:
    jdata = json.load(jFile)

intents = discord.Intents.all()
intents.members = True
    #1.5後的權限設置

bot = commands.Bot(command_prefix='$',intents=intents)
    #機器人符號(指令前的符號)

#bot.remove_command('help')

#bot.add_cog(help_cog(bot))
#bot.add_cog(music_cog(bot))


@bot.event
async def on_ready():
    print("-------->>機器人已上線<<--------")
    await bot.load_extension("cmds.main")
    await bot.load_extension("cmds.react")
    await bot.load_extension("cmds.event")
    await bot.load_extension("cmds.task")


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
    await ctx.send(f'已重新載入{extension}!')
    
async def load_extensions(): 
    for filename in os.listdir("./cmds"):
        if filename.endswith(".py"):
            await bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
    bot.run(jdata["TOKEN"])