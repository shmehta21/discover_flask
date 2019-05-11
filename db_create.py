from project import db
from project.models import BlogPost


#create the database and the db tables
db.create_all()

#insert
db.session.add(BlogPost("Good","I\'m good."))
db.session.add(BlogPost("Better","I\'m better."))
db.session.add(BlogPost("Best","I\'m best."))
db.session.add(BlogPost("postgres","We setup a local postgresql instance"))
db.session.add(BlogPost("hi","This is my first post on heroku"))
db.session.add(BlogPost("Heyya","I njoyed learning Heroku"))

#commit the changes
db.session.commit()