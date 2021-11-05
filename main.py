from dotenv import load_dotenv
import os
import discord
from discord.ext import commands
from discord.ext.commands import context

load_dotenv()

API_TOKEN = os.getenv("TOKEN")
API_PREFIX = os.getenv("PREFIX")

bot = commands.Bot(command_prefix=API_PREFIX,
                   description="PijarKeun Discord Bot")


@bot.event
async def on_ready():
    print("I am Alive!")


@bot.command(pass_context=True)
async def hello(ctx, name: str):
    await ctx.send(f"Hallo {name} jaga kesehatan dan jangan lupa minum air putih!")


@bot.command(pass_context=True)
async def bye(ctx):
    embed = discord.Embed(
        title="Hello I am leaving now"
    )

    msg = await ctx.send(embed=embed)
    await msg.add_reaction('✅')


@bot.command(pass_context=True)
async def status(ctx):
    embed = discord.Embed(
        title="bot is under developing"
    )

    msg = await ctx.send(embed=embed)
    await msg.add_reaction('✅')


@bot.command(pass_context=True)
async def clear(ctx, amount: str):
    if amount == 'all':
        await ctx.channel.purge()
    else:
        await ctx.channel.purge(limit=(int(amount)+1))


bot.run(API_TOKEN, bot=True, reconnect=True)
