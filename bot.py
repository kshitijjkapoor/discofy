import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
import server_log

load_dotenv(os.path.dirname(os.path.realpath(__file__)))
client = commands.Bot(command_prefix = "?")

client.remove_command("help")

@client.command()
async def hello(ctx):
    await ctx.send(f"Hello, {ctx.author.mention}")

@client.command(pass_context = True)
async def add(ctx, song_name: str):

    const = server_log.Logs(f"{ctx.message.guild.id}", f"{ctx.author}")
    result = const.add(song_name)
    uname = str(ctx.author).split("#")

    if result is True:
        await ctx.send(f"Added '{song_name}' to {uname[0]}'s queue")

    else:
        await ctx.send(f"Unable to add song to queue")

client.run(os.getenv("TOKEN"))