# Makes a summerizatiopn of an audio file
#

import openai
import whisper

def chat(prompt):
    
    completion = openai.ChatCompletion.create(
        model="gpt-4", 
        messages=[{"role": "user", "content": prompt}]
    )
    return completion.choices[0].message.content


model = whisper.load_model("tiny")
result = model.transcribe("isabelle.aifc")
text = result["text"]

prompt = f"Summarize the following text:{text}"
result = chat(prompt)
print(result)