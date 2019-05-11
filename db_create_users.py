from app import db
from models import User

# insert data
db.session.add(User('sagar', 'sagar@python.com','sagar@2019'))
db.session.add(User('admin', 'ad@admin.com','admin'))

#commit the changes
db.session.commit()