import os
import json
from discord.ext import commands
from discord import Embed
import requests

#This is an example cog to show how commands can be added

class Fun(commands.Cog):

  """Fun commands"""
  
  def __init__(self, bot):
    self.bot = bot
		

    #Pics neko from api.waifu.pics
    @bot.command(name='picneko', help='😳send some neko pics😳 \n command !picneko')
    async def pic_neko(ctx):
      response = requests.get('https://api.waifu.pics/sfw/neko')
      imageResponse = response.json()["url"]
      embed = Embed(
                title="-🐱Nekos🐱-"
                  )
      await ctx.reply(embed=embed, mention_author=False)
      await ctx.send("{0}".format(imageResponse))
    


    #Pics waifu from  api.waifu.pics
    @bot.command(name='picwaifu', help='😳send some waifu pics😳 \n command !picwaifu')
    async def pic_waifu(ctx):
      response = requests.get('https://api.waifu.pics/sfw/waifu')
      imageResponse = response.json()["url"]
      embed = Embed(
                title="-🌸Waifu🌸-"
                  )
      await ctx.reply(embed=embed, mention_author=False)
      await ctx.send("{0}".format(imageResponse))



    #Pics waifu from  api.waifu.pics
    @bot.command(name='picwaifu', help='😳send some waifu pics😳 \n command !picwaifu')
    async def pic_waifu(ctx):
      response = requests.get('https://api.waifu.pics/sfw/waifu')
      imageResponse = response.json()["url"]
      embed = Embed(
                title="-🌸Waifu🌸-"
                  )
      await ctx.reply(embed=embed, mention_author=False)
      await ctx.send("{0}".format(imageResponse))


    @bot.command(name='dance', help='😳send some waifu pics😳 \n command !picwaifu')
    async def dance(ctx):
      response = requests.get('https://api.waifu.pics/sfw/dance')
      imageResponse = response.json()["url"]
      await ctx.reply("{0}".format(imageResponse))

    
    #Yomama facts from yomomma-api
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
      await ctx.reply(embed=embed, mention_author=False)


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

def setup(bot):
	bot.add_cog(Fun(bot))