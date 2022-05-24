import discord
import random
import asyncio

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('Jogo'):
            await message.channel.send('Escolha um numero de 1 a 10.')

            def is_correct(m):
                return m.author == message.author and m.content.isdigit()

            answer = random.randint(1, 10)

            try:
                guess = await self.wait_for('message', check=is_correct, timeout=5.0)
            except asyncio.TimeoutError:
                return await message.channel.send('Desculpe, demorou muito era {}.'.format(answer))

            if int(guess.content) == answer:
                await message.channel.send('Acertou!')
            else:
                await message.channel.send('Oops. É {}.'.format(answer))

client = MyClient()
client.run('token')
