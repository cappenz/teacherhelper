# Makes a summerizatiopn of an audio file
#

import openai
import whisper
import dotenv
import os
from elevenlabs import set_api_key, generate, play

# take environment variables from .env.
dotenv.load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
elevenlabs_api_key = os.getenv("ELEVENLABS_API_KEY")
set_api_key(elevenlabs_api_key) # set your API key

# This function takes a user prompt and returns a chat response
# It uses the OpenAI API to generate the response
def chat(prompt):
    completion = openai.ChatCompletion.create(
        model="gpt-4", 
        messages=[{"role": "user", "content": prompt}]
    )
    return completion.choices[0].message.content

# This function takes a audio file and returns a text summary
def audiototext(audiofile):   
    model = whisper.load_model("tiny")
    result = model.transcribe(audiofile)
    text = result["text"]
    prompt = f"how could i respond (make this as short one scntence response and in english):{text}"
    result = chat(prompt)
    return result

# Main
result = audiototext("test/Yoko talking .m4a")

#elevenlabs
audio = generate(
  text=result,
  voice="Bella",
  model="eleven_multilingual_v2"
)
 
play(audio)