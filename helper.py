# Makes a summerizatiopn of an audio file
#

import openai
import whisper
import dotenv
import os

# take environment variables from .env.
dotenv.load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# This function takes a user prompt and returns a chat response
# It uses the OpenAI API to generate the response
def chat(prompt):
    completion = openai.ChatCompletion.create(
        model="gpt-4", 
        messages=[{"role": "user", "content": prompt}]
    )
    return completion.choices[0].message.content

model = whisper.load_model("tiny")
result = model.transcribe("test/isabelle.aifc")
text = result["text"]
print("\n--- Whisper Transcript -----------------")
print(text)

prompt = f"What is she saying and how could i respond:{text}"
result = chat(prompt)
print("\n--- LLM Summary -----------------")
print(result)