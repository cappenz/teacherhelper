#
# Function to read a reply in the teachers voice
#

import os
from elevenlabs import set_api_key, generate, play

import dotenv
dotenv.load_dotenv()
elevenlabs_api_key = os.getenv("ELEVENLABS_API_KEY")
set_api_key(elevenlabs_api_key) # set your API key

# Function to generate audio from text 
#Cynthia Kosut,Judith Worrall

def read_reply(response): 
    audio = generate(
        text=response,
        voice="Cynthia Kosut",
        model="eleven_multilingual_v2"
    )
    play(audio) # plays the audio

if __name__ == "__main__":
    read_reply("Hi there!")


