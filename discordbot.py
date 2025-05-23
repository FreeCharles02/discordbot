import discord  # type: ignore
import os
from dotenv import load_dotenv

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents = intents)

@client.event 
async def on_ready(): 
    print(f'We have logged in as {client.user}')

@client.event 
async def on_message(message): 
    if message.author == client.user: 
        return 
    if "child" in message.content.lower():
        await message.channel.send('https://cdn.discordapp.com/attachments/879979824167407646/1289527288471490590/2024-09-28_10-08-14.mp4?ex=6830475f&is=682ef5df&hm=37c632344b7f758a245930e0c725986401cf76fccd02813f428d7aac28626e88&')
    if message.content.startswith('$hello'):
        await message.channel.send('What\'s up MEXICAN!')
    if "dale" in message.contentlower(): 
        await message.channel.send()
    if "kaguya" in message.content.lower() or "coal" in message.content.lower(): 
        await message.channel.send('https://cdn.discordapp.com/attachments/1173495961419522081/1374992539676839956/niggas_who_say_hood_weeb_on_twitter_summarized.mp4?ex=68301117&is=682ebf97&hm=2b1bf31b6ddc7470efc45a0c5b1b4c56a89f8c7479e9d2cf78600167b52b6462&')

@client.event
async def on_message_delete(message):
    userAuthor = message.author.mention
    await message.channel.send('Nice try SPOOK')
    await message.channel.send(userAuthor + ": " + message.content)


client.run(os.getenv('TOKEN'))