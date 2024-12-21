from dotenv import load_dotenv
import os

import discord
from discord.ext import tasks
import asyncio


import requests

load_dotenv()

TOKEN = os.getenv("TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        response.raise_for_status()
        return response.json()['ip']
    except requests.RequestException as e:
        print(f"Error fetching public IP: {e}")
        return None
    
intents = discord.Intents.default()
client = discord.Client(intents=intents)

message_to_update = None

# Dynamic content function
def get_dynamic_content():
    # Replace this with your dynamic data logic
    from datetime import datetime
    return f"The current time is: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

@client.event
async def on_ready():
    global message_to_update
    print(f'Logged in as {client.user}')
    
    channel = client.get_channel(CHANNEL_ID)
    if channel is None:
        print("Channel not found! Check your CHANNEL_ID.")
        return

    # Send an initial message
    message_to_update = await channel.send("Initializing...")
    print(f"Message sent in channel: {channel.name}")
    update_message.start()  # Start the updating task

@tasks.loop(seconds=5)  # Update every 5 seconds
async def update_message():
    global message_to_update
    if message_to_update:
        new_content = get_dynamic_content()
        await message_to_update.edit(content=new_content)

@client.event
async def on_message(message):
    # Example: Reset the message if a user types "!reset"
    global message_to_update
    if message.content.lower() == "!reset" and message.channel.id == CHANNEL_ID:
        message_to_update = await message.channel.send("Resetting...")
        print("Message has been reset.")

client.run(TOKEN)