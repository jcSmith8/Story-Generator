from dotenv import load_dotenv
import os
import story
from story import StoryInfo, random_story, random_init, access_saved_story
import httpx
import json

MUBERT_TOKEN = os.getenv('MUBERT_TOKEN')
MUBERT_COMPANY = os.getenv('MUBERT_COMPANY')
MUBERT_LICENSE = os.getenv('MUBERT_LICENSE')
#url = "https://api.mubert.com/v2/{MUBERT_COMPANY}"
#email = "cooper@gmail.com" #@param {type:"string"}

# phone must be of form +16501234567 (+ and then 10 numbers)
def generate_mubert_token(email, phone):
    r = httpx.post('https://api-b2b.mubert.com/v2/GetServiceAccess', 
    json={
        "method":"GetServiceAccess",
        "params": 
        {
            "email": email,
            "phone": phone,
            "license":f'{MUBERT_LICENSE}',
            "token":f'{MUBERT_TOKEN}'
        }
    })

    rdata = json.loads(r.text)
    assert rdata['status'] == 1, "probably incorrect e-mail"
    pat = rdata['data']['pat']
    print(f'Got token: {pat} \n')
    return pat
    
#create_new_mubert_user("coopersmith@gmail.com", "+16501234567")

def create_mubert_song(email, phone, mubert_prompt):
    token = generate_mubert_token(email, phone)
    r = httpx.post('https://api-b2b.mubert.com/v2/TTMRecordTrack', 
    json={
            "method":"TTMRecordTrack",
            "params":
            {
                "text":f'{mubert_prompt}',
                "pat":f'{token}',
                "mode":"track",
                "duration":"60", 
                "bitrate":"192" ,
                "mode":"loop"
            }
        })
    rdata = json.loads(r.text)
    print(rdata, "\n")
    assert rdata['status'] == 1, "failed to load"
    download_link = rdata['data']['tasks'][0]['download_link']
    print(f'Got download link: {download_link} \n')
    
create_mubert_song("cooper.smith0808@gmail.com", "+16501234567")