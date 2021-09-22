import os
import discord
from apscheduler.schedulers.asyncio import AsyncIOScheduler

TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

scheduler = AsyncIOScheduler()
scheduler.start()

@client.event
async def on_ready():
    print(client.guilds)

@client.event
async def on_message(message):
    if message.content.startswith('!remind') and not message.author.bot:
        mentions = message.mentions
        content = message.content.split(' ')
        for user in mentions:
            print(user)
            if content[3] == 's':
                scheduler.add_job(user.send, 'interval' , seconds=int(content[2]), args=[" ".join(content[4:])])
            elif content[3] == 'm':
                scheduler.add_job(user.send, 'interval' , minutes=int(content[2]), args=[" ".join(content[4:])])
            elif content[3] == 'h':
                scheduler.add_job(user.send, 'interval' , hours=int(content[2]), args=[" ".join(content[4:])])
            elif content[3] == 'd':
                scheduler.add_job(user.send, 'interval' , days=int(content[2]), args=[" ".join(content[4:])])
            elif content[3] == 'w':
                scheduler.add_job(user.send, 'interval' , weeks=int(content[2]), args=[" ".join(content[4:])])
        for role in message.role_mentions:
            print(role)
            if content[3] == 's':
                scheduler.add_job(message.channel.send, 'interval' , seconds=int(content[2]), args=[content[1] + ' ' + " ".join(content[4:])])
            elif content[3] == 'm':
                scheduler.add_job(message.channel.send, 'interval' , minutes=int(content[2]), args=[content[1] + ' ' + " ".join(content[4:])])
            elif content[3] == 'h':
                scheduler.add_job(message.channel.send, 'interval' , hours=int(content[2]), args=[content[1] + ' ' + " ".join(content[4:])])
            elif content[3] == 'd':
                scheduler.add_job(message.channel.send, 'interval' , days=int(content[2]), args=[content[1] + ' ' + " ".join(content[4:])])
            elif content[3] == 'w':
                scheduler.add_job(message.channel.send, 'interval' , weeks=int(content[2]), args=[content[1] + ' ' + " ".join(content[4:])])

client.run(TOKEN)

scheduler.shutdown()
