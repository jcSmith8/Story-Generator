from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('IBM_API')
url_key = os.getenv('IBM_URL')

authenticator = IAMAuthenticator(api_key)
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url(url_key)

with open(f'mp3_files/filename.wav','wb') as audio_file:
    audio_file.write(text_to_speech.synthesize('This story will be about a collection of stories.',voice='en-US_MichaelExpressive',accept='audio/mp3').get_result().content)
    

### EXPRESSIVE NEURAL VOICES:
#   en-AU_HeidiExpressive
#   en-AU_JackExpressive
#   en-US_AllisonExpressive
#   en-US_EmmaExpressive
#   en-US_LisaExpressive
#   en-US_MichaelExpressive
#   
### ENHANCED NEURAL VOICES
#   nl-NL_MerelV3Voice
#   en-GB_CharlotteV3Voice
#   en-GB_JamesV3Voice
#   en-GB_KateV3Voice
#   en-US_AllisonV3Voice
#   en-US_EmilyV3Voice
#   en-US_HenryV3Voice
#   en-US_KevinV3Voice
#   en-US_LisaV3Voice
#   en-US_MichaelV3Voice
#   en-US_OliviaV3Voice
#   fr-CA_LouiseV3Voice
#   fr-FR_NicolasV3Voice
#   fr-FR_ReneeV3Voice
#   de-DE_BirgitV3Voice
#   de-DE_DieterV3Voice
#   de-DE_ErikaV3Voice
#   it-IT_FrancescaV3Voice
#   ja-JP_EmiV3Voice
#   ko-KR_JinV3Voice
#   pt-BR_IsabelaV3Voice
#   es-ES_EnriqueV3Voice
#   es-ES_LauraV3Voice
#   es-LA_SofiaV3Voice
#   es-US_SofiaV3Voice

def generate_voice(storyObject, current_chap):
    authenticator = IAMAuthenticator(api_key)
    text_to_speech = TextToSpeechV1(
        authenticator=authenticator
    )

    text_to_speech.set_service_url(url_key)
    current_chap = current_chap-1
    
    print("Story voiceover generating . . .")
    
    with open(f'mp3_files/{storyObject.title}_chapter_{current_chap}.wav','wb') as audio_file:
        audio_file.write(text_to_speech.synthesize(
            storyObject.chapters[current_chap],
            voice='en-US_MichaelExpressive',
            accept='audio/mp3'      
            ).get_result().content)
    