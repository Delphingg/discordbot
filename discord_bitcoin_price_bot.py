import random
import asyncio
import aiohttp
import json
from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ("?", "!")

client = Bot(command_prefix=BOT_PREFIX)
bot = commands.Bot(command_prefix='?', '!')

@client.command()
async def bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        await client.say("Bitcoin price is: $" + response['bpi']['USD']['rate'])
        
@client.command(name='Шар',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['Шарик', '8Шарик', '8Шар', 'шар', '8шарик', '8шар', 'ШАРИК', '8ШАРИК', '8ШАР', 'ШАР'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'Определённо нет',
        'Вероятно, нет',
        'Сложно сказать',
        'Возможно',
        'Определённо да',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)
    
    
    
@client.command()
async def square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))



client.run("NDg1NTAzMzQ5NTE3NzEzNDE4.Dm0jJw.RjBFbnkIQEcPE-zpP6EHTyquzoQ")

