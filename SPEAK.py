import streamlit as st
import pyttsx3
import speech_recognition as sr

def main():
    st.title("Text to Speech and Speech to Text")

    # Text input box
    text_input = st.text_input("Enter text:", "")

    # Button to trigger text-to-speech
    if st.button("Speak"):
        engine = pyttsx3.init()
        engine.say(text_input)
        engine.runAndWait()

    # Button to trigger speech recognition
    if st.button("Convert to Text"):
        recognizer = sr.Recognizer()
        st.write("Listening...")

        # Listen to audio from the microphone
        with sr.Microphone() as source:
            audio_data = recognizer.listen(source)

        try:
            # Convert speech to text using Google Speech Recognition
            recognized_text = recognizer.recognize_google(audio_data)
            st.write("You said:", recognized_text)

        except sr.UnknownValueError:
            st.write("Sorry, I couldn't understand what you said.")
        except sr.RequestError:
            st.write("Sorry, there was an error connecting to the Google API.")

if __name__ == "__main__":
    main()
