import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey=os.environ['apikey']
url=os.environ['url']

authenticator = IAMAuthenticator('4p2T0YDjO3gLrCfelTJe8LUrx8ZFa1r2M8xJ6mwvTNin')
language_translator = LanguageTranslatorV3(
    version='2018-01-05',
    authenticator=authenticator
)

language_translator.set_service_url(
    'https://api.us-south.language-translator.watson.cloud.ibm.com/instances/06df22ea-4740-4a9d-a4b3-d76e9dcaee77'
)


def english_to_french(english_text):

    "French to English Translator Function"

    translation = language_translator.translate(text=english_text, model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text


def french_to_english(french_text):

    "French to English Translator Function"

    translation = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text