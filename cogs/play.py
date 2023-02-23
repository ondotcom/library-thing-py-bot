import discord
import youtube_dl
from discord.ext import commands

class Play(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.queue = []

    @commands.Cog.listener()
    async def on_ready(self):
        print('play cmd ready')

    @commands.command()
    async def play(self, ctx, url, volume = 0.07):
        if ctx.author.voice is None:
            await ctx.send("You are not in a voice channel!")
        else:
            FFMPEG_OPTIONS = {
                'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                'options': '-vn'}

            ydl_opts = {'format': 'bestaudio'}
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                URL = info['formats'][0]['url']

            channel = ctx.message.author.voice.channel
            
            if ctx.voice_client is not None:
                return await ctx.voice_client.move_to(channel)
            else:
                await channel.connect()
            
            voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)

            if voice.is_playing():
                print("Already playing")

            # if ctx.voice_client:
            #     await ctx.voice_client.move_to(ctx.author.voice.channel)
            # else:
            #     await ctx.author.voice.channel.connect()
                
            source = discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS)
            source = discord.PCMVolumeTransformer(source, volume = volume)
            voice.play(source)
            await ctx.send("Playing!")

def setup(bot):
    bot.add_cog(Play(bot))