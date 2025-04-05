"""
Text-to-Speech module for language learning application.
Provides functionality to convert text to speech in different languages.
"""
import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Get available voices
voices = engine.getProperty('voices')
"""VOICE"""


def speak(input: str, language='en'):
    """
    Convert text to speech in the specified language.
    
    Args:
        input (str): The text to be converted to speech
        language (str): The language code ('en' for English, 'de' for German)
                        Default is 'en'
    """
    if language == 'de':
        # German voice settings
        engine.setProperty('voice', voices[5].id)
        engine.setProperty('rate', 145)  # Slower rate for German
    elif language == 'en':
        # English voice settings
        engine.setProperty('voice', voices[80].id)
        engine.setProperty('rate', 175)
    else:
        # Default voice settings
        engine.setProperty('voice', voices[138].id)
        engine.setProperty('rate', 175)
    
    # Speak the text and wait until finished
    engine.say(input)
    engine.runAndWait()


engine.stop()
