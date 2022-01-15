import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

prefix = commands.Bot( command_prefix=">" )
TOKEN = DISCORD_BOT_TOKEN

load_dotenv()

token = os.getenv(TOKEN)

client = discord.Client()

@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'hello':
        await message.channel.send("Hi there!")
    
    if message.content == 'who are you?':
        await message.channel.send("I am a generic discord bot created by SMAntony")
    
    if message.content == 'what do you do?':
        await message.channel.send("Right now, I am pretty inefficient but my creator promised me to update with exciting new features. So I am waiting for new updates to my neural networks")

# @client.event
# async def on_ready( ):
#            print("Bot is ready")

client.run(TOKEN)
