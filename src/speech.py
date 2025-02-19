import pyttsx3
import threading

engine = pyttsx3.init()
engine.setProperty('voice', engine.getProperty('voices')[1].id)

def speak(text):
    """Speak text asynchronously."""
    def _speak():
        engine.say(text)
        engine.runAndWait()
    threading.Thread(target=_speak, daemon=True).start()
