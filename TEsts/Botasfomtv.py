import nextcord

from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.members = True
intents.messages = True
bot = nextcord.ext.commands.Bot(command_prefix='!', intents=intents)

@bot.command(name="hi")
async def SendMessage(ctx):
    await ctx.send('Hello!')

@bot.event
async def on_ready():
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}')

if __name__ == '__main__':
    bot.run("MTA4Nzg1MTUyNjgyOTEzMzkwNA.G3bPTg.OJLsDgotZ-Y4QoSXHMF3vgJGdt2WAdrvwhXhm4")