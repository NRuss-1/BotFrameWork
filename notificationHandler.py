import pandas as pd
import numpy as np
from discord import Intents, Client, Message 
import discord.utils


def make_message(island):
        return f"Your Assigned island is {island}"
    
async def sendDM(member, bot_message):
    try:
        await member.send(bot_message)
    except Exception as e:
        print(f"Error sending message to {member}: {e}")
    

async def send_teams_messages(message:Message):
    Team1 = discord.utils.get(message.guild.roles, name = "Team 1: Duneus Maraudeus")
    Team2 = discord.utils.get(message.guild.roles, name = "Team 2: cute kitty cats")
    Team3 = discord.utils.get(message.guild.roles, name = "Team 3: Cursed Pirates")
    Team4 = discord.utils.get(message.guild.roles, name = "Team 4: Celtic Goblins")
    Team5 = discord.utils.get(message.guild.roles, name = "Team 5: Los Goats")
    Team6 = discord.utils.get(message.guild.roles, name = "Team 6: (Team name to be decided later)")
    Team7 = discord.utils.get(message.guild.roles, name = "Team 7: TWIN")
    Team8 = discord.utils.get(message.guild.roles, name = "Team 8: Mrs Puff’s Boating School")
    Team9 = discord.utils.get(message.guild.roles, name = "Team 9: Scallywag Special")

    ice_man = discord.utils.get(message.guild.roles, name = "Ice Man")
    temp_man = discord.utils.get(message.guild.roles, name = "temp")

    members = message.channel.guild.members
    
    for member in members:
        
        if Team1 in member.roles:
            botdm = make_message('Unassigned')
            await sendDM(member, botdm)
            
        elif Team2 in member.roles:
            botdm = make_message('Unassigned')
            await sendDM(member, botdm)
        
        elif Team3 in member.roles:
            botdm = make_message('Unassigned')
            await sendDM(member, botdm)
        
        elif Team4 in member.roles:
            botdm = make_message('Unassigned')
            await sendDM(member, botdm)
        
        elif Team5 in member.roles:
            botdm = make_message('Unassigned')
            await sendDM(member, botdm)
        
        elif Team6 in member.roles:
            botdm = make_message('Unassigned')
            await sendDM(member, botdm)

        elif Team7 in member.roles:
            botdm = make_message('Unassigned')
            await sendDM(member, botdm)

        elif Team8 in member.roles:
            botdm = make_message('Unassigned')
            await sendDM(member, botdm)

        elif Team9 in member.roles:
            botdm = make_message('Unassigned')
            await sendDM(member, botdm)
        


