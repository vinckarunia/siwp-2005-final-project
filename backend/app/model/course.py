
from utils import db
from model.user import User

class Course(db.Document):
    user = db.ReferenceField(User)
    kode_mk = db.StringField(required=True, unique=True)
    semester = db.StringField(required=True)
    nama_mk = db.StringField(required=False)
    sks = db.IntField(required=False)
    description = db.StringField(required=False)
    
class News(db.Document):
    user = db.ReferenceField(User)
    title = db.StringField(required=True)
    content =  db.StringField(required=False)
 

class Exam(db.Document):
    user = db.ReferenceField(User)
    kode_mk = db.StringField(required=True, unique=True)
    course = db.StringField(required=True)
    date = db.DateTimeField(required=True)
    room = db.StringField(required=False)

class CampusEvent(db.Document):
    user = db.ReferenceField(User)
    title = db.StringField(required=True)
    date = db.DateTimeField(required=True)
    time = db.StringField(required=True)
    location = db.StringField(required=True)
   
