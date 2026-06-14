import os
import json
import platform
from dotenv import load_dotenv
import discord
from discord.ext import commands
from botutils.utils import send_backend
from api.frontend.sub import start_bot_backend
import asyncio
import datetime


load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True 

bot = commands.Bot(command_prefix="!", intents=intents)
VERSION = "1.0.0"
ZAVATI = None # Zavati's UID will not be added in dev, for security reasons. You can place your own (or equivelent) here.


@bot.event
async def on_ready():
    activity = discord.Activity(
        type=discord.ActivityType.watching,
        name="Zavati's Socials",
        details="💘 Mananging Relationship Status"
    )
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print(f"Logged in as {bot.user}")
    print("Starting backend")

    asyncio.create_task(start_bot_backend())


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
        type=discord.ActivityType.streaming,
        name="Websocket Info",
        details="Started running sucessfully"
    )
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    await ctx.send("Started backend")


@bot.command()
async def zavati(ctx):
    members = ctx.guild

    theZava = members.get_member(ZAVATI)

    if ctx.author.id is ZAVATI:
        await ctx.send(f"""
<@{ZAVATI}> you are too cute to execute this
"""
)

    if theZava is None:
        await ctx.send("""
# Failed to send Zavati status:
`theZava was None at runtime`
""")
    else:
        time_found = datetime.datetime.now()
        resp_data = await send_backend(zavati=ZAVATI, execid=ctx.author.id, execuser=ctx.author, timefound=time_found)
        
        await ctx.send(f"""
# Zavati status sent sucessfully
```
Details:
Username: {ctx.author}
UID: {ctx.author.id}
Time Registered: {time_found}
Zavati Present: {True}
```
# Backend Response
```json
{json.dumps(resp_data, indent=2)}
```""")
    

bot.run(os.getenv("DISCORD_TOKEN"))
