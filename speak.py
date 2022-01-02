import pyttsx3
Bob_brain = "I don't understand what you said, try again"

Bob_mouth = pyttsx3.init()
Bob_mouth.say(Bob_brain)
Bob_mouth.runAndWait()
