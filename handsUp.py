# Watkins, jmw4dx
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
#GUILD = os.getenv('DISCORD_GUILD')
numbers = ["1️⃣","2️⃣", "3️⃣", "4️⃣", "5️⃣"]
client = discord.Client()
#print(discord.utils.get(client.emojis, name="\:one:"))

#emoji = ''
#print(client.get_emoji(emoji))

@client.event
async def on_ready():
    #guild = discord.utils.get(client.guilds, name=GUILD)

    print(
        f'{client.user} is activated'
       # f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return


    # print("a" + message.content + "a")
    if type(message.content) != type(""):
        return

    if message.content == '':
        return

    if message.content[0] == "!":
        print("command noticed")
        #await message.channel.send("Command noticed")

    if message.content.lower() in ["!handcheck", "!handscheck", "!handsup", "!handup"]:
        if "prof" not in message.author.nick.lower():
            print("not prof")
            return
        #await message.channel.send("Command noticed")

            #emoji = discord.utils.get(client.get_all_emojis(), name='EmojiName')
        #emoji = "\N{DIGIT ONE}"
        for num in numbers:
            await message.add_reaction(num)

        print("Emotes added")

# @client.event
# async def on_reaction_add(reaction, user):
#     print("reaction:[" + str(reaction) + "]")
#     print(type(reaction))
#     print(type(reaction.emoji))
#     print(user)

client.run(TOKEN)
