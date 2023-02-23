import discord
from discord.ext import commands

class Leave(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('leave cmd ready')

    @commands.command()
    async def leave(self, ctx):
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice.is_connected():
            voice.stop()
            await voice.disconnect()
            await ctx.send("Left the voice channel!")
        else:
            await ctx.send("I am not connected to a voice channel.")

def setup(bot):
    bot.add_cog(Leave(bot))