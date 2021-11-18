import os
import discord
from discord.ext import commands
from flask import Flask
bot = commands.Bot(command_prefix=['-&'], description='.')


bot.owner_id = 524622388629995541

#Cogs
for cog in ['cogs.fun','cogs.ready','cogs.roleplay']:
	bot.load_extension(cog)


app = Flask('app')

@app.route('/')
def hello_world():
  return 'main bot'

app.run(host='0.0.0.0', port=8080)




@bot.command()
@commands.is_owner()
async def load(ctx, cog:str):
	try:
		bot.load_extension(cog)
	except Exception as e:
		await ctx.send(e)
	else:
		await ctx.reply('Cog: ' + cog + '\n Foi carregado com sucesso!')
		
@bot.command()
@commands.is_owner()
async def unload(ctx, cog:str):
	try:
		bot.unload_extension(cog)
	except Exception as e:
		await ctx.send(e)
	else:
		await ctx.reply('Cog: ' + cog + '\n Foi descarregado com sucesso!')
		
@bot.command()
@commands.is_owner()
async def reload(ctx, cog:str):
	try:
		bot.unload_extension(cog)
		bot.load_extension(cog)
	except Exception as e:
		await ctx.send(e)
	else:
		await ctx.reply('Cog: ' + cog + '\n Foi recarregado com sucesso!')

		

TOKEN = os.environ['TOKEN']
bot.run(TOKEN)