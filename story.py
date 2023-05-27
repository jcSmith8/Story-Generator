from dotenv import load_dotenv
import openai
import json
import os
from gtts import gTTS


load_dotenv()
openai.api_key = os.getenv('OPENAI_API')

class StoryInfo:
    # Later on, will be initialized after submit button is pressed on the website
    def __init__(self, characters, mainchar, place, time, length, wordCount, theme, audience):
        self.characters = characters
        self.mainchar = mainchar
        self.place = place
        self.time = time
        self.length = length
        self.wordCount = wordCount
        self.theme = theme
        self.audience = audience
        self.chapters = []
        
    def print_story_type(self):
        print("Characters:", self.characters, "Main character", self.mainchar, "\n")
        print("Your story will take place in", self.place, "during time period:", self.time, "\n")
        print("Story theme:", self.theme, "\n")
        print("Story audience:", self.audience, "\n")
        
    def generate_title(self):
        messages = [ {"role": "system", "content": "You are a creative writer determining a title for a story."} ]
        
        message = f'Can you give this story a creative title in under 5 words? \n {self.generatedStory}'
        
        messages.append(
            {"role": "user", "content": message},
        )
        
        print("Your title is being generated . . . \n")
        chat = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo", 
            messages = messages
        )
        reply = chat.choices[0].message.content
        #print(f"ChatGPT: {reply}")
        self.title = reply
        return reply
        
    def write_story(self):
        messages = [ {"role": "system", "content": "You are an intelligent assistant helping to write creative stories based on input criteria."} ]

        message = f'Write a creative story that has a minimum of {self.wordCount} words. \n \
        I want the story to involve these characters: {self.characters} and revolve around  \
        main character: {self.mainchar}. \n This story will take place during this time:    \
        {self.time}, and this place: {self.place}. \n The story will have an overall theme  \
        similar to {self.theme} and be friendly for audiences that are {self.audience}      \
        years old. Please make sure to keep the story as long as the word count describes.  \
        If the word count is greater than 500, please do not end the story. Leave it open   \
        ended so we can add more chapters in the future.'

        messages.append(
            {"role": "user", "content": message},
        )
        print("Your story is being generated . . . \n")
        chat = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo", 
            messages = messages,
            temperature=0.7
        )
        reply = chat.choices[0].message.content
        #print(f"ChatGPT: {reply}")
        self.generatedStory = reply
        self.chapters.append(self.generatedStory)
        
        return reply
    
    def add_chapter(self):
        messages = [ {"role": "system", "content": "You are an intelligent assistant helping to write creative stories based on input criteria."} ]

        prev_chapter = self.chapters[len(self.chapters)-1]

        message = f'I want you to add to this existing story. Here is the previous chapter \
            of the story: {prev_chapter} I want you to write the next one. Please keep it around 500 words'
            
        messages.append(
            {"role": "user", "content": message},
        )
        print("Your chapter is being added . . . \n")
        chat = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo", 
            messages = messages,
            temperature=0.7
        )
        reply = chat.choices[0].message.content
        #print(f"ChatGPT: {reply}")
        self.generatedStory = reply
        self.chapters.append(self.generatedStory)
        
        return reply
        
    #def end_story(self):
        
