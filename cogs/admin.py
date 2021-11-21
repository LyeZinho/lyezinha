import os
import discord
from discord.ext import commands
import random

class Admin(commands.Cog):

  """Roleplay commands"""
  
  def __init__(self, bot):
    self.bot = bot

    bot.owner_id = 524622388629995541
    @bot.command(name='setgame')
    @commands.is_owner()
    async def setgame(ctx, *, arg):
      ctx = ctx
      if arg == "default":        
        activity = discord.Game(name="-& for some help", type=3)
        await self.bot.change_presence(status=discord.Status.idle, activity=activity)
      else:        
        activity = discord.Game(name=arg, type=3)
        await self.bot.change_presence(status=discord.Status.idle, activity=activity)



def setup(bot):
	bot.add_cog(Admin(bot))