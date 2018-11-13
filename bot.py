import discord
import os

# Variablen
client = discord.Client()
codelist1 = []
codelist2 = []
codelist3 = []
codelist4 = []
deniedlist1 = []
deniedlist2 = []
deniedlist3 = []
deniedlist4 = []

@client.event
async def on_ready():
    print("Bot is logged in. Running on servers:\n")

    for s in client.servers:
        print(" - %s (%s)" % (s.name, s.id))


@client.event
async def on_message(message):
    if message.content.lower().startswith("?scrim"):
        time = message.content[6:9] + " " + message.content[9:11]
        code =  message.content[11:13]
        enemy = message.content[13:]
        await client.delete_message(message)
        emb = discord.Embed(title="-----___**SCRIM**___-----", color=0xbe3c1b)
        emb.set_author(name="MystiK Bot ",
                       icon_url='https://cdn.discordapp.com/attachments/496460929337131008/496798174997118984/Final.png')
        emb.add_field(name="Time: ", value=time + " UK", inline=True)
        emb.add_field(name=enemy + " vs", value="MystiK EU A", inline=True)
        emb.set_footer(text="MystiK Bot by Lima")
        await client.send_message(message.channel, embed=emb)
        stringcode = str(code)
        await client.send_message(message.channel, "Are you available? ?a / ?d + Code:"+stringcode)

    if message.content.lower().startswith("?a"):
        vcode = int(message.content[2:])
        if vcode == 1:
            codelist1.append(message.author.name)
        elif vcode == 2:
            codelist2.append(message.author.name)
        elif vcode == 3:
            codelist3.append(message.author.name)
        elif vcode == 4:
            codelist4.append(message.author.name)

    if message.content.lower().startswith("?d"):
        dcode = int(message.content[2:])
        if dcode == 1:
            deniedlist1.append(message.author.name)
        elif dcode == 2:
            deniedlist2.append(message.author.name)
        elif dcode == 3:
            deniedlist3.append(message.author.name)
        elif dcode == 4:
            deniedlist4.append(message.author.name)

    if message.content.lower().startswith("?remove"):
        deletecode = int(message.content[7:])
        if deletecode == 1:
            codelist1.clear()
            deniedlist1.clear()
        elif deletecode == 2:
            codelist2.clear()
            deniedlist2.clear()
        elif deletecode == 3:
            codelist3.clear()
            deniedlist3.clear()
        elif deletecode == 4:
            codelist4.clear()
            deniedlist4.clear()

    if message.content.lower().startswith("?show"):
        showcode = int(message.content[5:])
        if showcode == 1:
            await client.send_message(message.channel,"Availabel:")
            await client.send_message(message.channel,codelist1)
            await client.send_message(message.channel, "Denied:")
            await client.send_message(message.channel, deniedlist1)
        elif showcode == 2:
            await client.send_message(message.channel,"Availabel:")
            await client.send_message(message.channel,codelist2)
            await client.send_message(message.channel, "Denied:")
            await client.send_message(message.channel, deniedlist2)
        elif showcode == 3:
            await client.send_message(message.channel,"Availabel:")
            await client.send_message(message.channel,codelist3)
            await client.send_message(message.channel, "Denied:")
            await client.send_message(message.channel, deniedlist3)
        elif showcode == 4:
            await client.send_message(message.channel,"Availabel:")
            await client.send_message(message.channel,codelist4)
            await client.send_message(message.channel, "Denied:")
            await client.send_message(message.channel, deniedlist4)

    if message.content.lower().startswith("?hello"):
        a =  message.author.top_role.position
        await client.send_message(message.channel, a)

    if message.content.lower().startswith("?game"):
        time = message.content[5:8] + " " + message.content[8:10]
        enemy = message.content[11:]
        await client.delete_message(message)
        emb = discord.Embed(title="-----___**GAME**___-----", color=0xbe3c1b)
        emb.set_author(name="MystiK Bot ",
                       icon_url='https://cdn.discordapp.com/attachments/496460929337131008/496798174997118984/Final.png')
        emb.add_field(name="Time: ", value=time + " UK", inline=True)
        emb.add_field(name=enemy + " vs", value="MystiK EU A", inline=True)
        emb.set_footer(text="MystiK Bot by Lima")
        await client.send_message(message.channel, embed=emb)

    if message.content.lower().startswith("?help"):
        embed = discord.Embed(title="Command list", description="Commands for MystiK Bot", color=0xb02222)
        embed.set_author(name="MystiK Bot",icon_url='https://cdn.discordapp.com/attachments/496460929337131008/496798174997118984/Final.png')
        embed.add_field(name="Scrim:", value="?scrim [ Time ] [ Code ] [ Enemy ]", inline=False)
        embed.add_field(name="Game:", value="?game [ Time ] [ Code ] [ Enemy ]", inline=False)
        embed.add_field(name="Available:", value="?a [ Scrim/Game Code ]", inline=False)
        embed.add_field(name="Denied:", value="?d [ Scrim/Game Code ]", inline=False)
        embed.add_field(name="Show:", value="?show [ Scrim/Game Code ]", inline=True)
        embed.add_field(name="Remove:", value="?remove [ Scrim/Game Code ]", inline=False)
        embed.set_footer(text="MystiK Bot by Lima")
        await client.send_message(message.channel, embed = embed)
        
   if message.content.lower().startswith("?annoy"):
        id = "<@369448048654548994>"
        for i in range(15):
            await client.send_message(message.channel,"Britons")

client.run(os.getenv("TOKEN"))
