from dotenv import load_dotenv
import openai
import json
import os

load_dotenv()
openai.api_key = os.getenv('OPENAI_API')

class StoryInfo:
    def __init__(self, characters, mainchar, place, time, length, theme, audience):
        self.characters = characters
        self.mainchar = mainchar
        self.place = place
        self.time = time
        self.length = length
        self.theme = theme
        self.audience = audience
        
    def print_story_type(self):
        print("Your story will involve", self.characters, "with main character", self.mainchar, "\n")
        print("Your story will take place in", self.place, "during time period:", self.time, "\n")
        print("The story will have a theme of:", self.theme, "\n")
        
    def write_story(self):
        messages = [ {"role": "system", "content": "You are an intelligent assistant helping to write creative stories based on input criteria."} ]

        message = f'Write a short story that will take around {self.length} time to read. \n I want the story to involve these characters: {self.characters} and revolve around main character: {self.mainchar}. \n This story will take place during this time: {self.time}, and this place: {self.place}. \n The story will have an overall theme similar to {self.theme} and be friendly for all ages {self.audience} and above.'
            
        messages.append(
            {"role": "user", "content": message},
        )
        print("Your story is being generated . . . \n")
        chat = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo", messages = messages
        )
        reply = chat.choices[0].message.content
        print(f"ChatGPT: {reply}")
        return reply


newStory = StoryInfo(["John", "James"], "Chris", "California", "1980s", "5:23", "happy theme", 12)

newStory.print_story_type()

newStory.write_story()

#def generate_story():