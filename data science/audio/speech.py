import speech_recognition as sr
def main():
    sound="Week 7_Graded assignment.wav"
    r =sr.Recognizer()
    
    with sr.AudioFile(sound) as source:
        r.adjust_for_ambient_noise(source)
        
        print("converting audio file to text")
        audio=r.listen(source)
        try:
             print("converted audio is:\n"+r.recognize_google(audio))
        except Exception as e:
             print(e)

main()
