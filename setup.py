#
# creates a loop to go though audio files in a folder and convert them to text 
#
import os
import whisper

audiodir = "audio"
textdir = "transcripts"

print("Converting audio to text")
print("Audio directory: " + audiodir)

for filename in os.listdir(audiodir):
    if filename.endswith(".m4a"):
        f = os.path.join(audiodir, filename)
        print("   "+f)

        # Use whisper to convert audio to text
        model = whisper.load_model("tiny")
        result = model.transcribe(f,fp16=False)
        text = result["text"]

        with open(os.path.join(textdir, filename + ".txt"), "w") as text_file:
            text_file.write(text)
        continue
    else:
        continue