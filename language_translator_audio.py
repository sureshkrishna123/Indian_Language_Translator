
from IPython.display import Audio
#import librosa
import googletrans
#import torch
#import os
from googletrans import Translator
#import soundfile
import speech_recognition as sr
#import pyaudio


def speech_to_text(audio_input,language_code):
    try:
        #audio,sr= librosa.load(audio_input)
        speech = sr.Recognizer()
        # Reading Audio file as source
        # listening the audio file and store in text variable
        # Give your file name with path

        with sr.AudioFile(audio_input) as source:
           text = speech.listen(source)

        #recoginize_() method will throw a request error if the API is unreachable or unable to
        #recogonize or match the words, hence using exception handling

           text_output = speech.recognize_google(text,language=language_code)  # By default, it converts the speech into english

        if language_code=='en':
            return {'transcript': text_output}
        else:
            # if language_code is not english, using googletrans library we will translate to english
            translater = Translator()
            out = translater.translate(text_output, dest='en')
            text_output=out.text
            return {'transcript': text_output}

    except FileNotFoundError:
        return {'error': 'Audio file not found'}
    except AttributeError as e:
        return {'error': str(e)}
    except ValueError as e:
        return {'error': str(e)}
    except Exception as e:
        return {'error': str(e)}



if __name__ == '__main__':
    #example on how we should give input parameters.
    audio_path='en.wav'
    lang='en'
    try:
        output_dict = speech_to_text(audio_path,lang)
        print(output_dict)

    except Exception as e:
        print("Error:", str(e))
