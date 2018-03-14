import discord
import asyncio
import os
import requests

client = discord.Client()

@client.event
async def on_ready():
    print("Bot: " + client.user.name+" has loaded successfully.")

@client.event
async def on_message(message):
    if message.content.startswith("fn "):
        name = message.content[3:]
        url = "https://api.fortnitetracker.com/v1/profile/pc/" + name
        headers = {"TRN-Api-Key" : "8db9d646-4be1-438e-b4da-c8088cbdfa8a"}
        print(name)
        jsonB = requests.get(url,headers=headers)
        json_data = jsonB.json()
        print(json_data.get("lifeTimeStats"))
        for item in json_data.get("lifeTimeStats"):
            if item['key']=="Wins":
                wins = item['value']
            if item['key']=="K/d":
                kd = item['value']
            if item['key']=="Win%":
                winpercent = item['value']
            if item['key']=='Kills':
                kills = item['value']
            if item['key']=='Matches Played':
                matches = item['value']

        await client.send_message(message.channel,'''```
'''+name+''':

Wins: '''+wins+'''
K/D: '''+kd+'''
Kills: '''+kills+'''
Win%: '''+winpercent+'''
Matches Played: '''+matches+'''

Stats brought to you by shtabbbe.
```''')
client.run("NDIyODExNzgyMTM1MTUyNjQw.DYjpXw.CtbkPdR-r8EHrkdniDXQRpRgc-s")
