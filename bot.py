import discord
import json
import datetime
import asyncio
import os
import aiohttp
import youtube_dl
from discord import Intents, Embed
from discord.ext import commands

intents = Intents.default()
intents.typing = False
intents.presences = True

#load the config
with open('config.json', 'r') as f:
    config = json.load(f)

activity = discord.Activity(type=discord.ActivityType.watching, name="gay yaoi anime porn")
status = discord.Status.dnd
bot = commands.Bot(command_prefix='t.', intents=intents, activity=activity, status=status)

#login
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

#cog things
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

#help
@bot.command()
async def asdf(ctx):
    print("Command received" + ctx.message.content)
    await ctx.channel.send("asdf")

token = config['token']
bot.run(token)