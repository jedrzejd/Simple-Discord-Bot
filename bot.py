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
        'ja pinczole\njam kebabe jem\nu je\nale pyszny jee st jam kebeb zjadany jee',
        'Ty to byś by tylko intepretowane by było',
        'Po chuj się na wakacje w gips ładujesz',
        'Daleko nie uciekniesz',
        'Potrzymaj mi piwo',
        'Słuchaj no studenciku jebany\n Jeszcze jeden taki numer i widzimy się u dziekana',
        'Nie pinczol zjedz kapote',
        'Michał ty byś tylko pierdolony skurwysynie',
        'Serek topiony jest jak widelec, samemu nic nim nie zdziałasz',
        'Zawsze miałeś łeb do interesów',
        'Ty chyba nie podczakres z pełną rurą',
        'Co to za trojan?',
        'Łaska\nŁaska\nŁaska\nŁaska\nŁaska\nKurwa\nŁaska\nKurwa\nŁaska\nKurwa\nLaska',
        'Człowieku nie bądz takim materialistą\n',
        'Trzeba się wyluzować',
        'Spal se gibczana',
        'Co to za wirus',
        'Kolega chyba po podpiwku Jędrzeju',
        'Dzisiaj krucjata kurcze będzie\nKurcze krucha\nBędzie\nJa brutus pod Wiedniem wygramy z tymi podpiekami z b1',
        'ja bym się kurcze zastanowił zanim pomyslał 2 razy',
        'Ty jesteś super wojtach',
        'Ty nie profokuj nadskurczynekersa żeby im przypadkiem żeby się nie poskładali jak parapety na wietrze',
        'Ja by im bana zasadził ze nie zapowiadali by się podczakersy',
        'ale podpiwek\njest jak podpiwek\nkazdy ma własny\njak nadpiwek od biedy\nwalne koło\nale tylko od biedy',
        'Więc cytując "I ten co kebab został zabrany jest bardziej szcześliwy od drugiego"\nchodzi o to że\nod tego co zapinczilil kebaba dla drugiego jest teraz mniej szcześliwy od drugiego nawet gdy ma ten 2 wypinczoliste kebaby ale ten co już ma minus jednego kebaba ma pełny portwel i może kupić dużo pysznych kebabów który będę lepsze i będzie ich wiecej niż te które i będzie ich wiecej niż te które ma ten pierwszy\nCzy to takie trudne',
        'No bo jak przestanie się jeść zwierząt co nie to kurcze będzie ich zadużo i wtedy to same zaczną się zjadać wieć co zwierzęta też mają być wege?',
        'Drugi wege kurcze jak ci schabowym przyjade to kurcze mieso się nauczysz wpinczalać jeszcze szybciej niż głodny rufus wiec uważaj',
        'ty chyba pijany albo pajany albo pjany albo pjany albo pjany',
        'Dziewiąty grosz stryjowi, nielicho się narobił.\nCo to za wegetarianin co wpierdala schabowe',
        'Morfeusz król dupeczek?',
        'haha\nale kurne smieszne\nja pinczole',
    ]

    reply = random.choice(odp)
    await message.channel.send(message.author.mention)
    await message.channel.send(reply)

client.run(TOKEN)