from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv
import vlc
from pydub import AudioSegment
import ffmpeg
import librosa

#HARD TO INSTALL FFMPEG
# Must install ffmpeg to your LOCAL environment, whatever you are in
# For me, I had to install it to my Conda environment (conda install ffmpeg)


load_dotenv()
api_key = os.getenv('IBM_API')
url_key = os.getenv('IBM_URL')

authenticator = IAMAuthenticator(api_key)
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url(url_key)


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

def get_audio_format(audioType):

    if(audioType == "alaw"):
        acceptAudio = 'audio/alaw'
    elif(audioType == "basic"):
        acceptAudio = 'audio/basic'
    elif(audioType == "flac"):
        acceptAudio = 'audio/flac'
    elif(audioType == "l16"):
        acceptAudio = 'audio/l16'
    elif(audioType == "mp3"):
        acceptAudio = 'audio/mp3'
    elif(audioType == "mpeg"):
        acceptAudio = 'audio/mpeg'
    elif(audioType == "mulaw"):
        acceptAudio = 'audio/mulaw'
    elif(audioType == "vorbis"):
        acceptAudio = 'audio/ogg;codec=vorbis'
    elif(audioType == "opus"):
        acceptAudio = 'audio/ogg;codecs=opus'
    elif(audioType == "ogg"):
        acceptAudio = 'audio/ogg'
    elif(audioType == "wav"):
        acceptAudio = 'audio/wav'
    elif(audioType == "webm"):
        acceptAudio = 'audio/webm'
    elif(audioType == "webm_opus"):
        acceptAudio = 'audio/webm;codecs=opus'
    else:
        print("\n\n if statements failed \n\n")
        acceptAudio = 'audio/wav'
    return acceptAudio

def generate_whole_voice(storyObject, audioType):
    
    authenticator = IAMAuthenticator(api_key)
    text_to_speech = TextToSpeechV1(
        authenticator=authenticator
    )

    text_to_speech.set_service_url(url_key)
    #current_chap = current_chap-1

    acceptAudio = get_audio_format(audioType)
    
    print("\n Generating Story Voiceover . . . \n")
    
    thisTitle = f'{storyObject.title}_audio_{audioType}.wav'
    
    with open(f'mp3_files/{thisTitle}','wb') as audio_file:
        audio_file.write(text_to_speech.synthesize(
            storyObject.wholeStory,
            voice = 'en-US_MichaelExpressive',
            accept = acceptAudio      
            ).get_result().content)
        
def generate_chapter_voice(storyObject, current_chap, audioType):
    
    authenticator = IAMAuthenticator(api_key)
    text_to_speech = TextToSpeechV1(
        authenticator=authenticator
    )

    text_to_speech.set_service_url(url_key)
    current_chap = current_chap-1
    
    acceptAudio = get_audio_format(audioType)

    print(f'\n Generating Chapter {current_chap} Voiceover . . . \n')

    thisTitle = f'{storyObject.title}_chapter_{current_chap}.wav'

    with open(f'mp3_files/{thisTitle}','wb') as audio_file:
        audio_file.write(text_to_speech.synthesize(
            storyObject.chapters[current_chap],
            voice = 'en-US_MichaelExpressive',
            accept = acceptAudio      
            ).get_result().content)
    voice_duration = int(librosa.get_duration(path=f'mp3_files/{thisTitle}'))+1
    print(f'This voice audio is {voice_duration} seconds long \n')
    storyObject.durations.append(voice_duration)
    return voice_duration
        
def compress_mp3(storyObject, chapterCount):
    infiles = []
    print("\n\n Compressing Chapters into 1 audio file . . . \n\n")
    i = 0
    while(i < chapterCount):
        
        infiles.append(f'mp3_files/{storyObject.title}_chapter_{i}.wav')

    outfile = f'mp3_files/{storyObject.title}_full_story.wav'

    data= []
    for infile in infiles:
        w = wave.open(infile, 'rb')
        data.append( [w.getparams(), w.readframes(w.getnframes())] )
        w.close()
        
    output = wave.open(outfile, 'wb')
    output.setparams(data[0][0])
    for i in range(len(data)):
        output.writeframes(data[i][1])
    output.close()
    
def vlc_player(storyObject):
    media = vlc.MediaPlayer(filename)
    media.play()

#vlc_player(f'"The Golden Tree's Wish"')

def compress_audio(storyObject, chapterCount):
    print("\n\n Compressing Chapters into 1 audio file . . . \n\n")
    combined_sounds = AudioSegment.from_file(f'mp3_files/{storyObject.title}_chapter_0.wav', format = 'wav')
    print(f' \n\n Total chapters to compress: {storyObject.chapterCount} \n\n')
    i = 1
    while(i < chapterCount):
        combined_sounds += AudioSegment.from_file(f'mp3_files/{storyObject.title}_chapter_{i}.wav', format = 'wav')
        i += 1
    combined_sounds.export("mp3_files/{storyObject.title}_FULL.wav", format="wav")


def slowdown_wav(filepath, percentage_val):
    audio = AudioSegment.from_file(filepath, format="wav")
    audio.speedup(playback_speed = percentage_val)
    audio.export(filepath, 'wav')



