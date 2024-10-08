import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

# Your bot token
TOKEN = os.getenv('DISCORD_TOKEN')

# A dictionary to map English typo to Thai text
eng2thai = {
    '1': 'ๅ',
    '!': '+',
    '@': '๑',
    '2': '/',
    '3': '-',
    '#': '๒',
    '4': 'ภ',
    '$': '๓',
    '5': 'ถ',
    '%': '๔',
    '6': 'ุ',
    '^': 'ู',
    '7': 'ึ',
    '&': '฿',
    '8': 'ค',
    '*': '๕',
    '9': 'ต',
    '': '๖',
    '0': 'จ',
    ')': '๗',
    '-': 'ข',
    '_': '๘',
    '=': 'ช',
    '+': '๙',
    'q': 'ๆ',
    'Q': '๐',
    'w': 'ไ',
    'W': '"',
    'e': 'ำ',
    'E': 'ฎ',
    'r': 'พ',
    'R': 'ฑ',
    't': 'ะ',
    'T': 'ธ',
    'y': 'ั',
    'Y': 'ํ',
    'u': 'ี',
    'U': '๊',
    'i': 'ร',
    'I': 'ณ',
    'o': 'น',
    'O': 'ฯ',
    'p': 'ย',
    'P': 'ญ',
    '[': 'บ',
    '{': 'ฐ',
    ']': 'ล',
    '}': ',',
    '\\': 'ฃ',
    '|': 'ฅ',
    'a': 'ฟ',
    'A': 'ฤ',
    's': 'ห',
    'S': 'ฆ',
    'd': 'ก',
    'D': 'ฏ',
    'f': 'ด',
    'F': 'โ',
    'g': 'เ',
    'G': 'ฌ',
    'h': '้',
    'H': '็',
    'j': '่',
    'J': '๋',
    'k': 'า',
    'K': 'ษ',
    'l': 'ส',
    'L': 'ศ',
    ';': 'ว',
    ':': 'ซ',
    '\'': 'ง',
    '"': '.',
    'z': 'ผ',
    'Z': '',
    'x': 'ป',
    'X': ')',
    'c': 'แ',
    'C': 'ฉ',
    'v': 'อ',
    'V': 'ฮ',
    'b': 'ิ',
    'B': 'ฺ',
    'n': 'ท',
    'N': '์',
    'm': 'ท',
    'M': '?',
    ',': 'ม',
    '<': 'ฒ',
    '.': 'ใ',
    '>': 'ฬ',
    '/': 'ฝ',
    '?': 'ฦ',
    ' ': ' ',
}

intents = discord.Intents.default()
intents.message_content = True 

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='ome')
async def on_message(ctx, *messages: str):    
    combined_message = ' '.join(messages)
    try:
        corrected_text = [eng2thai[eng_char] for eng_char in combined_message]
        if corrected_text:
            await ctx.send(f'จริง ๆ ตั้งใจจะพิมพ์ว่า "{"".join(corrected_text)}"')
    except Exception:
        pass

# # If you don't wanna use command (this will automatically convert every characters btw).
# @bot.event
# async def on_message(message: str):    
#     try:
#         corrected_text = [eng2thai[eng_char] for eng_char in message.content]
#         if corrected_text:
#             await message.channel.send(f'จริง ๆ ตั้งใจจะพิมพ์ว่า "{"".join(corrected_text)}"')
#     except Exception:
#         pass


bot.run(TOKEN)




