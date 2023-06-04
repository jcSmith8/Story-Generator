
import os
dir_to_clear = ['txt_files', 'static/mp3_files','static/mubert_mp3s', 'static/overlay_wavs']
for dir in dir_to_clear:
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))
 