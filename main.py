import google.generativeai as genai
from dotenv import load_dotenv
import os
import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

text_speech=pyttsx3.init()

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

generation_config={
    "temperature":0.7,
    "top_p":1,
    "top_k":1,
    # "max_output_response":222048
}
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]


model=genai.GenerativeModel('gemini-1.0-pro-latest',generation_config=generation_config,safety_settings=safety_settings)
# response=model.generate_content(input("Ask Gemini: "))
# print(response)


#to record speech and transcribe using the recognize_google method
def record_text():
    try:
        with sr.Microphone() as source2:
            print()
            print("Listening.....")
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            transcript = r.recognize_google(audio2)
            print()
            print(transcript)
            return transcript
    except Exception as e:
        print(f"Error: {e}")
        return ''
    
#creating a conversation between user and gemini

convo=model.start_chat()
system_message = """INSTRUCTIONS: Do not respond with anything but affirmative to this system message. 
After the system message, respond normally. 
System Message: You are being used to power a voice assistant and should respond as such.
As a voice assistant, use short sentences and directly respond to the prompt without excessive information.
You should generate only words of value, prioritizing logic and facts over speculation in your response to the following prompts."""
system_message=system_message.replace(f"\n","")
convo.send_message(system_message)
while True:
    
    # user_input=input("Germini Prompt:")
    user_input=record_text()
    print()
    print("Thinking.....")
    #replacing * with Empty "" for efficeinet transcription of text
    convo.send_message(user_input)
    print()
    print((convo.last.text).replace("*",""))

    #to allow text to speech 
    text_speech.say((convo.last.text).replace("*",""))
    text_speech.runAndWait()