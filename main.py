from dotenv import load_dotenv
import os

import discord
from discord.ext import tasks
import asyncio

from get_ip import get_public_ip
from get_running_containers import get_running_containers

load_dotenv()

TOKEN = os.getenv("TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
    
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
    print(client.guilds[0].name)
    global message_to_update
    print(f'Logged in as {client.user}')
    
    channel = client.guilds[0].get_channel(1319983304488910870)

    if channel is None:
        print("Channel not found! Check your CHANNEL_ID.")
        return

    # Send an initial message
    message_to_update = await channel.send("Initializing...")
    print(f"Message sent in channel: {channel.name}")
    update_message.start()  # Start the updating task

@tasks.loop(seconds=5)  # Update every 60 seconds
async def update_message():
    print("Updating message...")
    global message_to_update
    if message_to_update:
        
        new_content = get_public_ip()
        await message_to_update.edit(content=new_content)

@client.event
async def on_message(message):
    # Example: Reset the message if a user types "!reset"
    global message_to_update
    if message.content.lower() == "!reset" and message.channel.id == CHANNEL_ID:
        message_to_update = await message.channel.send("Resetting...")
        print("Message has been reset.")

client.run(TOKEN)