import os
import random
import json
import discord
from discord.ext import commands
from discord import Embed
import requests



TOKEN = os.environ['TOKEN']


bot = commands.Bot(command_prefix='!')


#Commands
@bot.command(name='picwaifu', help='😳send some waifu pics😳')
async def pic_waifu(ctx):
  response = requests.get('https://api.waifu.pics/sfw/waifu')
  imageResponse = response.json()["url"]
  embed = Embed(
            title="-🌸Waifu🌸-"
              )
  await ctx.send(embed=embed)
  await ctx.send("{0}".format(imageResponse))






@bot.command(name='picneko', help='😳send some neko pics😳')
async def pic_neko(ctx):
  response = requests.get('https://api.waifu.pics/sfw/neko')
  imageResponse = response.json()["url"]
  embed = Embed(
            title="-🐱Nekos🐱-"
              )
  await ctx.send(embed=embed)
  await ctx.send("{0}".format(imageResponse))






@bot.command(name='aniquote', help='📜send some anime quotes📜')
async def aniquote(ctx):
  response = requests.get('https://animechan.vercel.app/api/random')
  quoteResponse = response.json()
  embed = Embed(
            title="-📜AniQuotes📜-"
              )
  embed.add_field(name="{0}".format(quoteResponse["anime"]),
  value="**{0}**\n \n{1}".format(quoteResponse["character"], quoteResponse["quote"]), inline=True)
  await ctx.send(embed=embed)
bot.run(TOKEN)






