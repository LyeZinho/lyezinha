import os
import random
import json
import discord
import time
from discord.ext import commands
from discord.ext.commands import Bot
from discord import Embed
import asyncio
import requests



TOKEN = os.environ['TOKEN']
bot = commands.Bot(command_prefix='&', case_insensitive=True)


@bot.event
async def on_ready():
      await bot.change_presence(activity=discord.Game(name="&help"))
      print("Bot is ready")
'''
# Setting `Playing ` status
await 

# Setting `Streaming ` status
await bot.change_presence(activity=discord.Streaming(name="My Stream", url=my_twitch_url))

# Setting `Listening ` status
await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="a song"))

# Setting `Watching ` status
await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="a movie"))
'''



#Commands
@bot.command(name='picwaifu', help='😳send some waifu pics😳 \n command !picwaifu')
async def pic_waifu(ctx):
  response = requests.get('https://api.waifu.pics/sfw/waifu')
  imageResponse = response.json()["url"]
  embed = Embed(
            title="-🌸Waifu🌸-"
              )
  await ctx.send(embed=embed)
  await ctx.send("{0}".format(imageResponse))






@bot.command(name='picneko', help='😳send some neko pics😳 \n command !picneko')
async def pic_neko(ctx):
  response = requests.get('https://api.waifu.pics/sfw/neko')
  imageResponse = response.json()["url"]
  embed = Embed(
            title="-🐱Nekos🐱-"
              )
  await ctx.send(embed=embed)
  await ctx.send("{0}".format(imageResponse))






@bot.command(name='aniquote', help='📜send some anime quotes📜 \n command !aniquote')
async def aniquote(ctx):
  response = requests.get('https://animechan.vercel.app/api/random')
  quoteResponse = response.json()
  embed = Embed(
            title="-📜AniQuotes📜-"
              )
  embed.add_field(name="{0}".format(quoteResponse["anime"]),
  value="**{0}**\n \n{1}".format(quoteResponse["character"], quoteResponse["quote"]), inline=True)
  await ctx.send(embed=embed)






@bot.command(name='yomama', help='😎send your mother facts😎 \n command !yomama')
async def yomama(ctx):
  response = requests.get('https://yomomma-api.herokuapp.com/jokes?count=4')
  factsResponse = response.json()
  embed = Embed(
            title="-😎YoMama😎-"
              )
  embed.add_field(name="Fact 1",value="**{0}**\n".format(factsResponse[0]["joke"]), inline=True)
  embed.add_field(name="Fact 2",value="**{0}**\n".format(factsResponse[1]["joke"]), inline=True)
  embed.add_field(name="Fact 3",value="**{0}**\n".format(factsResponse[2]["joke"]), inline=True)
  await ctx.send(embed=embed)



@bot.command(name='changemymind', help='😲Change your mind😲 \n command !changemymind <text>')
async def args(ctx, *, arg1):
  username = os.environ['IMFLIPUSER']
  password = os.environ['IMFLIPPASS']
  if arg1 != None:
    URL = 'https://api.imgflip.com/caption_image'
    _id = "129242436"
    params = {
    'username':username,
    'password':password,
    'template_id':_id,
    'text0':arg1,
    }
    response = requests.request('POST',URL,params=params).json()
    vaule1 = response["data"]
    finalResult = vaule1["url"]
    await ctx.send("{0}".format(finalResult))
  else:
      replyembed = Embed(title="-🤔 Wrong Sintax 🤔-")
      replyembed.add_field(name="Correct command sintax",value="command !changemymind <text>", inline=True)
      await ctx.send(replyembed=replyembed)
    



bot.run(TOKEN)