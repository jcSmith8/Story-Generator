from flask import Flask, render_template, request, url_for, redirect
from story import StoryInfo, random_story, random_init, access_saved_story, removeSpecialCharacters
import sqlite3
import os
from flask_sqlalchemy import SQLAlchemy
from distutils.log import debug
from fileinput import filename

basedir = os.path.abspath(os.path.dirname(__file__))

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
    stories_3 = Stories.query.limit(3).all()
    print(stories_3)
    return render_template('index.html', stories = stories_3)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/create', methods =["GET", "POST"])
def create():
    if request.method == "POST":
        # Create a table for the stories
        story_new = Stories(
            story_name= '', 
            place=request.form['place'], 
            time_period=request.form['time_period'], 
            characters=request.form['characters'], 
            main_character=request.form['place'],
            theme=request.form['theme'],
            cover=request.form['cover'] if request.form['cover'] != '' else '',
        )
        db.session.add(story_new)
        db.session.commit()
           
        return render_template('form2.html', story=story_new)
    
    return render_template('form.html')

@app.route('/create/stage2', methods =["GET", "POST"])
def create2():
    if request.method == "POST":
        # Create a table for the stories
        print(request.form)
        
        story_new_model = StoryInfo(
            characters=request.form['characters'],
            mainchar=request.form['place'],
            place= request.form['place'],
            time=request.form['time_period'],
            wordCount=request.form['word_count'],
            theme=request.form['theme'],
            audience=request.form['audience'],
        )
        story_new_model.start_story()
        story_new_model.generate_title()
        story_new_model.title = removeSpecialCharacters(story_new_model.title)
        
        story_new = Stories(
            title= story_new_model.title, 
            place= story_new_model.place, 
            time_period=story_new_model.time, 
            characters=story_new_model.characters, 
            main_character=story_new_model.mainchar,
            word_count=story_new_model.wordCount,
            theme=story_new_model.theme,
            audience=story_new_model.audience,
            cover=request.form['cover'] if request.form['cover'] != '' else '',
        )
        
        db.session.add(story_new)
        db.session.commit()
        
        print('new story id: ', story_new.id)
        story_new_model.story_id = story_new.id
        
        story_chapter_new = Chapters(
            story_id = story_new.id,
            chapter_count=len(story_new_model.chapters),
            content=story_new_model.chapters[-1]
        )
        db.session.add(story_chapter_new)
        db.session.commit()
           
        return render_template('form2.html', story=story_new_model)
        
    
    return redirect(url_for('create'))

@app.route('/create/stage3', methods =["GET", "POST"])
def create3():
    if request.method == "POST":
        # Create a table for the stories
        print(request.form)
        print(request.form['place'])
        return render_template('form3.html')
    
    return redirect(url_for('create'))

@app.route('/edit', methods =["GET", "POST"])
def edit():
    if request.method == "POST":
        # Create a table for the stories
        return render_template('form2.html')
    
    return render_template('form.html')

@app.route('/stories', methods =["GET", "POST"])
def stories():
    if request.method == "POST":
        # Create a table for the stories
        return render_template('form2.html')
    
    return render_template('form.html')

if __name__ == "__main__":
    os.system("python init_db.py")
    app.run(debug=True)
    


