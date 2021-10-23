import os
import random
import json
from discord.ext import commands
from discord import Embed
from discord import Colour
import requests
import datetime, time

TOKEN = os.environ['TOKEN']


bot = commands.Bot(command_prefix='!')


def get_bot_uptime(self):
        now = datetime.datetime.utcnow()
        delta = now - self.bot.uptime
        hours, remainder = divmod(int(delta.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        if days:
            fmt = '{d} days, {h} hours, {m} minutes, and {s} seconds'
        else:
            fmt = '{h} hours, {m} minutes, and {s} seconds'
        return fmt.format(d=days, h=hours, m=minutes, s=seconds)




@bot.command(name='picwaifu', help='send some waifu pics😳')
async def pic_waifu(ctx):
  response = requests.get('https://api.waifu.pics/sfw/waifu')
  imageResponse = response.json()["url"]
  embed = Embed(
            title="-🌸Waifu🌸-"
              )
  await ctx.send(embed=embed)
  await ctx.send("{0}".format(imageResponse))




@bot.command(name='picneko', help='send some neko pics😳')
async def pic_neko(ctx):
  response = requests.get('https://api.waifu.pics/sfw/neko')
  imageResponse = response.json()["url"]
  embed = Embed(
            title="-🐱Nekos🐱-"
              )
  await ctx.send(embed=embed)
  await ctx.send("{0}".format(imageResponse))





@bot.command(name='picneko', help='send some neko pics😳')
async def uptime(ctx):
    await ctx.send('Uptime: **{}**'.format(get_bot_uptime()))


bot.run(TOKEN)


