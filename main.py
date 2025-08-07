import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import fileinput

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"We are ready to go in, {bot.user.name}")

@bot.command()
async def black(ctx):
    await ctx.send('Monkey!')

@bot.command()
async def sanchez(ctx):
    await ctx.send('Fucking Weeb!')

@bot.command()
async def ginger(ctx):
    await ctx.send('Ethan Baker the souless ginger!')

@bot.command()
async def unemployed(ctx):
    await ctx.send('@luhkapalot')

@bot.command()
async def carter(ctx):
    await ctx.send('I may be a Clanker, but at least im not a NIG-')

@bot.command()
async def image(ctx):
    """Send a local image file."""
    # adjust the path to wherever you stored it
    file_path = "Images/tepig.png"
    # send it
    await ctx.send(file=discord.File(file_path))

@bot.command()
async def jeremy(ctx):
    """Send a local image file."""
    # adjust the path to wherever you stored it
    file_path = "Images/jeremyc.png"
    # send it
    await ctx.send(file=discord.File(file_path))
    await ctx.send('Look at this beautiful boy!')

@bot.command()
async def pingremy(ctx):
    await ctx.send('<@418373528077991946>')

@bot.command()
async def pingbaker(ctx):
    await ctx.send('<@379305399813144587>')

@bot.command()
async def echome(ctx, *arg):
    arguments = ', '.join(arg)
    await ctx.send(f'{len(arg)} arguments: {arguments}')

@bot.command()
async def add(ctx, arg1: int, arg2: int):
    result = arg1 + arg2
    if result == 19 and (arg1 == 9 or arg2 == 9):
        result = 21
        await ctx.send(f'{result} :)')
        return

    elif result == 420:
        await ctx.send(f'{result} :)')
        file_path = "Images/weedimage.png"
        # send it
        await ctx.send(file=discord.File(file_path))
        return


    await ctx.send(f'{result}')

@bot.command()
async def addquote(ctx, *arg):
    #open quotes.txt and append a new line with the arguments
    with open('quotes.txt', 'a') as f:
        f.write(' '.join(arg) + '\n')
    return

@bot.command()
async def quotes(ctx):
    #open quotes.txt and read each line and send it as a message
    with open('quotes.txt', 'r') as f:
        lines = f.readlines()
        lineCount = len(lines)
        for i in range(lineCount):
            line = lines[i]
            if not line:
                break
            await ctx.send(line.strip())
        return


@bot.command()
async def commands(ctx):
    await ctx.send('add: math command\nechome: Repeats back what you type after.\nblack\nsanchez\nginger\nunemployed\njeremy\npingbaker\npingremy\naddquote\nquotes\n')






bot.run(token, log_handler=handler, log_level=logging.DEBUG)
