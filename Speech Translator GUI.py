# Below are the images needed: The package is sys is used for system specific functions and parameters, re for handling the functions in regular
# expression, speech_recognition for handling the speech recognition, googletrans package for the translation and to work with GUI and related
# widgets use the tkinter.ttk and tkinter.
import sys
from tkinter.ttk import Combobox
import re
from tkinter import messagebox
import speech_recognition as sr
from tkinter import *
import os
from googletrans import Translator as gt

# Global variables for error and dictionary to store the key, value of language code and country, translate country and code

speech_languages = {"af-ZA": "Afrikaans (South Africa)", "am-ET": "Amharic (Ethiopia)", "hy-AM": "Armenian (Armenia)",
                    "az-AZ": "Azerbaijani (Azerbaijan)",
                    "id-ID": "Indonesian (Indonesia)", "ms-MY": "Malay (Malaysia)", "bn-BD": "Bengali (Bangladesh)",
                    "bn-IN": "Bengali (India)",
                    "ca-ES": "Catalan (Spain)", "cs-CZ": "Czech (Czech Republic)", "da-DK": "Danish (Denmark)",
                    "de-DE": "German (Germany)",
                    "en-AU": "English (Australia)", "en-CA": "English (Canada)", "en-GH": "English (Ghana)",
                    "en-GB": "English (United Kingdom)",
                    "en-IN": "English (India)", "en-IE": "English (Ireland)", "en-KE": "English (Kenya)",
                    "en-NZ": "English (New Zealand)",
                    "en-NG": "English (Nigeria)", "en-PH": "English (Philippines)", "en-SG": "English (Singapore)",
                    "en-ZA": "English (South Africa)",
                    "en-TZ": "English (Tanzania)", "en-US": "English (United States)", "es-AR": "Spanish (Argentina)",
                    "es-BO": "Spanish (Bolivia)",
                    "es-CL": "Spanish (Chile)", "es-CO": "Spanish (Colombia)", "es-CR": "Spanish (Costa Rica)",
                    "es-EC": "Spanish (Ecuador)",
                    "es-SV": "Spanish (El Salvador)", "es-ES": "Spanish (Spain)", "es-US": "Spanish (United States)",
                    "es-GT": "Spanish (Guatemala)",
                    "es-HN": "Spanish (Honduras)", "es-MX": "Spanish (Mexico)", "es-NI": "Spanish (Nicaragua)",
                    "es-PA": "Spanish (Panama)",
                    "es-PY": "Spanish (Paraguay)", "es-PE": "Spanish (Peru)", "es-PR": "Spanish (Puerto Rico)",
                    "es-DO": "Spanish (Dominican Republic)",
                    "es-UY": "Spanish (Uruguay)", "es-VE": "Spanish (Venezuela)", "eu-ES": "Basque (Spain)",
                    "fil-PH": "Filipino (Philippines)",
                    "fr-CA": "French (Canada)", "fr-FR": "French (France)", "gl-ES": "Galician (Spain)",
                    "ka-GE": "Georgian (Georgia)",
                    "gu-IN": "Gujarati (India)", "hr-HR": "Croatian (Croatia)", "zu-ZA": "Zulu (South Africa)",
                    "is-IS": "Icelandic (Iceland)",
                    "it-IT": "Italian (Italy)", "jv-ID": "Javanese (Indonesia)", "kn-IN": "Kannada (India)",
                    "km-KH": "Khmer (Cambodia)",
                    "lo-LA": "Lao (Laos)", "lv-LV": "Latvian (Latvia)", "lt-LT": "Lithuanian (Lithuania)",
                    "hu-HU": "Hungarian (Hungary)",
                    "ml-IN": "Malayalam (India)", "mr-IN": "Marathi (India)", "nl-NL": "Dutch (Netherlands)",
                    "ne-NP": "Nepali (Nepal)",
                    "nb-NO": "Norwegian Bokmål (Norway)", "pl-PL": "Polish (Poland)", "pt-BR": "Portuguese (Brazil)",
                    "pt-PT": "Portuguese (Portugal)",
                    "ro-RO": "Romanian (Romania)", "si-LK": "Sinhala (Sri Lanka)", "sk-SK": "Slovak (Slovakia)",
                    "sl-SI": "Slovenian (Slovenia)",
                    "su-ID": "Sundanese (Indonesia)", "sw-TZ": "Swahili (Tanzania)", "sw-KE": "Swahili (Kenya)",
                    "fi-FI": "Finnish (Finland)",
                    "sv-SE": "Swedish (Sweden)", "ta-IN": "Tamil (India)", "ta-SG": "Tamil (Singapore)",
                    "ta-LK": "Tamil (Sri Lanka)",
                    "ta-MY": "Tamil (Malaysia)", "te-IN": "Telugu (India)", "vi-VN": "Vietnamese (Vietnam)",
                    "tr-TR": "Turkish (Turkey)",
                    "ur-PK": "Urdu (Pakistan)", "ur-IN": "Urdu (India)", "el-GR": "Greek (Greece)",
                    "bg-BG": "Bulgarian (Bulgaria)",
                    "ru-RU": "Russian (Russia)", "sr-RS": "Serbian (Serbia)", "uk-UA": "Ukrainian (Ukraine)",
                    "he-IL": "Hebrew (Israel)",
                    "ar-IL": "Arabic (Israel)", "ar-JO": "Arabic (Jordan)", "ar-AE": "Arabic (United Arab Emirates)",
                    "ar-BH": "Arabic (Bahrain)",
                    "ar-DZ": "Arabic (Algeria)", "ar-SA": "Arabic (Saudi Arabia)", "ar-IQ": "Arabic (Iraq)",
                    "ar-KW": "Arabic (Kuwait)",
                    "ar-MA": "Arabic (Morocco)", "ar-TN": "Arabic (Tunisia)", "ar-OM": "Arabic (Oman)",
                    "ar-PS": "Arabic (State of Palestine)",
                    "ar-QA": "Arabic (Qatar)", "ar-LB": "Arabic (Lebanon)", "ar-EG": "Arabic (Egypt)",
                    "fa-IR": "Persian (Iran)", "hi-IN": "Hindi (India)",
                    "th-TH": "Thai (Thailand)", "ko-KR": "Korean (South Korea)",
                    "zh-TW": "Chinese, Mandarin (Traditional, Taiwan)",
                    "yue-Hant-HK": "Chinese, Cantonese (Traditional, Hong Kong)", "ja-JP": "Japanese (Japan)",
                    "zh-HK": "Chinese, Mandarin (Simplified, Hong Kong)", "zh": "Chinese, Mandarin (Simplified, China)"}
error = "Didn't listened properly."
languages = {'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 'hy': 'armenian',
             'az': 'azerbaijani', 'eu': 'basque',
             'be': 'belarusian', 'bn': 'bengali', 'bs': 'bosnian', 'bg': 'bulgarian', 'ca': 'catalan', 'ceb': 'cebuano',
             'ny': 'chichewa',
             'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)', 'co': 'corsican', 'hr': 'croatian',
             'cs': 'czech',
             'da': 'danish', 'nl': 'dutch', 'en': 'english', 'eo': 'esperanto', 'et': 'estonian', 'tl': 'filipino',
             'fi': 'finnish', 'fr': 'french',
             'fy': 'frisian', 'gl': 'galician', 'ka': 'georgian', 'de': 'german', 'el': 'greek', 'gu': 'gujarati',
             'ht': 'haitian creole',
             'ha': 'hausa', 'haw': 'hawaiian', 'iw': 'hebrew', 'hi': 'hindi', 'hmn': 'hmong', 'hu': 'hungarian',
             'is': 'icelandic', 'ig': 'igbo',
             'id': 'indonesian', 'ga': 'irish', 'it': 'italian', 'ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada',
             'kk': 'kazakh', 'km': 'khmer',
             'ko': 'korean', 'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz', 'lo': 'lao', 'la': 'latin', 'lv': 'latvian',
             'lt': 'lithuanian',
             'lb': 'luxembourgish', 'mk': 'macedonian', 'mg': 'malagasy', 'ms': 'malay', 'ml': 'malayalam',
             'mt': 'maltese', 'mi': 'maori',
             'mr': 'marathi', 'mn': 'mongolian', 'my': 'myanmar (burmese)', 'ne': 'nepali', 'no': 'norwegian',
             'ps': 'pashto', 'fa': 'persian',
             'pl': 'polish', 'pt': 'portuguese', 'pa': 'punjabi', 'ro': 'romanian', 'ru': 'russian', 'sm': 'samoan',
             'gd': 'scots gaelic',
             'sr': 'serbian', 'st': 'sesotho', 'sn': 'shona', 'sd': 'sindhi', 'si': 'sinhala', 'sk': 'slovak',
             'sl': 'slovenian',
             'so': 'somali', 'es': 'spanish', 'su': 'sundanese', 'sw': 'swahili', 'sv': 'swedish', 'tg': 'tajik',
             'ta': 'tamil', 'te': 'telugu',
             'th': 'thai', 'tr': 'turkish', 'uk': 'ukrainian', 'ur': 'urdu', 'uz': 'uzbek', 'vi': 'vietnamese',
             'cy': 'welsh', 'xh': 'xhosa',
             'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu', 'fil': 'Filipino', 'he': 'Hebrew'}


class SR_GUI(Frame):
    # Printing the Python Version
    print("Python Version:" + sys.version)

    # The below is the constructor method. In this method we are setting the title of the frame and and configuring the backgroung color.
    # The argument self in the __init__ method points to the current object
    def __init__(self, master):
        Frame.__init__(self, master=None)
        self.master = master
        self.master.config(bg="#D95137")
        self.master.title("Speech Recognition & Translation Tool")
        #self.master.iconbitmap('mul_logo.ico')
        self.add_widgets()

    # In add_widgets() we are creating the widgets.# Use can use grid(),place() or pack() to place the widget in the frame or window.

    def add_widgets(self):
        self.combo_speech_var = StringVar()
        self.combo_var = StringVar()
        # Adding logo and the title
        self.photo = PhotoImage(file='sau-logo1.png')
        self.logoLabel = Label(root, image=self.photo,bg="#D95137")
        self.logoLabel.place(x=70,y=20)
        self.logoLabel2 = Label(root, text="Speech Recognition & Translation Tool", bg="#D95137", fg="#F1CC01", font="none 20 bold", wraplength=300)
        self.logoLabel2.place(x=185, y=40)

        # Retrieving all the languages dictionary values, sorting and converting to list as we are passing as input to the combobox
        self.speech_lang_values = sorted(list(speech_languages.values()))
        # Retrieving all the languages dictionary keys as we want to pass to the destination field during the translation
        self.speech_lang_keys = list(speech_languages.keys())


        # Language to translate Keys and Values. Already in sorted order
        self.lang_values = list(languages.values())
        # Retrieving all the languages dictionary keys as we want to pass to the destination field during the translation
        self.lang_keys = list(languages.keys())
        self.lang_values_Capitalize = [self.lang_value.capitalize() for self.lang_value in self.lang_values]

        #=================================Speaking Part==============================================

        # Labels for "Speaking In" and "You said"
        label_speech_language = Label(self.master, text="Speaking in:", bg="#D95137", font="none 10 bold")
        label_speech_language.place(x=0, y=160)

        label_yousaid = Label(self.master, text="You Said:", bg="#D95137", bd=3, font="none 10 bold")
        label_yousaid.place(x=0, y=220)

        # Languages Comboxbox you can speak in. By default is "English (United States)"
        self.combo_speech = Combobox(self.master, values=self.speech_lang_values, textvariable=self.combo_speech_var)
        self.combo_speech.bind("<<ComboboxSelected>>", self.speech_Callbackfunc)
        self.combo_speech.bind("<KeyPress>", self.searchList)
        self.combo_speech.bind("<Return>",self.returnEvent)
        self.combo_speech.bind("<Down>",self.arrowEvent)
        #self.combo_speech.bind("<Up>",self.arrowEvent)
        self.combo_speech.set("English (United States)")
        self.combo_speech.place(x=120, y=160)
        self.combo_speech.focus_set()



        # Textarea creation. Non editable as set state to DISABLED
        text_area = Text(self.master, width=50, height=5, state=DISABLED)
        text_area.place(x=120, y=190)

        # Referenced the text_area to self.ta as it has to be used in other functions
        self.ta = text_area
        # Button Creation. On Button click it'll call the method self.add_text and set the text_area to "Listening...."
        button1 = Button(text="Click Here to Speak", command=self.add_text, font="none 10")
        button1.place(x=240, y=300)

        #===================================Translation Part==========================================

        self.label_combo = Label(self.master, text="Translate To:", bg="#D95137", font="none 10 bold")
        self.label_combo.place(x=5, y=350)

        self.combo_translate = Combobox(self.master, height=6, textvariable=self.combo_var,values=sorted(self.lang_values_Capitalize))
        # Setting the default value of the combobox to "Select" instead of empty
        self.combo_translate.set("Select")
        self.combo_translate.bind("<<ComboboxSelected>>", self.callbackFunc)
        self.combo_translate.bind("<KeyPress>", self.searchList1)
        self.combo_translate.bind("<Return>", self.returnEvent1)
        self.combo_translate.bind("<Down>", self.arrowEvent1)


        self.combo_translate.place(x=120, y=350)

        label_translate = Label(self.master, text="Translated Text:", bg="#D95137", font="none 10 bold")
        label_translate.place(x=5, y=410)

        self.text_area_translate = Text(self.master, width=50, height=5, state=DISABLED)
        self.text_area_translate.place(x=120, y=380)

        self.translate_button = Button(self.master, text="Click Here to Translate", font="none 10",command=self.translate_text)
        self.translate_button.place(x=240, y=490)
        cancel_button = Button(self.master, text="Reset", command=self.on_Cancel, width=10, font="none 10")
        cancel_button.place(x=180, y=540)
        quit_button = Button(self.master, text="Quit", command=self.master.destroy, width=10, font="none 10")
        quit_button.place(x=330, y=540)

    #=========================Events and Method Calls=====================================

    def searchList(self, event):
        print("In searchList. Called by the event Key Press")
        if self.combo_speech_var.get() in self.speech_lang_values:
            print("Value of combo_speech_var.get:"+self.combo_speech_var.get())
            self.combo_speech_var.set("")
            self.combo_speech.focus_set()
            self.combo_speech.bind("<KeyRelease>", self.newSearchEvent)

    def newSearchEvent(self, event):
        print("In newSearchEvent. Called by the event KeyRelease")
        value = event.widget.get().upper()
        print("Converted the value of the key press to upper:"+value)
        for index, value_name in enumerate(self.speech_lang_values):
            if value_name[0] == value:
                self.combo_speech.current(index)
                print("Added to get value the search result in speech combobox:"+self.combo_speech_var.get())
                self.speech_Callbackfunc(event)
                break

    def returnEvent(self,event):
        self.combo_speech_var.set(self.combo_speech_var.get())
        self.speech_Callbackfunc(event)

    def arrowEvent(self,event):
        self.combo_speech.set(self.combo_speech_var.get())
    def arrowEvent1(self,event):

        self.combo_translate.set(self.combo_var.get())


    def searchList1(self, event):
        print("In searchList1. Called by the event Key Press")
        self.combo_var.set("")
        self.combo_translate.focus_set()
        self.combo_translate.bind("<KeyRelease>", self.newSearchEvent1)

    def newSearchEvent1(self, event):
        print("In newSearchEvent1. Called by the event KeyRelease")
        value = event.widget.get().upper()
        print("Value in new Event:"+value)
        print("Converted the value of the key press to upper:"+value)
        for index, value_name in enumerate(sorted(self.lang_values_Capitalize)):
            if value_name[0] == value:
                self.combo_translate.current(index)
                print("Added to get value the search result in translate combobox:" + self.combo_speech_var.get())
                self.callbackFunc(event)
                break


    def returnEvent1(self, event):
        self.combo_var.set(self.combo_var.get())
        self.callbackFunc(event)

    # Method to insert text into the text area adjust to "You said" label
    def add_text(self):
        if self.combo_speech_var.get()!="":
            if self.combo_speech_var.get() == "English (United States)":
                self.selected_speech_keys = [key for (key, value) in speech_languages.items() if value == "English (United States)"]
                self.final_sk = re.sub('[^-a-z-A-Z]', '', str(self.selected_speech_keys))
                print("Selected Language to Speak:"+self.final_sk)
                self.combo_translate.set("Select")
                self.ta.configure(state=NORMAL)
                self.ta.delete(1.0, END)
                self.ta.insert(END, "Listening....")
                self.text_area_translate.configure(state=NORMAL)
                self.text_area_translate.delete(1.0, END)
                self.text_area_translate.configure(state=DISABLED)
                self.ta.update()
                self.speech_recog()
            else:
                self.selected_speech_keys = [key for (key, value) in speech_languages.items() if value == self.selected_speech_value]
                self.final_sk = re.sub('[^-a-z-A-Z]', '', str(self.selected_speech_keys))
                print("Selected Language to Speak:" + self.final_sk)
                self.combo_translate.set("Select")
                self.ta.configure(state=NORMAL)
                self.ta.delete(1.0, END)
                self.ta.insert(END, "Listening....")
                self.text_area_translate.configure(state=NORMAL)
                self.text_area_translate.delete(1.0, END)
                self.text_area_translate.configure(state=DISABLED)
                self.ta.update()
                self.speech_recog()
        else:
            self.combo_speech_var.set("English (United States)")
            self.add_text()


    def on_Cancel(self):
        self.combo_speech.set("English (United States)")
        self.ta.configure(state=NORMAL)
        self.ta.delete(1.0, END)
        self.ta.configure(state=DISABLED)
        self.text_area_translate.configure(state=NORMAL)
        self.text_area_translate.delete(1.0, END)
        self.text_area_translate.configure(state=DISABLED)
        self.combo_translate.set("Select")
        #self.translate_button.configure(state=DISABLED)

    # Event for the language combo box where user selects the desired language to speak
    def speech_Callbackfunc(self, event):
        self.selected_speech_value = self.combo_speech_var.get()
        print("Callback:"+self.selected_speech_value)


    # Event for the language combo box where user selects the desired language to translate
    def callbackFunc(self, event):

        self.selected_value = self.combo_var.get().lower()
        print("Selected Language" + ":" + self.selected_value)

    # In this method we are creating object for speechrecognition and selecting the engine we want to use.
    def speech_recog(self):
        # Printing the Speech Recognition Version
        print("Speech Recognition:" + sr.__version__)
        # Creating the object for speech recognition as r
        r = sr.Recognizer()
        # Print the object r
        print("The object of speech recognition:" + str(r))
        # As we want to listen to the voice from the microphone use the Microphone() from speech_recognition
        micro_phone = sr.Microphone()
        # To list all the available microphones use the list_microphone_names
        list_of_microphone_devices = micro_phone.list_microphone_names()
        print("List of available devices:")
        for i in range(0, len(list_of_microphone_devices)):
            print(list_of_microphone_devices[i] + " ")
        print("Total number of devices:" + str(len(list_of_microphone_devices)))
        with micro_phone as source:
            # As we are using the microphone as source we use the listen(). If we are using source as some audio files we use the record()
            audio = r.listen(source)
        try:
            self.a_text = r.recognize_google(audio, language=self.final_sk)
            print("you said: " + self.a_text)
            # As we want to clear the text everytime we speak, we delete the already present text in the textarea insert new text and diable the
            # textarea. Before inserting the text to the textarea set the state to NORMAL or else if wont insert the text
            self.ta.delete(1.0, END)
            self.ta.insert(END, self.a_text)
            self.ta.configure(state=DISABLED)
            # In the exception we disabling the radio buttons and inserting the error message inside the textarea
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            self.ta.delete("1.0", END)
            self.ta.insert(END, "Click the button to try again")
            self.ta.configure(state=DISABLED)
            messagebox.showwarning("Warning", (error + "\n" + "Try Again....!"))

    # This method will retreive the key pass to the destination field in translator.translate()
    def translate_text(self):
        print("Getting combo_var:" + self.combo_var.get())
        if self.combo_var.get()=="Select":
            self.text_area_translate.configure(state=NORMAL)
            self.text_area_translate.delete(1.0, END)
            self.text_area_translate.configure(state=DISABLED)
        else:
            self.selected_keys = [key for (key, value) in languages.items() if value == self.selected_value]
            # Here we are extracting only the alphabets. As the keys we get in enclosed in the square brakets and single quotes
            reg_key = re.sub('[^-a-zA-Z]', '', str(self.selected_keys))
            print("reg_key:" + reg_key)
            # Creating the object for translator
            translator = gt()
            self.text_after_translation = translator.translate(self.a_text, dest=reg_key)
            print(self.text_after_translation)
            self.insert_translation_text()

    # This method will insert the translated text to the text_area_translate and delete the content in the text_area_translate if there is no
    # translation available
    def insert_translation_text(self):
              if self.combo_var.get()!="":
                print("Translated Text:"+self.text_after_translation.text)
                self.text_area_translate.configure(state=NORMAL)
                self.text_area_translate.delete(1.0, END)
                self.text_area_translate.insert(1.0, self.text_after_translation.text)
                self.text_area_translate.configure(state=DISABLED)
              else:
                  self.combo_var.set("Select")
                  self.translate_text()



root = Tk()
# Set the dimensions of the window using geometry
root.geometry("550x600")
# Disable maximise
root.resizable(width=0, height=0)
my_sr = SR_GUI(root)
root.mainloop()

