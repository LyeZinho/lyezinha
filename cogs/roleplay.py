import os
import discord
from discord.ext import commands
import random

class Roleplay(commands.Cog):

  """Roleplay commands"""
  
  def __init__(self, bot):
    self.bot = bot
		
    @bot.command(name='ping') 
    async def ping(ctx):
      await ctx.reply('Pong!', mention_author=False) #Sends a chat message. Remember to await async functions.
      


    @bot.command(name='inviteurl')
    async def inviteurl(ctx):
      ctx = ctx

      await ctx.reply('https://discordapp.com/oauth2/authorize?&client_id=' + str(self.bot.user.id) + '&scope=bot&permissions=8', mention_author=False)

    @bot.command(name='d4', help='Roll 4 sides dice\n command !d20 <dice count>')
    async def d4(ctx):
      ctx = ctx
      await ctx.reply('↳ `{0}` ↲'.format(random.randint(1,4)))

    @bot.command(name='d6', help='Roll 6 sides dice\n command !d20 <dice count>')
    async def d6(ctx):
      ctx = ctx
      await ctx.reply('↳ `{0}` ↲'.format(random.randint(1,6)))
    
    @bot.command(name='d10', help='Roll 10 sides dice\n command !d20 <dice count>')
    async def d10(ctx):
      ctx = ctx
      await ctx.reply('↳ `{0}` ↲'.format(random.randint(1,10)))
    
    @bot.command(name='d12', help='Roll 12 sides dice\n command !d20 <dice count>')
    async def d12(ctx):
      ctx = ctx
      await ctx.reply('↳ `{0}` ↲'.format(random.randint(1,12)))
    
    @bot.command(name='d100', help='Roll 100 sides dice\n command !d20 <dice count>')
    async def d100(ctx):
      ctx = ctx
      rolls = [
        "00",
        "10",
        "20",
        "30",
        "40",
        "50",
        "60",
        "70",
        "80",
        "90",
      ]
      i = random.randint(0,9)
      await ctx.reply('↳ `{0}` ↲'.format(rolls[i]))
    
    @bot.command(name='d20', help='Roll 20 sides dice\n command !d20 <dice count>')
    async def d20(ctx):
      ctx = ctx
      await ctx.reply('↳ `{0}` ↲'.format(random.randint(1,20)))
    
  


def setup(bot):
	bot.add_cog(Roleplay(bot))