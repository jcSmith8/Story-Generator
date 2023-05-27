import voice
import story
import voice2
from story import StoryInfo
from voice import read_story
from voice2 import generate_voice


#       StoryInfo(characters, mainchar, place, time, length, wordCount, theme, audience)
#newStory = StoryInfo(["John", "James"], "Chris", "California", "16 BC", 3, 1000, "happy theme", 12)
#newStory = StoryInfo(["John", "James"], "Chris", "Arizona", "2020s", 3, 500, "happy theme", 21)
#newStory = StoryInfo(["John", "James"], "Chris", "Europe", "1800s", 3, 600, "happy theme", 7)
newStory = StoryInfo(["John", "James"], "Chris", "Africa", "200s", 3, 200, "happy theme", 5)
#newStory.print_story_type()

myStory = newStory.write_story()

newStory.generate_title()

print(newStory.title)

print(newStory.chapters[0])

newStory.add_chapter()

print(newStory.chapters[1])

newStory.add_chapter()

print(newStory.chapters[2])

generate_voice(newStory, 1)

#read_story(newStory, "en", False)
