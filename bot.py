import os
import platform
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
VERSION = "1.0.0"


@bot.event
async def on_ready():
    activity = discord.Activity(
        type=discord.ActivityType.watching,
        name="Zavati's Socials",
        details="💘 Mananging Relationship Status",
    )
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print(f"Logged in as {bot.user}")


@bot.command()
async def test(ctx: commands.Context):
    await ctx.send("i think it worked")


@bot.command()
async def implinfo(ctx: commands.Context):
    os_name = platform.platform()
    cpu_brand = platform.processor() or "Unknown"
    cores = os.cpu_count() or 0
    try:
        import psutil
        ram = psutil.virtual_memory().total
        ram_gb = ram / (1024 ** 3)
        ram_str = f"{ram_gb:.2f} GB"
    except ImportError:
        ram_str = "N/A (install psutil)"

    await ctx.send(
        f"# Zavati Script Loader Info\n"
        f"```\n"
        f"OS: {os_name}\n"
        f"Version: {VERSION}\n"
        f"RAM: {ram_str}\n"
        f"Cores: {cores}\n"
        f"CPU: {cpu_brand}\n"
        f"```"
    )


@bot.command()
async def start(ctx: commands.Context):
    activity = discord.Activity(
        type=discord.ActivityType.watching,
        name="Zavati's Socials",
        details="💘 Mananging Relationship Status",
    )
    await bot.change_presence(status=discord.Status.online, activity=activity)
    await ctx.send("RP started")


bot.run(os.getenv("DISCORD_TOKEN"))
