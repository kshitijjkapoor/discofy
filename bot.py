import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv(os.path.dirname(os.path.realpath(__file__)))
client = commands.Bot(command_prefix = "!")

client.remove_command("help")

@client.command()
async def hello(ctx):
    await ctx.send(f"Hello, {ctx.author.mention}")

client.run(os.getenv("TOKEN"))