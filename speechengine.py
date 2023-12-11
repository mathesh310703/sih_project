from gtts import gTTS
language = "en"
text = 'dog'
speech = gTTS(text = text , lang = language ,slow = True)
speech.save("a.mp3")