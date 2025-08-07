import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import json
import os

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Load or create image map
if os.path.exists("data.json"):
    with open("data.json", "r") as f:
        image_map = json.load(f)
else:
    image_map = {}

def save_image_map():
    with open("data.json", "w") as f:
        json.dump(image_map, f, indent=4)

"""
@bot.command()
async def image(ctx, *, keyword):
    #Send the image associated with the keyword.
    keyword = keyword.lower()

    if keyword not in image_map:
        await ctx.send("No image found for that keyword.")
        return

    file_path = image_map[keyword]

    if not os.path.exists(file_path):
        await ctx.send("Image file not found. Maybe it was deleted.")
        return

    await ctx.send(file=discord.File(file_path))
"""
@bot.command()
async def tagimage(ctx, keyword):
    #Attach an image with a keyword. Usage: !tagimage pizza (attach an image)
    if not ctx.message.attachments:
        await ctx.send("Please attach an image file.")
        return

    attachment = ctx.message.attachments[0]

    if not attachment.filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
        await ctx.send("Only image files are allowed.")
        return

    # Download and save the file
    file_ext = attachment.filename.split('.')[-1]
    filename = f"{keyword}_{ctx.author.id}.{file_ext}"
    file_path = os.path.join("images", filename)

    await attachment.save(file_path)

    # Update the keyword mapping
    image_map[keyword.lower()] = file_path
    save_image_map()

    await ctx.send(f"Image saved for keyword '{keyword}'!")


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
    await ctx.send('<@297764518568656897>')

@bot.command()
async def carter(ctx):
    await ctx.send('I may be a Clanker, but at least im not a NIG-')

@bot.command()
async def image(ctx):
    """Send a local image file."""
    # adjust the path to wherever you stored it
    file_path = "tImages/epig.png"
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



@bot.event
async def on_message(message):
    # Avoid responding to itself
    if message.author == bot.user:
        return

    # Replace this with the actual user ID you want to track
    watched_user_id = 844944679330119680

    # Check if that user is mentioned in the message
    for user in message.mentions:
        if user.id == watched_user_id:
            await message.channel.send(f"NIGGER ALERT!!!")

    # Check if the user was mentioned in the message
    #for user in message.mentions):
    #    if message.mentions[0].user == watched_user_id:
    #     await ctx.send('Come hither my little Nigger!')
    await bot.process_commands(message)

@bot.event
async def on_message(message):
    # Avoid responding to itself
    if message.author == bot.user:
        return

    # Replace this with the actual user ID you want to track
    watched_user_id = 275760118509862913

    # Check if that user is mentioned in the message
    for user in message.mentions:
        if user.id == watched_user_id:
            await message.channel.send(f"Come here babygirl, or better yet, FUCKING SHOWER.")

    # Check if the user was mentioned in the message
    #for user in message.mentions):
    #    if message.mentions[0].user == watched_user_id:
    #     await ctx.send('Come hither my little Nigger!')
    await bot.process_commands(message)

@bot.event
async def on_message(message):
    # Avoid responding to itself
    if message.author == bot.user:
        return


    # Replace this with the actual user ID you want to track

    baker_user_id = 379305399813144587
    remy_user_id = 418373528077991946

    if message.author.id != baker_user_id:
        return

    # Check if that user is mentioned in the message
    for user in message.mentions:
        if user.id == remy_user_id:
            await message.channel.send(f"Awww daddy baker called? Remy's coming!")

    # Check if the user was mentioned in the message
    #for user in message.mentions):
    #    if message.mentions[0].user == watched_user_id:
    #     await ctx.send('Come hither my little Nigger!')
    await bot.process_commands(message)


@bot.command()
async def joel(ctx):
    """Send a local image file."""
    # adjust the path to wherever you stored it
    file_path = "joelimage.png"
    # send it
    await ctx.send(file=discord.File(file_path))
    await ctx.send('Super Jew!')

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
        lines = file.readlines()
        lineCount = len(lines)
        for i in range(lineCount):
            line = f.readline()
            if not line:
                break
            await ctx.send(line.strip())
        return


@bot.command()
async def commands(ctx):
    await ctx.send('add: math command\nechome: Repeats back what you type after.\nblack\nsanchez\nginger\nunemployed\njeremy\njoel\npingbaker\npingremy\n')






bot.run(token, log_handler=handler, log_level=logging.DEBUG)
