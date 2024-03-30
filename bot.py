# Import the required modules
import discord
import os
import random
from time import sleep
from query import create_video_from_query
from discord.ext import commands 
from dotenv import load_dotenv , find_dotenv
load_dotenv(find_dotenv())

# Import frameworks
import os
from llama_index import StorageContext, load_index_from_storage

# load the existing index
storage_context = StorageContext.from_defaults(persist_dir="./storage")
index = load_index_from_storage(storage_context)

# Create a Discord client instance and set the command prefix
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# Event listener for when the bot is ready
@client.event
async def on_message(message):

    # If the message is from the bot itself, ignore it
    if message.author == client.user:
        return
    
    msg = message.content
    print("Received: "+msg)

    s = msg.strip() 
    m = s.split()
   

    print(f"the list is {m}")

    if m[0].lower() != "hi":
        return 
    

    # if only one word is present in the message then say 'yo bestie more words pls'
    if len(m) == 1:
       
        #pick a random reply based on random number
        r = random.randrange(1,4)
        print (f"random number is {r}")
        if r == 1:
            await message.channel.send  ("yo bestie more words pls")
        if r == 2:
            await message.channel.send  ("I thus command thee to speak more words to know who to speak to, promptly")
        if r == 3:
            await message.channel.send  ("I require more words as sustenance")
        return

    teacher_name = m[1].lower()
    
    #wait 4 seconds and then send a follow up about waiting  
    sleep (4)
    message.channel.send("One moment, I am processing your request")
    
    # if the messege starts with cynthia voice cynthia
    if teacher_name == "cynthia":
        question = ' '.join(m[2:])
        print (question)

        #run query and get response
        response = str(index.as_query_engine().query(question))
        #run video made from query
        create_video_from_query(question, "Cynthia")
        #take the video we create in the other python files and upload to discord
        file = discord.File("output.mp4", filename="output.mp4")
        await message.channel.send("Here's your file!", file=file)

    # if the message starts with judith voice judith
    elif teacher_name == "judith":
        question = ' '.join(m[2:])
        print(question)
        #run query and get response
        response = str(index.as_query_engine().query(question))
        #run video made from query
        create_video_from_query(question, "Judith")
        #take the video we create in the other python files and upload to discord
        file = discord.File("output.mp4", filename="output.mp4")
        await message.channel.send("Here's your file!", file=file)

   


# Retrieve token from the .env file
print("Bot is starting! ----------")
client.run(os.getenv('BOT_TOKEN'))