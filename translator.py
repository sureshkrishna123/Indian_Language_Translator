import streamlit as st
import streamlit_webrtc as webrtc
import asyncio
import io
import glob
import os
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
    ("About Me","Language Translation","audio"),
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



  
if app_mode=='audio':
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
        audio_input = webrtc.audio_input()
        # Display the audio input component on the Streamlit app
        if audio_input:
            st.audio(audio_input)
        else:
            st.warning('No audio input found.')
    except:
        st.error("!! Please enter input in any language")

  st.markdown('---')
