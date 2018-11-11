import discord
import os


#Variablen
client = discord.Client()
res = []


@client.event
async def on_ready():
    print("Bot is logged in. Running on servers:\n")

    for s in client.servers:
        print(" - %s (%s)" % (s.name, s.id))

@client.event
async def on_message(message):
    if message.content.lower().startswith("?scrim"):
        time = message.content[6:9] + " " + message.content[9:11]
        enemy = message.content[12:]
        await client.delete_message(message)
        emb = discord.Embed(title="-----___**SCRIM**___-----", color=0xbe3c1b)
        emb.set_author(name="MystiK Bot ", icon_url='https://cdn.discordapp.com/attachments/496460929337131008/496798174997118984/Final.png')
        emb.add_field(name="Time: ", value=time, inline=True)
        emb.add_field(name=enemy+" vs", value="MystiK EU A", inline=True)
        emb.set_footer(text="MystiK Bot by Lima")
        await client.send_message(message.channel, embed=emb)


client.run(os.getenv("TOKEN"))
