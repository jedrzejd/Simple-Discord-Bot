import os
import random
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    odp = [
        'W domu cie nie biją?',
        'Jak ty chyba nietrześwy',
        'Co się lampisz gruby',
        'Jak ci wyjebie to ci się orężada z komuni odbije',
        'No debil no',
        'W domu cie nie biją?',
        'Zara w pinczakersa dostaniesz',
        'Oddawaj buty frajerze',
        'Co ty chłopie odwalasz',
        'Tobie to już nic nie pomoże',
        'Kruca bomba ty głupi czy głupi',
        'Do roboty jebane nieroby',
        'No i co taki koksu z ciebie',
        'Zamiast się uczysz to w te głupoty się bawisz',
        'Siedzisz na stojąco i jeszcze masz pretensje',
        ':slight_smile:',
        'Uuu je jam kebebe jem\nUuu jeee ale pyszny jeeest',
        'Ty to byś tylko intepretowane by było',
        'Po chuj się na wakacje w gips ładujesz',
        'Daleko nie uciekniesz',
        'Potrzymaj mi piwo',
        'Słuchaj no studenciku jebany\n Jeszcze jeden taki numer i widzimy się u dziekana'
    ]

    reply = random.choice(odp)
    await message.channel.send(message.author.mention)
    await message.channel.send(reply)

client.run(TOKEN)