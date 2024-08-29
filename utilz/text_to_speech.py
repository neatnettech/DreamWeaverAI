import pyttsx3

def text_to_speech(text, filename='output.mp3'):
    engine = pyttsx3.init()
    engine.setProperty('rate', 125)
    engine.setProperty('volume', 1)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.save_to_file(text, filename)
    engine.runAndWait()
    engine.stop()