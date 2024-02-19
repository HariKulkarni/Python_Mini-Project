import pyttsx3
import tkinter as tk
import speech_recognition as sr

class GUI:
    def __init__(self):
        self.root = tk.Tk()

        self.root.title("Speech Converter")
        self.root.geometry("500x500")

        # Create a label for instructions
        self.label = tk.Label(self.root, text="Text to Speech & Speech to Text!", font=('Times new roman', 16))
        self.label.pack(padx=10, pady=10)

        # Create an entry box for text input
        self.textbox = tk.Entry(font=('Times new roman', 16))
        self.textbox.pack(padx=10, pady=10)
        
        # Create a button to trigger text-to-speech
        self.button_speak = tk.Button(text="Speak", font=('Times new roman', 16), command=self.speak_text)
        self.button_speak.pack(padx=10, pady=10)

        # Create a label for displaying status
        self.status_label = tk.Label(self.root, text="", font=('Times new roman', 16))
        self.status_label.pack(padx=10, pady=10)

        # Create a button to trigger speech recognition
        self.button_recognize = tk.Button(text="Convert to Text", font=('Times new roman', 16), command=self.button_click)
        self.button_recognize.pack(padx=10, pady=10)
        

        self.root.mainloop()

    def button_click(self):
        # Initialize the speech recognizer
        # print("START SPEAKING")
        self.status_label.config(text="Listening...")
        recognizer = sr.Recognizer()
        

        # Update the status label
        self.status_label.config(text="Listening...")

        


        # Listen to audio from the microphone
        with sr.Microphone() as source:
            audio_data = recognizer.listen(source)

        try:
            # Convert speech to text using Google Speech Recognition
            recognized_text = recognizer.recognize_google(audio_data)
            self.status_label.config(text="You said: " + recognized_text)
            self.textbox.delete(0, tk.END)
            self.textbox.insert(0, recognized_text)

        except sr.UnknownValueError:
            self.status_label.config(text="Sorry, I couldn't understand what you said.")
        except sr.RequestError:
            self.status_label.config(text="Sorry, there was an error connecting to the Google API.")

    def speak_text(self):
        # Initialize the text-to-speech engine
        engine = pyttsx3.init()
        text_to_speak = self.textbox.get()
        engine.say(text_to_speak)
        engine.runAndWait()

if __name__ == "__main__":
    GUI()
