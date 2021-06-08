import discord 
import requests 
import json
import os 

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('hello'):
        await message.channel.send('go away')

@client.event
async def on_message(welcome):
    if welcome.author == client.user:
        return 
    if welcome.content.startswith('how are you'):
        await welcome.channel.send('please stop talking to me i hate people')

def get_quotes():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" +json_data[0]['a']
    return (quote)

@client.event
async def on_message(quote):
    if quote.author == client.user:
        return
    if quote.content.startswith('$inspire'):
        happy_message = get_quotes()
        await quote.channel.send(happy_message)
        
client.run("")
