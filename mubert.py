from dotenv import load_dotenv
import os
import story
from story import StoryInfo, random_story, random_init, access_saved_story
import httpx
import json
import requests
import urllib.request
import re
from bs4 import BeautifulSoup

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
    return download_link
    
downloadURL = create_mubert_song("cooper.smith@gmail.com", "+16501234567", "calm, soothing, slow tempo, background music.")

def download_from_url(mubert_url, song_name):
    url = f'{mubert_url}'
    file_extension = '.mp3'   # Example .wav
    r = requests.get(url)

    # If extension does not exist in end of url, append it
    if file_extension not in url.split("/")[-1]:
            filename = f'{last_url_path}{file_extension}'
    # Else take the last part of the url as filename
    else:
            filename = url.split("/")[-1]

    with open(f'mubert_mp3s/{song_name}.mp3', 'wb') as f:
            # You will get the file in base64 as content
            f.write(r.content)
    
    # r = requests.get(f'{mubert_url}')
    # soup = BeautifulSoup(r.content, 'html.parser')

    # for a in soup.find_all('a', href=re.compile(r'http.*\.mp3')):
    #     filename = a['href'][a['href'].rfind("/")+1:]
    #     print(f'opened: {filename} \n')
    #     doc = requests.get(a['href'])
    #     with open(f'mubert_mp3s/{filename}.mp3', 'wb') as f:
    #         f.write(doc.content)
            
download_from_url(downloadURL, "calm soothing background")