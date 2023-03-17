import streamlit as st
import asyncio
import io
import glob
import os
from gtts import gTTS
from io import BytesIO
import sys
import time
import uuid
import requests
from urllib.parse import urlparse
from io import BytesIO
# To install this module, run:
# python -m pip install Pillow
from io import BytesIO
from PIL import Image
from PIL import ImageDraw
import json
import googletrans
from googletrans import Translator




st.set_page_config(layout="wide")
st.sidebar.image('images/translate.jpg', width=300)
st.sidebar.header('Used googletrans library to detect and translate the text and using google speech recognition, it will translate any lanuguage to your desired language')
st.sidebar.markdown('It can translate any language (default-"english")')


app_mode = st.sidebar.radio(
    "",
    ("About Me","Language Translation","text to speech"),
)


st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.markdown('---')
st.sidebar.write('N.V.Suresh Krishna | sureshkrishnanv24@gmail.com https://github.com/sureshkrishna123')

if app_mode =='About Me':
    #st.image('images/wp4498220.jpg', use_column_width=True)
    st.markdown('''
              # About Me \n 
                Hey this is ** N.V.Suresh Krishna **. \n
                
                
                Also check me out on Social Media
                - [git-Hub](https://github.com/sureshkrishna123)
                - [LinkedIn](https://www.linkedin.com/in/suresh-krishna-nv/)
                - [Instagram](https://www.instagram.com/worldofsuresh._/)
                - [Portfolio](https://sureshkrishna123.github.io/sureshportfolio/)
                - [Blog](https://ingenious-point.blogspot.com/)\n
                ''')
               

if app_mode=='Language Translation':
  st.image(os.path.join('./images','translate.jpg'),use_column_width=True )
  st.title("Language Translation")
  st.header('Language translation taking text as an input')
  st.markdown("Using googletrans library to detect and translate the text to your desired language")
  #st.text("Detect the objects in images")
  
  detect=st.text_input('Enter the text to detect (No language Restriction):')

  detect_select=st.selectbox("select language to translate" ,['arabic','bangla','chinese','dutch','english','french','german','greek','hindi','hungarian','indonesian','irish','italian','japanese','kannada','korean','malayalam','nepali','portuguese','punjabi','russian','spanish','tamil','telugu','turkish','urdu'],key=1)

  if detect_select == 'arabic':
        detect_lang= 'ar'
  elif detect_select == 'bangla':
        detect_lang= 'bn'
  elif detect_select == 'chinese':
        detect_lang= 'lzh'
  elif detect_select == 'dutch':
        detect_lang= 'nl'
  elif detect_select == 'english':
        detect_lang= 'en'
  elif detect_select == 'french':
        detect_lang= 'fr'
  elif detect_select == 'german':
        detect_lang= 'de'
  elif detect_select == 'greek':
        detect_lang= 'el'
  elif detect_select == 'hindi':
        detect_lang= 'hi'
  elif detect_select == 'hungarian':
        detect_lang= 'hu'
  elif detect_select == 'indonesian':
        detect_lang= 'id'
  elif detect_select == 'irish':
        detect_lang= 'ga'
  elif detect_select == 'italian':
        detect_lang= 'it'
  elif detect_select == 'japanese':
        detect_lang= 'ja'
  elif detect_select == 'kannada':
        detect_lang= 'kn'
  elif detect_select == 'korean':
        detect_lang= 'ko'
  elif detect_select == 'malayalam':
        detect_lang= 'ml'
  elif detect_select == 'nepali':
        detect_lang= 'ne'
  elif detect_select == 'portuguesei':
        detect_lang= 'pt'
  elif detect_select == 'punjabi':
        detect_lang= 'pa'
  elif detect_select == 'russian':
        detect_lang= 'ru'
  elif detect_select == 'spanish':
        detect_lang= 'es'
  elif detect_select == 'tamil':
        detect_lang= 'ta'
  elif detect_select == 'telugu':
        detect_lang= 'te'  
  elif detect_select == 'turkish':
        detect_lang= 'tr'
  elif detect_select == 'urdu':
        detect_lang= 'ur'  

  button_translate=st.button('Click me',help='To give the image')


  if button_translate and detect :
    try:
        translater = Translator()
        out = translater.translate(detect, dest=detect_lang)
        st.header(out.text)
    except:
        st.error("!! Please enter input in any language")

  st.markdown('---')

if app_mode=='text to speech':
    
    st.image(os.path.join('./images','translate.jpg'),use_column_width=True )
    st.title("Text to speech")
    st.header('Language translation taking text as an input')
    st.markdown("Using googletrans library to detect and translate the text to your desired language")
  #st.text("Detect the objects in images")
    try:
        os.mkdir("temp")
    except:
        pass
    translator = Translator()
  
    text=st.text_input('Enter the text to convert to speech (No language Restriction):')

    input_text=st.selectbox("select language to of the text" ,['arabic','bangla','chinese','dutch','english','french','german','greek','hindi','hungarian','indonesian','irish','italian','japanese','kannada','korean','malayalam','nepali','portuguese','punjabi','russian','spanish','tamil','telugu','turkish','urdu'],key=1)
    
    output_language=st.selectbox("select language to convert" ,['arabic','bangla','chinese','dutch','english','french','german','greek','hindi','hungarian','indonesian','irish','italian','japanese','kannada','korean','malayalam','nepali','portuguese','punjabi','russian','spanish','tamil','telugu','turkish','urdu'],key=2)

    if input_text == 'arabic':
        input_lang= 'ar'
    elif input_text == 'bangla':
        input_lang= 'bn'
    elif input_text == 'chinese':
        input_lang= 'lzh'
    elif input_text == 'dutch':
        input_lang= 'nl'
    elif input_text == 'english':
        input_lang= 'en'
    elif input_text == 'french':
        input_lang= 'fr'
    elif input_text == 'german':
        input_lang= 'de'
    elif input_text == 'greek':
        input_lang= 'el'
    elif input_text == 'hindi':
        input_lang= 'hi'
    elif input_text == 'hungarian':
        input_lang= 'hu'
    elif input_text == 'indonesian':
        input_lang= 'id'
    elif input_text == 'irish':
        input_lang= 'ga'
    elif input_text == 'italian':
        input_lang= 'it'
    elif input_text == 'japanese':
        input_lang= 'ja'
    elif input_text == 'kannada':
        input_lang= 'kn'
    elif input_text == 'korean':
        input_lang= 'ko'
    elif input_text == 'malayalam':
        input_lang= 'ml'
    elif input_text == 'nepali':
        input_lang= 'ne'
    elif input_text == 'portuguesei':
        input_lang= 'pt'
    elif input_text == 'punjabi':
        input_lang= 'pa'
    elif input_text == 'russian':
        input_lang= 'ru'
    elif input_text == 'spanish':
        input_lang= 'es'
    elif input_text == 'tamil':
        input_lang= 'ta'
    elif input_text == 'telugu':
        input_lang= 'te'  
    elif input_text == 'turkish':
        input_lang= 'tr'
    elif input_text == 'urdu':
        input_lang= 'ur'  
    
    if output_language == 'arabic':
        output_lang= 'ar'
    elif output_language == 'bangla':
        output_lang= 'bn'
    elif output_language == 'chinese':
        output_lang= 'lzh'
    elif output_language == 'dutch':
        output_lang= 'nl'
    elif output_language == 'english':
        output_lang= 'en'
    elif output_language == 'french':
        output_lang= 'fr'
    elif output_language == 'german':
        output_lang= 'de'
    elif output_language == 'greek':
        output_lang= 'el'
    elif output_language == 'hindi':
        output_lang= 'hi'
    elif output_language == 'hungarian':
        output_lang= 'hu'
    elif output_language == 'indonesian':
        output_lang= 'id'
    elif output_language == 'irish':
        output_lang= 'ga'
    elif output_language == 'italian':
        output_lang= 'it'
    elif output_language == 'japanese':
        output_lang= 'ja'
    elif output_language == 'kannada':
        output_lang= 'kn'
    elif output_language == 'korean':
        output_lang= 'ko'
    elif output_language == 'malayalam':
        output_lang= 'ml'
    elif output_language == 'nepali':
        output_lang= 'ne'
    elif output_language == 'portuguesei':
        output_lang= 'pt'
    elif output_language == 'punjabi':
        output_lang= 'pa'
    elif output_language == 'russian':
        output_lang= 'ru'
    elif output_language == 'spanish':
        output_lang= 'es'
    elif output_language == 'tamil':
        output_lang= 'ta'
    elif output_language == 'telugu':
        output_lang= 'te'  
    elif output_language == 'turkish':
        output_lang= 'tr'
    elif output_language == 'urdu':
        output_lang= 'ur'  
        
    
    
    def text_to_speech(input_language, output_language, text):
        translation = translator.translate(text, src=input_lang, dest=output_lang)
        trans_text = translation.text
        tts = gTTS(trans_text, lang=output_lang, slow=False)
        try:
            my_file_name = text[0:20]
        except:
            my_file_name = "audio"
        tts.save(f"temp/{my_file_name}.mp3")
        return my_file_name, trans_text

    display_output_text = st.checkbox("Display output text")

    if st.button("convert"):
        result, output_text = text_to_speech(input_lang, output_lang, text)
        audio_file = open(f"temp/{result}.mp3", "rb")
        audio_bytes = audio_file.read()
        st.markdown(f"## Your audio:")
        st.audio(audio_bytes, format="audio/mp3", start_time=0)

        if display_output_text:
            st.markdown(f"## Output text:")
            st.write(f" {output_text}")


    def remove_files(n):
        mp3_files = glob.glob("temp/*mp3")
        if len(mp3_files) != 0:
            now = time.time()
            n_days = n * 86400
            for f in mp3_files:
                if os.stat(f).st_mtime < now - n_days:
                    os.remove(f)
                    print("Deleted ", f)


    remove_files(7)   

    st.markdown('---')
    
