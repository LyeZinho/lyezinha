import os
import random
import json
from discord.ext import commands
from discord import Embed
from discord import Colour
import requests

TOKEN = os.environ['TOKEN']


bot = commands.Bot(command_prefix='!')


@bot.command(name='waifu', help='send some waifu pics😳')
async def nine_nine(ctx):
  response = requests.get('https://api.waifu.pics/sfw/waifu')
  imageResponse = response.json()["url"]
  embed = Embed(
            title="-🌸Waifu🌸-"
              )
  await ctx.send(embed=embed)
  await ctx.send("{0}".format(imageResponse))
   

bot.run(TOKEN)