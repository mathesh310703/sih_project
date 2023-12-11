import  psycopg2
connection = psycopg2.connect(host = "localhost",port = "5432",database = "dbhost",user = "postgres",password = "root")

cursor = connection.cursor()
print("database is connected successfully")

disease = input()
if disease == "apraxia":
    cursor.execute("select therapy_text from therapy where t_id = 1;")
elif disease == "dysrthria":
    cursor.execute("select therapy_text from therapy where t_id = 2;")
elif disease == "stuttering":
    cursor.execute("select therapy_text from therapy where t_id = 3;")

a = cursor.fetchall()


lst = a
i=0
lst = [str(i) for i in lst]
result = ''.join(lst)
retrived_therapy = (result[2:-3])
print(retrived_therapy)

import pyttsx3 
instruction = retrived_therapy
text_speech = pyttsx3.init()
text_speech.say(instruction)
text_speech.runAndWait()

import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak anything: ")
    audio = r.listen(source)
try:
    text = r.recognize_google(audio)
    print(text)
except Exception as e:
     print('Sorry, I could not convert the audio to text')

if text == instruction:
    print("your exercise is successfully completed")
else:
    print("retry this exercise")
    