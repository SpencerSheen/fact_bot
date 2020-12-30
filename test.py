import requests
import discord
import os

# i dont think this is being used
import base64
from dotenv import load_dotenv
load_dotenv()

# bot ID
BOT_TOKEN = os.getenv("BOT_TOKEN")
print(BOT_TOKEN)
print("test")

# not being used
def get_token():
  data = {
    'grant_type': 'client_credentials',
    'scope': 'identify connections'
  }
  headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
  }
  r = requests.post('%s/oauth2/token' % API_ENDPOINT, data=data, headers=headers, auth=(CLIENT_ID, CLIENT_SECRET))
  r.raise_for_status()
  return r.json()

# not being used
def bare_get():
    r = requests.get('%s/channels/385910497741897750/messages' % API_ENDPOINT)
    return r

# retrieves fact from factgenerator link
def fact_get():
    r = requests.get('http://randomfactgenerator.net/')
    result_str = r.text

    start_index = result_str.find("<div id=\'z\'>")
    if start_index == -1:
        return "Fact cannot be generated"

    end_index = result_str.find("<br/>", start_index)

    if end_index == -1:
        return "Fact cannot be generated"

    return result_str[start_index+len("<div id=\'z\'>"):end_index]


client = discord.Client()

@client.event
async def on_message(message):
    # only replies to '!fact'
    if message.content == "!fact":
        await message.channel.send(fact_get())

client.run(BOT_TOKEN)
