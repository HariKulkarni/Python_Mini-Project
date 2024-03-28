import streamlit as st
from googletrans import Translator
from gtts import gTTS
import os

class LanguageTranslatorApp:
    def __init__(self):
        st.title("Language Translator")
        
        self.source_lang = st.text_input("Source Language:")
        self.target_lang = st.text_input("Target Language:")
        self.text_to_translate = st.text_area("Text to Translate:")
        
        self.translate_button = st.button("Translate")
        self.translated_text_display = st.empty()
        
        self.play_button = st.button("Play")
        
    def translate_text(self):
        if not self.source_lang or not self.target_lang or not self.text_to_translate:
            st.error("Please fill in all fields.")
            return
        
        source_lang_code = self.get_language_code(self.source_lang.lower())
        target_lang_code = self.get_language_code(self.target_lang.lower())
        
        translator = Translator()
        translation = translator.translate(self.text_to_translate, src=source_lang_code, dest=target_lang_code)
        
        self.translated_text_display.text(translation.text)
        self.translated_text = translation.text
        
    def play_translated_text(self):
        tts = gTTS(text=self.translated_text, lang=self.get_language_code(self.target_lang.lower()))
        tts.save("translated_text.mp3")
        os.system("start translated_text.mp3")
        
    def get_language_code(self, language):
        lang_mapping = {
            "english": "en",
            "hindi": "hi",
            "bengali": "bn",
            "telugu": "te",
            "marathi": "mr",
            "tamil": "ta",
            "kannada": "kn",
            "usa": "en",
            "china": "zh-cn",
            "brazil": "pt",
            "russia": "ru",
            "japan": "ja",
            "germany": "de",
            "france": "fr",
            "italy": "it",
            "spain": "es"
        }
        return lang_mapping.get(language, "en")

def main():
    app = LanguageTranslatorApp()
    if app.translate_button:
        app.translate_text()
    if app.play_button:
        app.play_translated_text()

if __name__ == "__main__":
    main()
