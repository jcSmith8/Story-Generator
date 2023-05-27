import voice
import story
from story import StoryInfo
from voice import read_story


#       StoryInfo(characters, mainchar, place, time, length, wordCount, theme, audience)
#newStory = StoryInfo(["John", "James"], "Chris", "California", "16 BC", 3, 1000, "happy theme", 12)
#newStory = StoryInfo(["John", "James"], "Chris", "Arizona", "2020s", 3, 500, "happy theme", 21)
#newStory = StoryInfo(["John", "James"], "Chris", "Europe", "1800s", 3, 600, "happy theme", 7)
newStory = StoryInfo(["John", "James"], "Chris", "Africa", "200s", 3, 500, "happy theme", 5)
#newStory.print_story_type()

myStory = newStory.write_story()

newStory.generate_title()

print(newStory.title)

print(newStory.chapters[0])

newStory.add_chapter()

print(newStory.chapters[1])

newStory.add_chapter()

print(newStory.chapters[2])

#read_story(newStory, "en", False)
