import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import asyncio
import datetime


class Task(Cog_Extension):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    self.counter = 0

  @commands.command()
  async def time_task(self, ctx):
      await self.bot.wait_until_ready()
      self.channel = self.bot.get_channel(1065030744315002940)
      while not self.bot.is_closed():
        now_time = datetime.datetime.now().strftime('%H%M%S') #%H%M 時+分
        with open("Setting.json","r",encoding='utf8') as jFile:
          jdata = json.load(jFile)
        if now_time == jdata['time'] and self.counter == 0: 
          await self.channel.send("大家早安\n快來聊天吧!")
          self.counter = 1
          await asyncio.sleep(1)
        else:
          await asyncio.sleep(1)
          self.counter = 0
          pass

  #self.bg_task=self.bot.loop.create_task(time_task())
'''
  @commands.command()
  async def set_time(self,ctx,time:int):
    self.counter = 0 
    with open("Setting.json","r",encoding='utf8') as jFile:
      jdata = json.load(jFile)

    jdata["time"] = time
    with open("Setting.json","w",encoding='utf8') as jFile:
      json.dump(jFile,jFile,indent=4)

    
    async def interval():
      await self.bot.wait_until_ready()
      self.channel = self.bot.get_channel(1053893211539644416)
      while not self.bot.is_closed():
        await self.channel.send("Hi! I'am running!")
        await asyncio.sleep(3600) 
        #單位為秒

    self.bg_task=self.bot.loop.create_task(interval())

  @commands.command()
  async def set_channel(self,ctx,ch:int):
    self.channel=self.bot.get_channel(ch)
    await ctx.send(f'設定頻道：{self.channel.mention}')
'''


async def setup(bot):
  await bot.add_cog(Task(bot))
