from dotenv import load_dotenv
import openai
import json
import os
from gtts import gTTS
import random
import pickle

load_dotenv()
openai.api_key = os.getenv('OPENAI_API')


def access_saved_story(title):
    with open(f'txt_files/{title}.pkl', 'rb') as file:
        data = pickle.load(file)
        file.close()
    return data

# def show_story_info(StoryInfo):

def random_line(afile):
    line = next(afile)
    for num, aline in enumerate(afile, 2):
        if random.randrange(num):
            continue
        line = aline
    return line
    

# Randomly initializes a StoryInfo object with characters, main char... to write a good story
def random_init():
    messages = [ {"role": "system", "content": "You are an intelligent assistant helping to write creative stories based on input criteria."} ]
    
    rand_themes = open('static/txt_files/themes.txt').read().splitlines()
    rand_story_theme = random.choice(rand_themes)
    rand_audiences = open('static/txt_files/audiences.txt').read().splitlines()
    rand_story_audience = random.choice(rand_audiences)

    
    print("\n\n Randomizing a new StoryInfo object . . . \n\n")
<<<<<<< Updated upstream
    message = f'Instantiate a new StoryInfo object with random information to       \
        create an interesting story. I want you to include characters,    \
        main character, place, time, wordCount=500, theme, and audience. Here is a      \
        sample StoryInfo object: StoryInfo(["John", "James"], "Chris", "California",\
        "16 BC", 1000, "happy theme", 12). I want your output to be in the       \
        same format as this. Only include the instantiation in the reply, nothing else.'
=======
    message = f'I want you to generate random inputs for the following categories: \n\
        Character list (between 3 and 10 characters) \n\
        Main Character \n\
        Do not generate random data for wordCount, theme, or audience. These values will be set to \
        wordCount={wordCount}, theme={rand_story_theme}, audience = {rand_story_audience} \
        Generate a random setting: a city, destination, or landmark, and store it in the place parameter \
        Generate a random time period between 2000 BC and 3000 AD. It can be a historical event or a general time period. Store this value in the time parameter. \n\
        Please do not look at past conversations to determine the answer. \n\
        StoryInfo(characters, mainChar, place, time, wordCount, theme, audience) \n\
        I want your output to be in the exact same format as the line above. Keep all 7 parameters in the reply, with the correct name.  \
        The response should be the object only and on one line.'
>>>>>>> Stashed changes
        
    messages.append(
        {
            "role": "user", 
            "content": message
        },
    )
    chat = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo", 
        messages = messages,
        temperature=0.7
    )
    reply = chat.choices[0].message.content                
    print(reply)
    return reply


# Similar to random_init, but also generates the first chapter in the story
def random_story():
    
    messages = [ {"role": "system", "content": "You are an intelligent assistant helping to write creative stories based on input criteria."} ]

    message = f'Write a creative story that has around 500 words. \n                    \
    I want the story to involve random characters of your choosing, and revolve around  \
    a main character also of your choosing. \n This story will take place during a      \
    random time period between 0-2200, and a random place on Earth. \n The story will   \
    have an ongoing theme and also be friendly for children and young adult audiences   \
    Please leave the story open ended so we can add more chapters in the future.'

    messages.append(
        {
            "role": "user", 
            "content": message
        },
    )
    print("\n Your randomized story is being started . . . \n")
    chat = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo", 
        messages = messages,
        temperature=0.7
    )
    reply = chat.choices[0].message.content
    #print(f"ChatGPT: {reply}")
    #self.generatedStory = reply
    generatedStory = reply
    #self.chapters.append(self.generatedStory)
    #self.chapterCount += 1
    
    print("\n\n Populating new StoryInfo object . . . \n\n")
    message2 = f'Instantiate a new StoryInfo object with all of the information from \
        this previously generated random story: {generatedStory}. I want you to include characters,    \
        main character, place, time, wordCount, theme, and audience. Here is a      \
        sample StoryInfo object: StoryInfo(["John", "James"], "Chris", "California",\
        "16 BC", 1000, "happy theme", 12). I want your output to be in the       \
        same format as this. Do not include the story in the output reply.'
        
    messages.append(
        {
            "role": "user", 
            "content": message2
        },
    )
    chat = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo", 
        messages = messages,
        temperature=0.7
    )
    reply = chat.choices[0].message.content                
    print(reply)
    return reply



class StoryInfo:
    # Later on, will be initialized after submit button is pressed on the website
    def __init__(self, characters, mainchar, place, time, wordCount, theme, audience):
        print("\n\n New StoryInfo object created! \n\n")
        self.characters = characters
        self.mainchar = mainchar
        self.place = place
        self.time = time
        self.wordCount = wordCount
        self.theme = theme
        self.audience = audience
        self.chapters = []
        self.chapterCount = 0
        self.wholeStory = ''
        
    
    def print_story_type(self):
        print("\nCharacters:   ", self.characters, "\n\nMain character:   ", self.mainchar, "\n")
        print("Your story will take place in:   ", self.place, "during ", self.time, "\n")
        print("Story theme:", self.theme, "\n")
        print("Story audience:", self.audience, "\n")
        
    def print_all_story_info(self):
        print("Characters:   ", self.characters, "\nMain character:   ", self.mainchar, "\n")
        print("Your story will take place in:   ", self.place, "during ", self.time, "\n")
        print("Story theme:", self.theme, "\n")
        print("Story audience:", self.audience, "\n")
        i = 0
        chapterCount = 1
        for chap in self.chapters:
            print(f'\n\nChapter {chapterCount}: \n\n {self.chapters[i]}')
            i += 1
            chapterCount += 1
        
    def generate_title(self):
        messages = [ {"role": "system", 
                      "content": "You are a creative writer determining a title for a story."} 
                    ]
        
        message = f'Can you give this story a creative title in under 5 words? \n {self.generatedStory} \
        make sure that the title has no quotes around it. Make sure the title has no period afterwards'
        
        messages.append(
            {"role": "user", "content": message},
        )
        
        print("\n Your title is being created . . . \n")
        chat = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo", 
            messages = messages
        )
        reply = chat.choices[0].message.content
        #print(f"ChatGPT: {reply}")
        self.title = reply
        return reply
        
    def start_story(self):
        messages = [ {"role": "system", "content": "You are an intelligent assistant helping to write creative stories based on input criteria."} ]

        message = f'Write a creative story that has a minimum of {self.wordCount} words. \n \
        I want the story to involve these characters: {self.characters} and revolve around  \
        main character: {self.mainchar}. \n This story will take place during this time:    \
        {self.time}, and this place: {self.place}. \n The story will have an overall theme  \
        similar to {self.theme} and be friendly for {self.audience} audiences.     \
        Please make sure to keep the story as long as the word count describes.  \
        Please do not end the story. Leave it open   \
        ended so we can add more chapters in the future.'

        messages.append(
            {
                "role": "user", 
                "content": message
            },
        )
        print("\n Your story is being started . . . \n")
        chat = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo", 
            messages = messages,
            temperature=0.7
        )
        reply = chat.choices[0].message.content
        #print(f"ChatGPT: {reply}")
        self.generatedStory = reply
        self.chapters.append(self.generatedStory)
        self.chapterCount += 1
        
        return reply
    
    def add_chapter(self):
        messages = [ {
            "role": "system", 
            "content": "You are an intelligent assistant helping to write creative stories based on input criteria."
            } ]

        prev_chapter = self.chapters[len(self.chapters)-1]

        message = f'I want you to add to this existing story. Here is the previous chapter \
            of the story: {prev_chapter} I want you to write the next one. Please keep it around 500 words'
            
        messages.append(
            {"role": "user", "content": message},
        )
        self.chapterCount += 1
        print(f'Chapter {self.chapterCount} is being created . . . \n')
        chat = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo", 
            messages = messages,
            temperature=0.7
        )
        reply = chat.choices[0].message.content
        #print(f"ChatGPT: {reply}")
        self.generatedStory = reply
        self.chapters.append(self.generatedStory)
        self.save_story()
        return reply
    
    def compress_chapters(self):
        for chap in self.chapters:
            self.wholeStory += chap
            self.wholeStory += ("\n\n ---Next Chapter--- \n\n")
            

    def save_story(self):
        with open(f'txt_files/{self.title}.pkl', 'wb') as file:
            pickle.dump(self, file)
            file.close()

            

        

        
