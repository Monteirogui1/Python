import os
import random
from discord.ext import commands
import discord
from dotenv import load_dotenv
import asyncio

load_dotenv()
client = discord.Client()
bot = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print(f'{client.user.name} Começouu!')


@client.event
async def on_member_join(member):
    await member.create()
    await member.channel.send(f'Fala ae, {member.name}, pronto para tiltar?!')


@bot.command(name='Jogo', help='Escolha um numero de 1 a 10')
async def escolha(ctx):
    answer = random.randint(1, 10)

    if answer == escolha:
        await ctx.send('Acertou o numero!')
    else:
        await ctx.send(f'Errou, numero: {answer}')


@bot.command(name='Bot', help='Perguntas: Responde a uma pergunta(Respostas Padrões)')
async def perguntas(ctx):
    resposta = ['Não respondo a isso', 'Sim', 'As vezes', 'Não', 'Claro', 'NUNCA!', 'Um dia talvez',
                'A resposta está dentro de ti', 'Mais ou menos', 'Uma Bosta', 'Podia ser pior', 'Tilta não!']

    r = random.choice(resposta)
    await ctx.send(r)


@bot.command(name='Dado', help='Dado: Joga um dado de 6 Lados!')
async def jogar(ctx):
    dado = [str(random.randint(1, 6))]
    await ctx.send(''.join(dado))


@bot.command(name='Pedro', help='Xinga o pedro')
async def xinga(ctx):
    resposta = 'Da uma  !!'

    await ctx.send(resposta)


bot.run('')

