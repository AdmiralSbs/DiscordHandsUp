# Watkins, jmw4dx
import os
import shlex
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
#GUILD = os.getenv('DISCORD_GUILD')
numbers = ["1️⃣","2️⃣", "3️⃣", "4️⃣", "5️⃣"]
numbers10 = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟']
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

    words = message.content.split(" ")
    command = words[0]

    if command[0] == "!":
        print("command noticed")
        #await message.channel.send("Command noticed")

    if command.lower() in ["!handcheck", "!handscheck", "!handsup", "!handup"]:
        if "prof" not in message.author.display_name.lower():
            print("not prof")
            return
        #await message.channel.send("Command noticed")

            #emoji = discord.utils.get(client.get_all_emojis(), name='EmojiName')
        #emoji = "\N{DIGIT ONE}"
        for num in numbers:
            await message.add_reaction(num)

        print("Emotes added")

    if command.lower() in ["!poll"]:
        items = (shlex.split(message.content))[1:]
        title = items[0]
        if len(items) == 1:
            options = ["Yes", "No"]
        elif len(items) == 2:
            options = items
            title = ""
        else:
            options = items[1:]
        if len(options) > 10:
            options = options[0:10]
        channel = message.channel
        try:
            await message.delete()
        except discord.NotFound:
            pass
        text = ["Poll:"]
        if title != "":
            text += [title]
        for i in range(len(options)):
            text += [numbers10[i] + ": " + options[i]]
        newMessage = await channel.send("   ".join(text))
        for i in range(len(options)):
            await newMessage.add_reaction(numbers10[i])


# @client.event
# async def on_reaction_add(reaction, user):
#     print("reaction:[" + str(reaction) + "]")
#     print(type(reaction))
#     print(type(reaction.emoji))
#     print(user)

client.run(TOKEN)
