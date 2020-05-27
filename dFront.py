import discord
import os
from main_hatBot import *

# GetToken
text_file = open("token.txt", "r")
token = text_file.readlines()[0]
client = discord.Client()


@client.event
async def on_ready():
    activity = discord.Game(name="Do you want a hat?", type=3)
    await client.change_presence(status=discord.Status.idle, activity=activity)
    print("[INFO] hatBot is ready!")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if ".hat" in message.content.lower():
        hatTypes = getHatTypes()
        hatType = "marisa"
        for type in hatTypes:
            if type in message.content.lower():
                hatType = type
                print("[INFO] type is {}".format(type))
                break
        if "-c" in message.content.lower():
            yOffset = False
            xOffset = False
            scale = False
            for s in message.content.lower().split():
                woStuff = s.replace('-', '')
                woStuff = woStuff.replace('.', '')
                print(s)
                print(woStuff)
                if woStuff.isdigit():
                    if not(xOffset):
                        xOffset = s
                    elif not(yOffset):
                        yOffset = s
                    elif not(scale):
                        scale = s
        else:
            xOffset = 0
            yOffset = 0
            scale = 1


        print("yOffset: {}".format(yOffset))
        print("xOffset: {}".format(xOffset))
        print("scale:   {}".format(scale))

        user = message.author.name
        avatarUrl = message.author.avatar_url
        print(avatarUrl)
        print("[INFO] Request by {}!".format(user))
        await message.channel.send('Here comes a hat for you {} !'.format(user))
        filepath = getImage(avatarUrl, user, hatType, int(yOffset), int(xOffset), scale)
        image = discord.File(filepath, filename="result.png")
        await message.channel.send(file=image)

    if ".help" in message.content.lower():
        await message.channel.send("""```Help
        Syntax:    
            .hat <type> [-c <X-offset>(0) <Y-offset>(0) <scale>(1)]
        Types:
            marisa, doremy, clownpiece, flandre, alice, reimu, remilia, keine, eiki, koishi, tenshi, patchouli, zun, yuyuko, rin, mokou
        Example:
            .hat doremy -c 10 50 50```
        """)

client.run(token)

