import voice
import story
import voice2
from story import StoryInfo, random_story, random_init, access_saved_story
from voice import read_story
from voice2 import generate_chapter_voice, generate_whole_voice, compress_audio
import pickle

#       StoryInfo(characters, mainchar, place, time, length, wordCount, theme, audience)
#newStory = StoryInfo(["John", "James"], "Chris", "California", "16 BC", 3, 1000, "happy theme", 12)
#newStory = StoryInfo(["John", "James"], "Chris", "Arizona", "2020s", 3, 500, "happy theme", 21)
#newStory = StoryInfo(["John", "James"], "Chris", "Europe", "1800s", 3, 600, "happy theme", 7)
#newStory = StoryInfo(["John", "James"], "Chris", "Africa", "200s", 3, 200, "happy theme", 5)
#newStory.print_story_type()

# random_init = random_init()
# randomStory = eval(random_init)

# randomStory.print_story_type()

# randomStory.start_story()
# randomStory.generate_title()
# generate_chapter_voice(randomStory, 1, 'wav')
# randomStory.add_chapter()
# randomStory.save_story()
# generate_chapter_voice(randomStory, 2, 'wav')
# #randomStory.add_chapter()
# #generate_chapter_voice(randomStory, 3, 'wav')


# compress_audio(randomStory, 3)

story_stuff = access_saved_story("New York Mysteries Uncovered.")

story_stuff.print_all_story_info()
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
