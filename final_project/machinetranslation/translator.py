import os

from ibm_watson import LanguageTranslatorV3, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv



load_dotenv()

apikey = os.environ['apikey'] #SETTING API KEY FROM RAJDEEP'S IBM ACCOUNT
url = os.environ['url'] #SETTING URL FROM RAJDEEP'S IBM ACCOUNT

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)
language_translator.set_disable_ssl_verification(True)

def englishToFrench(english_text):
    """
    This function translates English to French
    """

    try:
        response = language_translator.translate(
            text=english_text,
            model_id='en-fr').get_result()
        french_text=response["translations"][0]["translation"]
        return french_text

    except ApiException as ex:
        print("Method failed with status code " + str(ex.code) + ": " + ex.message)

def frenchToEnglish(french_text):
    """
    This function translates French to English
    """

    try:
        response = language_translator.translate(
            text=french_text,
            model_id='fr-en').get_result()
        english_text=response["translations"][0]["translation"]
        return english_text

    except ApiException as ex:
        print("Method failed with status code " + str(ex.code) + ": " + ex.message)
