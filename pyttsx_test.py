import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Text to be spoken
text = input('Type the text to be spoken')

# Speak the text
engine.say(text)
engine.runAndWait()