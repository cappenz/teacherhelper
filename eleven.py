from elevenlabs import generate, play

audio = generate(
  text="Hello! 你好! Hola! नमस्ते! Bonjour! こんにちは! مرحبا! 안녕하세요! Ciao! Cześć! Привіт! வணக்கம்!",
  voice="Charlotte Appenzeller",
  model="eleven_multilingual_v2"
)

play(audio)