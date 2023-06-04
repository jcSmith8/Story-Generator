from flask import Flask, render_template, request, url_for, redirect
from story import StoryInfo, random_story, random_init, access_saved_story, removeSpecialCharacters
import sqlite3
import json
import os
from flask_sqlalchemy import SQLAlchemy
from distutils.log import debug
from voice2 import generate_chapter_voice, generate_whole_voice, compress_audio 
from mubert import regenerate_music_high_intensity, regenerate_music_med_intensity, regenerate_music_low_intensity, overlay_audio

basedir = os.path.abspath(os.path.dirname(__file__))
overlay_music = []
story_now = StoryInfo('','','','','','','')
app = Flask(__name__, template_folder='templates', static_url_path='/static')
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'story_database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Stories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=True)
    place = db.Column(db.String(50), nullable=False)
    time_period = db.Column(db.String(10), nullable=False)
    characters = db.Column(db.String(100), unique=True, nullable=False)
    main_character = db.Column(db.String(50), nullable=False)
    word_count = db.Column(db.Integer, nullable=False)
    theme = db.Column(db.String(30), nullable=False)
    audience = db.Column(db.String(30), nullable=False)
    cover = db.Column(db.String(30), nullable=True)
    
    def __init__(self, title, place, time_period, characters, main_character, word_count, theme, audience, cover = ''):
        self.title = title
        self.place = place
        self.time_period = time_period
        self.characters = characters
        self.main_character = main_character
        self.word_count = word_count
        self.theme = theme
        self.audience = audience
        self.cover = cover

    def __repr__(self):
        return f'<Story about {self.main_character} and {self.characters}  at {self.place} in {self.time_period}>'
    
class Chapters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    story_id = db.Column(db.Integer, db.ForeignKey('stories.id'))
    chapter_count = db.Column(db.Integer, nullable=True)
    content = db.Column(db.String(500), unique=True, nullable=False)
    
    def __init__(self, story_id, chapter_count, content):
        self.story_id = story_id
        self.chapter_count = chapter_count
        self.content = content
      
    
    def __repr__(self):
        return f'<Chapter {self.chapter_count} of story {self.story_id}>'

@app.route('/')
def index():
    print(request.root_url)
    stories_3 = Stories.query.limit(3).all()
    print(stories_3)
    return render_template('index.html', stories = stories_3)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/create', methods =["GET", "POST"])
def create():
    global story_now
    print(request.environ)
    route = request.environ['REQUEST_URI'].split('/')[-1]
    print(route)
    if request.method == "POST":
        # Create a table for the stories
        story_now = Stories(
            story_name= '', 
            place=request.form['place'], 
            time_period=request.form['time_period'], 
            characters=request.form['characters'], 
            main_character=request.form['place'],
            theme=request.form['theme'],
            cover=request.form['cover'] if request.form['cover'] != '' else '',
        )
        db.session.add(story_now)
        db.session.commit()
           
        return render_template('form2.html', story=story_now)
    
    return render_template('form.html')

@app.route('/create/stage2', methods =["GET", "POST"])
def create2():
    global story_now
    print(request.form)
    print(request.environ)
    route = request.environ['HTTP_REFERER'].split('/')[-1]
    print("POST FROM: ", route)
    if request.method == "POST":
        # Create a table for the stories
        
        
        if route == 'create':
            story_now = StoryInfo(
                characters=request.form['characters'],
                mainChar=request.form['main_character'],
                place= request.form['place'],
                time=request.form['time_period'],
                wordCount=request.form['word_count'],
                theme=request.form['theme'],
                audience=request.form['audience'],
            )
            story_now.start_story()
            story_now.generate_title()
            story_now.title = removeSpecialCharacters(story_now.title)
            
            story_new = Stories(
                title= story_now.title, 
                place= story_now.place, 
                time_period=story_now.time, 
                characters=','.join(story_now.characters), 
                main_character=story_now.mainChar,
                word_count=story_now.wordCount,
                theme=story_now.theme,
                audience=story_now.audience,
                cover = '' if not 'cover' in request.form.keys else request.form['cover']
            )
            
            db.session.add(story_new)
            db.session.commit()
            
            print('new story id: ', story_new.id)
            story_now.story_id = story_new.id
            
            story_chapter_new = Chapters(
                story_id = story_new.id,
                chapter_count=len(story_now.chapters),
                content=story_now.chapters[-1]
            )
            db.session.add(story_chapter_new)
            db.session.commit()
            
            return render_template('form2.html', story=story_now)
        elif route == 'random':
            random_start = random_init(request.form['word_count'])
            story_now = eval(random_start)

            story_now.print_story_type()

            story_now.start_story()
            story_now.generate_title()
            story_now.title = removeSpecialCharacters(story_now.title)
            
            story_new = Stories(
                title=story_now.title, 
                place=story_now.place, 
                time_period=story_now.time, 
                characters=','.join(story_now.characters), 
                main_character=story_now.mainChar,
                word_count=story_now.wordCount,
                theme=story_now.theme,
                audience=story_now.audience,
                cover='' if 'cover' not in request.form.keys() else request.form['cover']
            )
            
            db.session.add(story_new)
            db.session.commit()
            
            print('new story id: ', story_new.id)
            story_now.story_id = story_new.id
            
            story_chapter_new = Chapters(
                story_id = story_new.id,
                chapter_count=len(story_now.chapters),
                content=story_now.chapters[-1]
            )
            db.session.add(story_chapter_new)
            db.session.commit()
            return render_template('form2.html', story=story_now)
        else:
            story_now.add_chapter()
            story_chapter_new = Chapters(
                story_id = story_now.story_id,
                chapter_count=len(story_now.chapters),
                content=story_now.chapters[-1]
            )
            db.session.add(story_chapter_new)
            db.session.commit()
            return render_template('form2.html', story=story_now)
        
    if story_now == None:
        return redirect(url_for('create'))
    else:
        return render_template('form2.html', story=story_now)

@app.route('/create/stage3', methods =["GET", "POST"])
def create3():
    global story_now
    route = request.environ['HTTP_REFERER'].split('/')[-1]
    print("POST FROM: ", route)
    print(request.data.decode('utf-8'))

    if request.method == "POST":
        # Create a table for the stories
        if route == 'stage2':
            print(request.form)
            voice_chapter_duration = generate_chapter_voice(story_now, len(story_now.chapters), 'wav')
            return render_template('form3.html', story = story_now, overlays = [])
        elif route == 'stage3':
            if  request.get_json():
                story_now.add_chapter()
                story_chapter_new = Chapters(
                    story_id = story_now.story_id,
                    chapter_count=len(story_now.chapters),
                    content=story_now.chapters[-1]
                )
                db.session.add(story_chapter_new)
                db.session.commit()
                return render_template('form3.html', story = story_now, overlays = [])
            else:
                regenerate_music_low_intensity(story_now, story_now.chapterCount)
                regenerate_music_med_intensity(story_now, story_now.chapterCount)
                regenerate_music_high_intensity(story_now, story_now.chapterCount)
                return render_template('form3.html', story = story_now, overlays = [])
            
                
    
    return redirect(url_for('create'))

@app.route('/create/stage4', methods =["GET", "POST"])
def create4():
    global story_now
    global overlay_music
    #print(json.dumps(request.json["overlay"]))
    if request.method == "POST":
        print("creating overlay ...")
        overlay_audio(story_now, f'static/mp3_files/{story_now.title}_chapter_{story_now.chapterCount-1}.wav', request.json["overlay"])
        overlay_music = [request.json["overlay"][:-4].replace('static/mubert_mp3s/','') + "_soft.wav",request.json["overlay"][:-4].replace('static/mubert_mp3s/','') + "_softer.wav"]
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 
    
    return render_template('form_overlay.html', story = story_now, overlays = overlay_music)

@app.route('/create/random', methods =["GET", "POST"])
def random():
    if request.method == "POST":
        # Create a table for the stories
        return redirect(url_for('index'))
    
    return render_template('random.html')

@app.route('/stories', methods =["GET"])
def stories():
    stories = Stories.query.all()
    return render_template('stories.html', stories = stories)

@app.route('/stories/<story_name>', methods =["GET"])
def story(story_name):
    story = Stories.query.filter_by(title = story_name).first()
    chapters = Chapters.query.filter_by(story_id = story.id).all()
    print(story)
    print(chapters)
    return render_template('story.html', story = story, chapters = chapters)

@app.route('/stories/<story_name>/edit', methods =["GET", "POST"])
def edit(story_name):
    story = Stories.query.filter_by(title = story_name).first()
    chapters = Chapters.query.filter_by(story_id = story.id).all()
    if request.method == "POST":
        # Create a table for the stories
        return render_template('form2.html')
    
    return render_template('edit.html', story = story, chapters = chapters)

if __name__ == "__main__":
    os.system("python init.py")
    os.system("python init_db.py")
    app.run(debug=True)
    


