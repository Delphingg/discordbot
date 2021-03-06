import random
import asyncio
import aiohttp
import json
from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ("?", "!")
TOKEN = "NDg1NTAzMzQ5NTE3NzEzNDE4.Dn6Fjg.OnCymgrFXIFAvOLMJKQBPfNCDzY"  # Get at discordapp.com/developers/applications/me

client = Bot(command_prefix=BOT_PREFIX)



@client.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'Определённо нет',
        'Наверное нет',
        'Сложно сказать',
        'Возможно',
        'Определённо да',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)


@client.command()
async def квадрат(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " в квадрате " + str(squared_value))


@client.command()
async def bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        await client.say("Bitcoin price is: $" + response['bpi']['USD']['rate'])


async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)

client.run('NDg1NTAzMzQ5NTE3NzEzNDE4.Dn6Fjg.OnCymgrFXIFAvOLMJKQBPfNCDzY')        
