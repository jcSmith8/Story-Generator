import voice
import story
from story import StoryInfo
from voice import read_story



newStory = StoryInfo(["John", "James"], "Chris", "California", "1980s", 3, "happy theme", 12)

newStory.print_story_type()

myStory = newStory.write_story()

newStory.generate_title()

print(newStory.title)
print(newStory.generatedStory)

read_story(newStory, "en")