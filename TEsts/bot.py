import nextcord
from nextcord.ext import commands
intents = nextcord.Intents.default()
intents.members = True
intents.messages = True
bot = nextcord.ext.commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print("Bot urchomiony!")
    
@bot.command(name="witam")
async def witam(ctx):
    await ctx.send('Witam was')


token = open("token.txt","r")
if __name__ == '__main__':
    bot.run(token.read())
token.close()