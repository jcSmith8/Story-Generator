from gtts import gTTS
import os.path

### Reads the story with a specified language. Current available languages are here:
#   af: Afrikaans
#   ar: Arabic
#   bg: Bulgarian
#   bn: Bengali
#   bs: Bosnian
#   ca: Catalan
#   cs: Czech
#   da: Danish
#   de: German
#   el: Greek
#   en: English
#   es: Spanish
#   et: Estonian
#   fi: Finnish
#   fr: French
#   gu: Gujarati
#   hi: Hindi
#   hr: Croatian
#   hu: Hungarian
#   id: Indonesian
#   is: Icelandic
#   it: Italian
#   iw: Hebrew
#   ja: Japanese
#   jw: Javanese
#   km: Khmer
#   kn: Kannada
#   ko: Korean
#   la: Latin
#   lv: Latvian
#   ml: Malayalam
#   mr: Marathi
#   ms: Malay
#   my: Myanmar (Burmese)
#   ne: Nepali
#   nl: Dutch
#   no: Norwegian
#   pl: Polish
#   pt: Portuguese
#   ro: Romanian
#   ru: Russian
#   si: Sinhala
#   sk: Slovak
#   sq: Albanian
#   sr: Serbian
#   su: Sundanese
#   sv: Swedish
#   sw: Swahili
#   ta: Tamil
#   te: Telugu
#   th: Thai
#   tl: Filipino
#   tr: Turkish
#   uk: Ukrainian
#   ur: Urdu
#   vi: Vietnamese
#   zh-CN: Chinese (Simplified)
#   zh-TW: Chinese (Mandarin/Taiwan)
#   zh: Chinese (Mandarin)

def read_story(storyObject, lan, readSlow):
    if lan=="":
        language = "en"
    else:
        language = lan
        
    print("\n Generating story voiceover . . . \n")
    fullText = storyObject.title + " . . . . " + storyObject.generatedStory
    readThis = gTTS(text=fullText, lang = language, slow = readSlow)
    readThis.save(f'mp3_files/{storyObject.title}{lan}.mp3')
    
