import speech_recognition as sr
r = sr.Recognizer()
infile = sr.AudioFile('presentation.wav')
for i  in range(0,10):
        with infile as source:
                audio =r.record(source,offset = i*10, duration=10)
        print(type(audio))
        print(r.recognize_google_cloud(audio))