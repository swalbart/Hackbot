import os
import discord

client = discord.Client()
print("Hello there")

# useful shortcut variables
rt = "\n"   # rt = return

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="videos"))

@client.event
async def on_message(message):
    # make sure to not get triggered by own messages
    if message.author == client.user:
        return
    # in order to be able to let the bot read the content of the message,
    # you need to enable the "MESSAGE CONTENT INTENT" in the discord developer portal
    m = message.content
    m = m.lower()
    output = ""
    
    if m.startswith("test"):
        output = "hello world"
    #elif m.startswith(""):
    #    output = ""
    #...

    # error output
    if output == "":
        output = "404 Kein Anschluss unter dieser Nummer"
    # send the output to discord
    await message.channel.send(output)


token = "mytoken"
if(len(token)<59):
    # check for token in token.txt
    token_path = 'token.txt'
    if os.path.exists(token_path):
        # token exits in token.txt
        with open(token_path, 'r') as file:
            token = file.read().replace('\n', '') 
    else:
        # no token found
        noTokenText = "Zur Information:"
        noTokenText+= rt+"Um sicherzustellen, dass der Token nicht im Quellcode von Hackbott landet, wird er in einer separaten Datei names token.txt im gleichen Ordner gespeichert."
        noTokenText+= rt+"Der Token ist im discord developer portals zu finden."
        noTokenText+= rt+"Dies ist ein einmaliger Prozess, sodass beim erneuten Starten des Bots der Token automatisch aus der token.txt ausgelesen wird."
        token = input("Discord token:")
        with open(token_path, 'w') as file:
            file.write(token)
client.run(token)