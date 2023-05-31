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
from time import sleep
import urllib.request
import pydub
from pydub import AudioSegment
from pydub.playback import play

MUBERT_TOKEN = os.getenv('MUBERT_TOKEN')
MUBERT_COMPANY = os.getenv('MUBERT_COMPANY')
MUBERT_LICENSE = os.getenv('MUBERT_LICENSE')
#url = "https://api.mubert.com/v2/{MUBERT_COMPANY}"
#email = "cooper@gmail.com" #@param {type:"string"}
#pat = Y29vcGVyc21pdGgwODA4LjE5NTcwNTYyLmEzOGUzOTcxNTEwNTJhZGFhN2RiZTU1MTBkMTVhZmE1OGYxOThiYmQuMS4z.973aa6032378e159a6611624b987426ea833c26194f02fd5a4ee6ea44305a9d0
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


def create_mubert_song(mubert_prompt, duration, intensity):
    token = generate_mubert_token("coopersmith@gmail.com", "+16501234567")
    r = httpx.post('https://api-b2b.mubert.com/v2/TTMRecordTrack', 
    json={
            "method":"TTMRecordTrack",
            "params":
            {
                "text":f'{mubert_prompt}',
                #"pat":f'{token}',
                "pat":f'{token}',
                "mode":"track",
                "duration":duration,
                "intensity":f'{intensity}',
                "format":"wav", 
                "bitrate":"192" ,
                "mode":"loop"
            }
        })
    rdata = json.loads(r.text)
    #print(f'CREATEMUBERT ALL: {rdata} \n')
    assert rdata['status'] == 1, "failed to load"
    
    generation_progress = rdata['data']['tasks'][0]['task_status_code']
    this_task_id = rdata['data']['tasks'][0]['task_id']
    
    print(f'CREATEMUBERT: {generation_progress}')
    
    if generation_progress == 1:
        print("Task in Progress \n")
        in_progress = True
    while(in_progress):
        if(track_mubert_status(this_task_id, token) == 1):
            print("\n waiting until track is done . . . \n")
            sleep(5)
        else:
            break
    full_path = f'mubert_mp3s/' + f'TEMP_FILE_NAME' + '.wav'
    download_url = track_mubert_status(this_task_id, token)
    urllib.request.urlretrieve(download_url, full_path)
    print(download_url)
    return download_url
    
def track_mubert_status(task_id, token):
    #token = generate_mubert_token("coopersmith@gmail.com", "+16501234567")
    
    r = httpx.post('https://api-b2b.mubert.com/v2/TrackStatus',
    json={
        "method":"TrackStatus",
        "params":
        {
            "pat":f'{token}'
        }
    })
    rdata = json.loads(r.text)
    
    # Parse task list to find correct task by Task_ID
    for task in rdata['data']['tasks']:
        if(task['task_id'] == task_id):
            print("FOUND THE TASK \n")
            progress =  task['task_status_text'] 
            task_id = task['task_id']
            task_status = task['task_status_code']
            download_link = task['download_link']
            
    # print(f'TRACKMUBERT: {task_status} \n')
    # print(f'TRACKMUBERT: {progress} \n')
    # print(f'TRACKMUBERT: {task_id} \n')
    #print(rdata)
    if(task_status == 1):
        return 1
    else:
        # print(f'TRACKMUBERT: {progress} \n')
        # print(f'Got download link: {download_link} \n')
        return download_link

def download_audio(url, file_path, file_name):
    full_path = file_path + file_name + '.wav'
    urllib.request.urlretrieve(url, full_path)
    
    
def overlay_audio(StoryInfoObj, voice_file, music_file):
    voice_seg = AudioSegment.from_wav(f'{voice_file}')
    music_seg = AudioSegment.from_wav(f'{music_file}')

    soft_music_seg = music_seg - 10
    softer_music_seg = music_seg - 17
    overlay_soft = voice_seg.overlay(soft_music_seg, position=0)
    overlay_softer = voice_seg.overlay(softer_music_seg, position=0)
    fileName = os.path.basename(os.path.normpath(music_file))
    fileNameTuple = os.path.splitext(fileName)
    fileName = fileNameTuple[0]
    overlay_soft.export(f'overlay_wavs/{fileName}_soft.wav', format="wav")
    overlay_softer.export(f'overlay_wavs/{fileName}_softer.wav', format="wav")
    
    
def regenerate_music_low_intensity(StoryInfoObj, chapter):
    i = chapter-1    
    StoryInfoObj.regenerate_mubert()
    downloadURL = create_mubert_song(StoryInfoObj.mubertPrompt, StoryInfoObj.durations[i], f'low')
    download_audio(downloadURL, f'mubert_mp3s/', f'{StoryInfoObj.title}_low')
    overlay_audio(StoryInfoObj, f'mp3_files/{StoryInfoObj.title}_chapter_{i}.wav', f'mubert_mp3s/{StoryInfoObj.title}_low.wav')
    
def regenerate_music_med_intensity(StoryInfoObj, chapter):
    i = chapter-1    
    StoryInfoObj.regenerate_mubert()
    downloadURL = create_mubert_song(StoryInfoObj.mubertPrompt, StoryInfoObj.durations[i], f'medium')
    download_audio(downloadURL, f'mubert_mp3s/', f'{StoryInfoObj.title}_medium')
    overlay_audio(StoryInfoObj, f'mp3_files/{StoryInfoObj.title}_chapter_{i}.wav', f'mubert_mp3s/{StoryInfoObj.title}_medium.wav')
    
def regenerate_music_high_intensity(StoryInfoObj, chapter):
    i = chapter-1    
    StoryInfoObj.regenerate_mubert()
    downloadURL = create_mubert_song(StoryInfoObj.mubertPrompt, StoryInfoObj.durations[i], f'high')
    download_audio(downloadURL, f'mubert_mp3s/', f'{StoryInfoObj.title}_high')
    overlay_audio(StoryInfoObj, f'mp3_files/{StoryInfoObj.title}_chapter_{i}.wav', f'mubert_mp3s/{StoryInfoObj.title}_high.wav')
    

    
#mubert_prompt = f'Violin, Piano, Saxophone  , Struggle between passion and security , Paris, France (Roaring Twenties)'
#pat_id = generate_mubert_token("coopersmith@gmail.com", "+16501234567")             
#downloadURL = create_mubert_song(mubert_prompt, 120, f'low')
#download_audio(downloadURL, f'mubert_mp3s/', f'{mubert_prompt}')

#overlay_audio(f'mp3_files/African Journey Meeting Chris_chapter_0.wav', f'mubert_mp3s/NEW_FILE22.wav')