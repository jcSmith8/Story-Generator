import voice
import story
import voice2
from story import StoryInfo, random_story, random_init, access_saved_story
from voice import read_story
from voice2 import generate_chapter_voice, generate_whole_voice, compress_audio
import pickle
import mubert
from mubert import overlay_two_wavs, overlay_audio, generate_mubert_token, create_mubert_song, track_mubert_status, download_audio, regenerate_music_low_intensity, regenerate_music_med_intensity, regenerate_music_high_intensity


# StoryInfo(characters, mainchar, place, time, length, wordCount, theme, audience)
newStory = StoryInfo(["John", "James"], "Chris", "California", "16 BC", 1000, "happy theme", 12)
newStory.chapterCount = 2
newStory.title = "Betrayed A Roaring Revenge"
newStory.mubertPrompt = "calm, soothing"
regenerate_music_low_intensity(newStory, 1)
# compress_audio(newStory)
#newStory = StoryInfo(["John", "James"], "Chris", "Arizona", "2020s", 3, 500, "happy theme", 21)
#newStory = StoryInfo(["John", "James"], "Chris", "Europe", "1800s", 3, 600, "happy theme", 7)
#newStory = StoryInfo(["John", "James"], "Chris", "Africa", "200s", 3, 200, "happy theme", 5)
#newStory.print_story_type()


# initializes a random StoryInfo() call with random info
# random_init = random_init(300)
# randomStory = eval(random_init)
# randomStory.print_story_type()

# # starts first chapter of the story
# # openai generates a title and music generation prompt based on the first chapter
# randomStory.start_story()
# randomStory.generate_title()

# # generating the voice sample for chapter 1. Typically takes 1-2 minutes depending on wordCount
# voice_duration_chap_1 = generate_chapter_voice(randomStory, 1, 'wav')

# # adds another chapter to the story. Must be called AFTER start_story(), we must have a first chapter to write based on
# #### randomStory.add_chapter()

# #generating voice for chapter 2. Duration of voice recording will be passed into create_mubert_song to correlate durations
# #voice_duration_chap_2 = generate_chapter_voice(randomStory, 2, 'wav')


# #compress_audio(randomStory, 2)

# downloadURL = create_mubert_song(randomStory.mubertPrompt, voice_duration_chap_1, f'low')
# download_audio(downloadURL, f'mubert_mp3s/', f'{randomStory.title}')
# overlay_audio(randomStory, f'mp3_files/{randomStory.title}_chapter_0.wav', f'mubert_mp3s/{randomStory.title}.wav')
# overlay_two_wavs(f'static/mp3_files/Eternal Small Town Bonds_chapter_0.wav', f'static/mubert_mp3s/Eternal Small Town Bonds_medium.wav')
# regenerate_music_low_intensity(randomStory, 1)
# regenerate_music_med_intensity(randomStory, 1)
# regenerate_music_high_intensity(randomStory, 1)

# #randomStory.add_chapter()
# #generate_chapter_voice(randomStory, 3, 'wav')
#newStory = access_saved_story("New York Mysteries Uncovered.")

#story_stuff.print_all_story_info()
#myStory = newStory.start_story()

#newStory.generate_title()

#print(newStory.title)

#print(newStory.chapters[0])

#newStory.add_chapter()

#print(newStory.chapters[1])

# newStory.add_chapter()

# newStory.compress_chapters()
# #print(newStory.chapters[2])

# generate_chapter_voice(newStory, 1, 'wav')
# generate_chapter_voice(newStory, 2, 'wav')
# generate_chapter_voice(newStory, 3, 'wav')

# compress_audio(newStory, 3)
#generate_voice(newStory, 1, 'opus')
#generate_voice(newStory, 1, 'basic')

#read_story(newStory, "en", False)
