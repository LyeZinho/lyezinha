import discord
from discord.ext import commands


class Ready(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
      
    @commands.Cog.listener()
    async def on_ready(self):
        print('Ready!')
        print('Logged in as ---->', self.bot.user)
        print('ID:', self.bot.user.id)
        print('Invite URL: ' + 'https://discordapp.com/oauth2/authorize?&client_id=' + str(self.bot.user.id) + '&scope=bot&permissions=8')
        activity = discord.Game(name="-&help for some help", type=3)
        await self.bot.change_presence(status=discord.Status.idle, activity=activity)
        channel = self.bot.get_channel(910901122603040802)
        await channel.send("**LyeZinha esta Online!**")
        
    

    
    
def setup(bot):
    bot.add_cog(Ready(bot))