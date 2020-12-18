import speech_recognition as sr
spch_rec = sr.Recognizer()

def input_command():
    with sr.Microphone() as src:
         voice_input = spch_rec.listen(src)
         command = spch_rec.recognize_google(voice_input)
         command = command.lower()
         print(command)

while True:
    input_command()
