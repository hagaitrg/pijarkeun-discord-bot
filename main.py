from decouple import config
import discord
from discord.ext import commands
from discord.ext.commands import context


API_TOKEN = config('TOKEN')
API_PREFIX = config('PREFIX')

bot = commands.Bot(command_prefix=API_PREFIX,
                   description="PijarKeun Discord Bot")


@bot.event
async def on_ready():
    print("I am Alive!")


@bot.command(pass_context=True)
async def hello(ctx):
    await ctx.send("Hallo jaga kesehatan dan jangan lupa minum air putih!")


bot.run(API_TOKEN, bot=True, reconnect=True)
