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
print(a)


lst = a
i=0
lst = [str(i) for i in lst]
result = ''.join(lst)
print(result)


retrived_therapy = (result[2:-3])
print(retrived_therapy)

import pyttsx3 
text = retrived_therapy
text_speech = pyttsx3.init()
text_speech.say(text)
text_speech.runAndWait()





   