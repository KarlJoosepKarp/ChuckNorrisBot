import requests
import discord
from discord.ext import commands


names = ["chuck", "norris", "chucknorris", "chuck norris"]
Client = discord.Client()
bot = commands.Bot(command_prefix="!")


def get_joke():
    """Get joke via api and from json"""
    joke = requests.get("https://api.chucknorris.io/jokes/random").json()
    return joke["value"]


@bot.event
async def bot_ready():
    print("Bot is ready for action")


@bot.event
async def on_message(message):
    print("okei")
    if message.content.lower() in names:
        await bot.send_message(message.channel, get_joke())

bot.run("NTM3MzQ2MTg5MDY3MDI2NDcw.Dyj6vQ.T4UTXoc_CirpcxElJ9QOKOx6V4Q")
