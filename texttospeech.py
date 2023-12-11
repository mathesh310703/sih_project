import pyttsx3 
text = "cat"
text_speech = pyttsx3.init()
text_speech.say(text)
text_speech.runAndWait()