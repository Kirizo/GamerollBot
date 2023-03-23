import random
from craiyon import Craiyon, craiyon_utils
import discord
from discord.ext import commands
from io import BytesIO
import base64

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(intents = intents, command_prefix="!")

gry = ["Liga","TF2","Overwatch"]

generator = Craiyon() # Initialize Craiyon() class

@bot.event
async def on_ready():
    print(f"Successfully logged in as {bot.user.name}!")

# Create command
@bot.command(name='gra')
async def gra(ctx):
    await ctx.send(random.choice(gry))

@bot.command()
async def generuj(ctx, *, prompt: str):
    await ctx.send(f"Generuje \"{prompt}\"...")
    
    generated_images = await generator.async_generate(prompt) # Generate images
    b64_list = await craiyon_utils.async_encode_base64(generated_images.images) # Download images from https://img.craiyon.com and store them as b64 bytestring object
    
    images1 = []
    for index, image in enumerate(b64_list): # Loop through b64_list, keeping track of the index
        img_bytes = BytesIO(base64.b64decode(image)) # Decode the image and store it as a bytes object
        image = discord.File(img_bytes)
        image.filename = f"result{index}.webp"
        images1.append(image) # Add the image to the images1 list
        
    await ctx.reply(files=images1) # Reply to the user with all 9 images in 1 message
        

bot.run("MTA4Nzg1MTUyNjgyOTEzMzkwNA.G3bPTg.OJLsDgotZ-Y4QoSXHMF3vgJGdt2WAdrvwhXhm4")