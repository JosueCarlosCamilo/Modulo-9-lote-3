import discord
from discord.ext import commands
import pyttsx3 #Biblioteca para sintesis de voz
from clima import get_weather
from clima import frase_1 
from clima import get_quote
# Inicializar el bot
intents = discord.Intents.default()
intents.message_content = True  # Para leer mensajes
bot = commands.Bot(command_prefix="!", intents=intents)

#Iniciar sintesis de voz

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

@bot.command()
async def start(ctx):
    await ctx.send("¡Hola! Soy un bot que anuncia el pronóstico del tiempo.")

@bot.command()
async def clima(ctx,*, city:str):
    clima_info = get_weather(city)
    await ctx.send(f"El clima de {city} es de: {clima_info}")
    speak(f"El clima de {city} es de: {clima_info}")

@bot.command()
async def escribe(ctx):
    frase = frase_1()
    await ctx.send(f"Frase del día: {frase}")
    speak(frase)

@bot.command()
async def hablemos(ctx):
    get_quote_info = get_quote()
    await ctx.send(f"Escuche esto:{get_quote_info}")
    speak(get_quote_info)  
    

    
bot.run("TOKEN")
