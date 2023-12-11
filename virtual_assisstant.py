import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak anything: ")
    audio = r.listen(source)
try:
    text = r.recognize_google(audio)
    print('The converted text is:', text)
except:
    print('Sorry, I could not convert the audio to text.')