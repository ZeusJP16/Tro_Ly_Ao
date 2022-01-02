import speech_recognition

Bob_ear = speech_recognition.Recognizer()

with speech_recognition.Microphone() as mic:
	print("\nBob: I'm listening")
	audio = Bob_ear.listen(mic) 

try:
	Me = Bob_ear.recognize_google(audio, language='en-US') 
	
except:
	Me = "" 
print("Me: " + Me)
