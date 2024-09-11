import discord
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

# Initialize Discord client with all intents enabled
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Dictionary to store user names
user_names = {}

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello! What is your name?')
    
    elif message.content.startswith('$name '):
        # Extract the name from the message
        user_name = message.content[len('$name '):].strip()
        print(user_name)
        user_names[message.author.id] = user_name
        print(user_names)
        await message.channel.send(f'Nice to meet you, {user_name}!')

    elif message.content.startswith('$greet'):
        # Get the user's name
        user_name = user_names.get(message.author.id, 'there')
        
        # Get the current hour
        current_hour = datetime.now().hour
        
        if 5 <= current_hour < 12:
            greeting = 'Good morning'
        elif 12 <= current_hour < 17:
            greeting = 'Good afternoon'
        else:
            greeting = 'Good evening'
        
        await message.channel.send(f'{greeting}, {user_name}!')
    
