import speech_recognition as sr
import pyttsx3 
  
# Initialize the recognizer 
r = sr.Recognizer() 
  
# Function to convert text to
# speech
def SpeakText(command):
      
    # Initialize the engine
    engine = pyttsx3.init()
    engine.setProperty('voice', 'english+f1')
    engine.setProperty("rate", 178)
    engine.say(command) 
    engine.runAndWait()
      


stop_program = ["see you", "good bye", "see you around", "talk to you later", "talk later"]
goodbye_msg = "Okay! I will miss you"
one_to_ten = "One, Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten"
# Loop infinitely for user to
# speak
  
while(1):    
      
    # Exception handling to handle
    # exceptions at the runtime
    try:
          
        # use the microphone as source for input.
        with sr.Microphone() as source2:
              
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level 
            r.adjust_for_ambient_noise(source2, duration=0.2)
              
            #listens for the user's input 
            audio2 = r.listen(source2)
              
            # Using ggogle to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            if any(stop_program in MyText for stop_program in stop_program):
                SpeakText(goodbye_msg)
                break
            if "1 to 10" in MyText:
                SpeakText(one_to_ten)

            print("Did you say "+MyText)
            SpeakText(MyText)
              
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
          
    except sr.UnknownValueError:
        print("unknown error occured")