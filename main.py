import datetime
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import context
from discord.utils import get
from datetime import datetime

load_dotenv()

API_TOKEN = os.getenv("TOKEN")
API_PREFIX = os.getenv("PREFIX")

intents = discord.Intents(messages=True, guilds=True)
bot = commands.Bot(command_prefix=API_PREFIX,
                   description="PijarKeun Discord Bot")


@bot.event
async def on_ready():
    print("Bot on Duty! 🔥")


@bot.command(pass_context=True)
async def hello(ctx, name: str):
    await ctx.send(f"Hallo {name} jaga kesehatan dan jangan lupa minum air putih!")


@bot.event
async def on_raw_reaction_add(payload):
    msgId = payload.message_id

    if msgId == 906332391528861736:
        guild_id = payload.guild_id
        guild = bot.get_guild(guild_id)
        member = get(guild.members, id=payload.user_id)

        if payload.emoji.name == '👩‍💼':
            role = get(payload.member)
        elif payload.emoji.name == '🗣️':
            role = discord.utils.get(guild.roles, name="Scrum Master")
        elif payload.emoji.name == '👨‍💻':
            role = discord.utils.get(guild.roles, name="Back End")
        elif payload.emoji.name == '📱':
            role = discord.utils.get(guild.roles, name="Front End")
        elif payload.emoji.name == '⏳':
            role = discord.utils.get(guild.roles, name="QA")
        elif payload.emoji.name == '⛑️':
            role = discord.utils.get(guild.roles, name="Maintainer")
        await payload.member.add_roles(role)


@bot.command(pass_context=True)
async def testRole(ctx):
    embed = discord.Embed(
        title="Selamat datang di Bot PijarKeun",
        url="https://github.com/hagaitrg/pijarkeun-discord-bot",
        description="Silahkan pilih role terlebih dahulu \n \n 👩‍💼 : Product Owner \n 🗣️ : Scrum Master \n 👨‍💻 : Back End \n 📱 : Front End \n ⏳ : QA \n ⛑️ : Maintainer ",
        timestamp=datetime.now(),
    )

    msg = await ctx.send(embed=embed)
    # PO Role
    await msg.add_reaction('👩‍💼')
    # Scrum Master Role
    await msg.add_reaction('🗣️')
    # Backend Role
    await msg.add_reaction('👨‍💻')
    # Frontend Role
    await msg.add_reaction('📱')
    # QA Role
    await msg.add_reaction('⏳')
    # Maintainer Role
    await msg.add_reaction('⛑️')

    await ctx.message.add_reaction('✔️')


@bot.command(pass_context=True)
async def status(ctx):
    embed = discord.Embed(
        title="bot is under developing"
    )

    msg = await ctx.send(embed=embed)


@bot.command(pass_context=True)
async def clear(ctx, amount: str):
    if amount == 'all':
        await ctx.channel.purge()
    else:
        await ctx.channel.purge(limit=(int(amount)+1))


bot.run(API_TOKEN, bot=True, reconnect=True)
