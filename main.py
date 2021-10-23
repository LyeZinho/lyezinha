import os
import random
import json
from discord.ext import commands
from discord import Embed
from discord import Colour
import requests

TOKEN = os.environ['TOKEN']


bot = commands.Bot(command_prefix='!')


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
            title="-🌸Waifu🌸-"
              )
  await ctx.send(embed=embed)
  await ctx.send("{0}".format(imageResponse))
bot.run(TOKEN)