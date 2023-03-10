import discord
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('ping cmd ready')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('pong')

def setup(bot):
    bot.add_cog(Ping(bot))