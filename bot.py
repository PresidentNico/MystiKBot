import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print("Bot is logged in. Running on servers:\n")

    for s in client.servers:
        print(" - %s (%s)" % (s.name, s.id))


@client.event
async def on_message(message):

    #SCRIM

    if message.content.lower().startswith("?scrim"):
        global msgdate
        msgdate = await client.send_message(message.channel,"Date? ?date 03-05")
        await client.delete_message(message)


    #DATE

    if message.content.lower().startswith("?date"):
        global day, month,timestamp, channel_del, msgtime
        await client.delete_message(msgdate)
        day = message.content[6:8]
        month = message.content[9:11]
        timestamp = message.timestamp
        channel_del = message.channel
        msgtime = await client.send_message(message.channel, "Time? ?time 05:23 PM")
        await client.delete_message(message)


        #TIME

    if message.content.lower().startswith("?time"):
        global hour,minute,meridiem, msgenemy
        await client.delete_message(msgtime)
        hour = message.content[6:8]
        minute = message.content[9:11]
        meridiem = message.content[12:14]
        msgenemy = await client.send_message(message.channel,"Enemy? ?enemy PENTA")
        await client.delete_message(message)



        #ENEMY

    if message.content.lower().startswith("?enemy"):
        enemy = message.content[6:]
        time = hour + ":" + minute + " " + meridiem
        date = day + "." + month
        await client.delete_message(message)
        await client.delete_message(msgenemy)
        #stime = str(timestamp)
        #minu = stime[14:16]
        #intminu = int(minu)
        #finaltime = timestamp.replace(minute=intminu-2)
        #await client.purge_from(channel_del, after= finaltime)
        embed = discord.Embed(title="---___**SCRIM**___---")
        embed.set_author(name="MystiK Bot",
                         icon_url='https://cdn.discordapp.com/attachments/496460929337131008/496798174997118984/Final.png')
        embed.add_field(name="Date and Time:", value=date + " " + time, inline=True)
        embed.add_field(name="Enemy:", value=enemy, inline=True)
        embed.set_footer(text="MystiK Bot by Lima")
        await client.send_message(message.channel, embed=embed)



    if message.content.lower().startswith("?annoy"):
        id = "<@369448048654548994>"
        for i in range(15):
            await client.send_message(message.channel,id)
