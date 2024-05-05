## teacherhelper

AI helper for teachers.

With this project, you can ‘ask your teacher’ a question through Discord at any time and receive an answer in video format as if the teacher responded. We use AI to generate a reply that is based on transcripts of the teacher's past lessons.

https://github.com/cappenz/teacherhelper/assets/143547735/1d142150-135f-4634-88c6-ef83509d21c7


## How It Works
Over the last few months, I recorded audio files from lessons in Cynthia’s and Judith’s classes, transcribed them, divided the transcripts into chunks,  and stored them in a database (Steps A-G in the diagram below).

When a user asks a relevant question on Discord (starting with “Hi Cynthia” or “Hi Judith”) the code searches the database of embeddings to find the chunks with the highest similarity (Steps 1-3). It then provides Chat GPT with these chunks to write the answer and uses ElevenLabs with the right teacher’s voice model (Steps 4-6). Then the audio is combined with a photo of the teacher and lip movements are added. This makes it look as if the teacher is answering the question (Steps 6-7). Then the video is sent to the user who can watch the AI teacher answer the questions on Discord. (Step 8) 
## Tools Used
-Whisper
  Whisper is a powerful model developed by OpenAI that transcribes spoken language into text. It is the first step in processing the input by converting spoken questions into a written format that other models can understand.

-Llama Index and GPT
  Llama Index works alongside GPT (Generative Pre-trained Transformer) to enhance the transcriptions provided by Whisper. These models add necessary context and generate answers that are not only accurate but also pedagogically aligned with educational objectives.

-Eleven Labs
  Eleven Labs technology is used to convert the text responses generated by GPT into high-quality, lifelike audio. This makes the responses   more engaging and easier for students to understand, mirroring a natural teacher-student interaction.

-Discord
  Discord acts as the user interface where students can submit their questions and receive answers. It is crucial for interaction   management, providing a familiar and accessible platform for users to engage with AI Teacher Helper.

-GitHub
  All source code, documentation, and updates are hosted on GitHub. This allows for collaborative development and easy access to the project's resources for users and developers interested in the project’s methodology or wishing to contribute.
  
  <img width="1279" alt="Screenshot 2024-05-04 at 1 19 14 PM" src="https://github.com/cappenz/teacherhelper/assets/143547735/d158f8dc-fbc4-4ea1-8737-862699291870">

## Example

If I ask the question ‘Hi Cynthia, Tell me about Alexander the Great’ it will first say one of 3 acknowledgment phrases like ‘Stop rushing me, your teacher and I are trying to find the answer to your question.’ then it will prepare the file and say ‘Here's your file!’ and send you the file!

The file will be a video of Cynthia saying “Alexander the Great was a historical figure who traveled along the Silk Road and was responsible for opening trade routes. He is known for his conquests and for spreading Greek culture throughout the regions he conquered.”

## Thanks

- Marco Mascorro: He was my mentor for this project and helped me with the code and helped me with the ideas around this project, plus helped me make answers for questions people might have when I present it.
- Both my teachers gave me content for the audio files and let me make them the guinea pigs for this.
