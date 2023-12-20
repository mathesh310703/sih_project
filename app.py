from flask import Flask, render_template,request
# import  psycopg2
# import speech_recognition as sr
# r = sr.Recognizer()

app = Flask(__name__)

# connection = psycopg2.connect(host = "localhost",port = "5432",database = "localhost",user = "postgres",password = "root")
# cursor = connection.cursor()
# print("database is connected successfully")
    
@app.route("/")
def home():
    return render_template('index.html')

@app.route('/play_audio',methods=['POST'])
def process():

    data = request.get_json()
    word = data['word']
    print(f"Received word: {word}")
    cursor.execute(f"select therapy_words from therapy where therapy_words = {word};")

    a = cursor.fetchall()
    lst = a
    i=0
    lst = [str(i) for i in lst]
    result = ''.join(lst)
    retrived_therapy = (result[2:-3])
    print(retrived_therapy)
    instruction = retrived_therapy

    with sr.Microphone() as source:
        print("Speak anything: ")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(text)
    except Exception as e:
        print('Sorry, I could not convert the audio to text')
    text = text.lower()

    if text == instruction:
        print("your exercise is successfully completed")
    else:
        print("retry this exercise")

    return (f"{text} {instruction}")

if __name__ == "__main__":
    app.run()