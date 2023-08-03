import discord
from key import token

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
TOKEN = token.get("TOKEN")

@client.event
async def on_ready():
    print(f'{client.user} está online!')

client.run(TOKEN)