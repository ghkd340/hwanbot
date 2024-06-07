import discord
import asyncio
import random
from discord.ext import commands
from gtts import gTTS
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print("이 문장은 Python의 내장 함수를 출력하는 터미널에서 실행됩니다\n지금 보이는 것처럼 말이죠")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("싸우자세상아덤벼라세상아"))

@bot.event
async def on_message(message):
    if message.content.startswith("!환서"):
        pic = "ghkstj" + str(random.randint(1, 30)) + ".jpg"
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("!건희"):
        pic = "rjsgml" + str(random.randint(1, 10)) + ".jpg"
        await message.channel.send(file=discord.File(pic))

    await bot.process_commands(message)  # 이 줄을 추가하여 on_message에서 명령어 처리가 되도록 합니다.

@bot.command()
async def 들어와(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("음성 채널에 먼저 들어가 주세요.")

@bot.command()
async def 나가(ctx):
    if ctx.voice_client:
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.send("봇이 음성 채널에 연결되어 있지 않습니다.")

@bot.command()
async def tts(ctx, *, text):
    tts = gTTS(text, lang='ko')
    tts.save("tts.mp3")
    if ctx.voice_client:
        if ctx.voice_client.is_playing():
            ctx.voice_client.stop()
        ctx.voice_client.play(discord.FFmpegPCMAudio("tts.mp3"), after=lambda e: print('done', e))

        while ctx.voice_client.is_playing():
            await asyncio.sleep(1)
    else:
        await ctx.send("봇이 음성 채널에 연결되어 있지 않습니다. !들어와 명령어로 봇을 음성 채널에 연결하세요.")

@bot.command()
async def 노래(ctx, *, text):
    text = text + ".mp3"
    if ctx.voice_client:
        if ctx.voice_client.is_playing():
            ctx.voice_client.stop()
        ctx.voice_client.play(discord.FFmpegPCMAudio(text), after=lambda e: print('done', e))

        while ctx.voice_client.is_playing():
            await asyncio.sleep(1)
    else:
        await ctx.send("봇이 음성 채널에 연결되어 있지 않습니다. !들어와 명령어로 봇을 음성 채널에 연결하세요.")



# 봇을 실행시키기 위한 토큰을 작성해주는 곳i
bot.run('MTI0Nzk1OTc5MDgwMjQzNjE3OA.GIjX0L.c2zMcQfYMtQ_woSVQSdLAUT-w6Zff1bgqUXSms')