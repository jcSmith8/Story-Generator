from datetime import date
from app import app, db, Stories, Chapters

with app.app_context():
    db.drop_all()
    db.create_all()

    story1 = Stories(
        title = 'A Music Festival in the Bob Valley',
        place = "Texas",
        time_period = "2023",
        characters = "Bob the Builder, Bob Dylan, Bob Sponge",
        main_character = "Sponge Bob Square Pants",
        word_count = 100,
        theme = "drama",
        audience = "k-12",
        cover = 'sample1.png'
    )

    story2 = Stories(
        title = 'Hola Mis Amigos',
        place = "Rio",
        time_period = "2016",
        characters = "The Migos, Juan Martinex, Rosario Ecuador",
        main_character = "Xavier Sanchez",
        word_count = 100,
        theme = "adventure",
        audience = "PG13",
        cover = 'sample2.png'
    )
    
    story3 = Stories(
        title = 'We are Family',
        place = "Atlanta",
        time_period = "2019",
        characters = "Vin Diesel, Dwayne Johnson, Han Lue",
        main_character = "Brian O'Conner",
        word_count = 100,
        theme = "adventure",
        audience = "PG13",
        cover = ''
    )

    db.session.add_all([story1, story2, story3])
    db.session.commit()

    story1_chapter1 = Chapters(
        story_id=story1.id,
        chapter_count=1,
        content='Hello from the other side ~~~'
    )

    story1_chapter2 = Chapters(
        story_id=story1.id,
        chapter_count=1,
        content='I must have called it a thousand time ~~~'
    )

    story2_chapter1 = Chapters(
        story_id=story2.id,
        chapter_count=1,
        content='Go e~~~azy on me babe ~~~'
    )
    
    story3_chapter1 = Chapters(
        story_id=story3.id,
        chapter_count=1,
        content='It\'s been a long day, without you, my friend ~~~'
    )

    db.session.add_all([story1_chapter1, story1_chapter2, story2_chapter1, story3_chapter1])
    db.session.commit()
    
    print("finished initializing DB ...")