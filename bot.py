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

# list of teachers
list_of_teachers = ["judith", "cynthia"]

#list of thinking
thinking_list = [
"One moment, you wise teacher {teacher_name}, is trying to finish grading your paper, give her a moment to stop what shes doing and answer your question.", 
"Give me a moment, I am trying to find the answer to your question, from the wise {teacher_name}.",
"Stop rushing me, your teacher and I are trying to find the answer to your question.",
]

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

    if len(m) < 2:
        return

    if m[0].lower() != "hi":
        return 
    
    teacher_name = m[1].lower().strip(',!?. :')

    if teacher_name not in list_of_teachers:
        return

    # if only one word is present in the message then say 'yo bestie more words pls'
    if len(m) < 4:
        # Pick a random reply based on random number
        r = random.randrange(1, 4)
        print(f"random number is {r}")
        if r == 1:
            await message.channel.send("yo bestie more words pls")
        if r == 2:
            await message.channel.send("I thus command thee to speak more words to know who to speak to, promptly")
        if r == 3:
            await message.channel.send("I require more words as sustenance")
        return

    
    
    #wait 4 seconds and then send a follow up about waiting
    r = random.randrange(1, len(thinking_list))
    await message.channel.send(thinking_list[r].format(teacher_name=teacher_name))
    
    # take name + everything else!!!!! wowowowowowo
    question = ' '.join(m[2:])
    print (question)

    #run query and get response
    response = str(index.as_query_engine().query(question))
    #run video made from query
    try: 
        success = create_video_from_query(question, teacher_name)
    except Exception as e:
        print("Error in creating video:")
        print(e)
        success = False
    if success == False:
        await message.channel.send("Sorry, Something went wrong. Please try again later.")
        return
    #take the video we create in the other python files and upload to discord
    file = discord.File("output.mp4", filename="output.mp4")
    await message.channel.send("Here's your file!", file=file)


# Retrieve token from the .env file
print("Bot is starting! ----------")
client.run(os.getenv('BOT_TOKEN'))