from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import getResponse
from notificationHandler import send_teams_messages
import discord.utils

load_dotenv()
token : Final = os.getenv('DISCORD_TOKEN')


intents = Intents.default()
intents.message_content = True
intents.members = True
client = Client(intents = intents)

async def send_message(message, user_message):
    if not user_message:
        print("Message is empty")
        return
    
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]
    
    staff_role = discord.utils.get(message.guild.roles, name = "Tournament Staff")
    if staff_role in message.author.roles: 
        try:
            if (user_message.lower() == 'assignteams'):
                await send_teams_messages(message)
            response = getResponse(user_message)
            if is_private:
                await message.author.send(response)
                await message.channel.send("Done!") 
        except Exception as e:
            print(e)


@client.event
async def on_ready():
    print(f'{client.user} is now running')


@client.event
async def on_message(message):
    if message.author == client.user:
        return 
    
    username = str(message.author)
    user_message = message.content
    channel = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    
    await send_message(message, user_message)

def main():
    client.run(token)

if __name__ == '__main__':
    main()