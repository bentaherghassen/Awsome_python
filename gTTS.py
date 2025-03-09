from gtts import gTTS

def text_to_speech():
    """Takes user input for text and language, and saves it as an MP3."""

    text = input("Enter the text you want to be spoken: ")
    language = input("Enter the language code (e.g., en, ar, fr): ")

    try:
        tts = gTTS(text=text, lang=language)
        filename = "user_spoken_text.mp3"
        tts.save(filename)
        print(f"Audio saved as {filename}")  # Inform user where the file is saved.

    except ValueError:
        print("Invalid language code. Please use a valid ISO 639-1 language code.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    text_to_speech()