import discord
from discord.ext import commands
import asyncio
from bs4 import BeautifulSoup
from urllib.request import urlopen
import random
from pprint import pprint

#TOKEN = 'MzE5NTI3NTMwMDE5MjkxMTU3.DBRkaA.x9CeoWNl7TGgy_DlQeCh8tXBuSI'
#class FryBot(object):
"""Bot that sends Futurama's Fry memes and quotes."""

bot = commands.Bot(command_prefix=['>> ', '>>bot '], description='this is Funnybot.')
Token = 'MzE5NTI3NTMwMDE5MjkxMTU3.DBRkaA.x9CeoWNl7TGgy_DlQeCh8tXBuSI'


@bot.event
async def on_ready():
    """on ready function"""
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    #await bot.change_presence(status=discord.Status("offline"))




@bot.command()
async def whomade():
    """who made snek?"""
    await bot.say('Mohamed Jmaa made the FunnyBot')

@bot.command()
async def info():
    """info about bot"""
    await bot.say('this bot was made by Mohamed Jmaa, you can use it to: \n - Find some videos\
     on youtube \n - look up for the temperature in your city \n - listen to music on soundcloud \n - find funny picture\
     \n Have fun ')

@bot.command()
async def invite():
    """FunnyBot invite link"""
    await bot.say('to add snekbot to your server click this: https://goo.gl/HTxJWJ')



@bot.command()
async def sourcecode():
    """Funny's source code"""
    await bot.say('https://github.com/SplitPixl/snekbot')



@bot.command(pass_context = True)
async def meteo(ctx, message):
    """get the weather of your city"""
    """:param: ctx"""
    """:param: message"""
    """return meteo url"""

    print(message)
    city = message
    if((message == 'Fribourg') | (message == 'fribourg')):
        city = message+'-fr'
    await bot.say('http://www.prevision-meteo.ch/uploads/widget/%s_0.png' % city)




@bot.command(pass_context = True)
async def clear(ctx, number):
    """Delete all the message"""
    """:param: ctx"""
    """:param: number"""
    """return """
    number = int(number) 
    counter = 0
    async for x in bot.logs_from(ctx.message.channel, limit = number):
        if counter < number:
            await bot.delete_message(x)
            counter += 1
            await asyncio.sleep(1.2) #1.2 second timer so the deleting process can be even




@bot.command(pass_context = True)
async def video(ctx, message):
    """get the youtube video of your choise"""
    """:param: ctx"""
    """:param: message"""
    """return video url"""
    link_list = []
    print ('Searching YouTube for: %s' % message)
    url = "https://www.youtube.com/results?search_query=" + message
    response = urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, "lxml")
    for vid in soup.findAll(attrs={'class': 'yt-uix-tile-link'}):
            link_list.append('https://www.youtube.com' + vid['href'])
    if(len(link_list) >=1):
        random_num = random.randint(0, len(link_list) - 1)
        await bot.say(link_list[random_num])
    else:
        await bot.say("there is no contente for "+message)




@bot.command(pass_context = True)
async def song(ctx, message):
    """get the musique of your choise on soundcloud"""
    """:param: ctx"""
    """:param: message"""
    """return song url"""
    link_list = []
    print ('Searching SoundCloud for: %s' % message)

    url = "https://soundcloud.com/search?q=" + message
    response = urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, "lxml")
    for a in soup.find_all('a', href=True):
        if((a['href'][0:7]) != "/search"):
            if((a['href'][0:7]) != "http://"):
                if ((a['href'][0:7]) != "/popula"):
                        if ((a['href'][0:7]) != "/"):
                            link_list.append("https://soundcloud.com" + a['href'])
    if(len(link_list) >=1):
        random_num = random.randint(0, len(link_list) - 1)
        await bot.say(link_list[random_num])
    else:
        await bot.say("there is no contente for "+message)




@bot.command(pass_context = True)
async def img(ctx, message):
    """get a funny image or gif"""
    """:param: ctx"""
    """:param: message"""
    """return image url"""
    link_list = []

    url = "http://imgur.com/search?q=" + message
    response = urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, "lxml")
    for a in soup.find_all('a', href=True):
        if((a['href'][0:9]) == "/gallery/"):
            link_list.append("https://imgur.com/" + a['href'])
    if(len(link_list) >=1):
        random_num = random.randint(0, len(link_list) - 1)
        await bot.say(link_list[random_num])
    else:
        await bot.say("there is no contente for "+message)


bot.run(Token)
