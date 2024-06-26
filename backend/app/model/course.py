from utils import db
from model.user import User

class Course(db.Document):
    user = db.ReferenceField(User)
    kode_mk = db.StringField(required=True, unique=True)
    semester = db.StringField(required=True)
    nama_mk = db.StringField(required=False)
    sks = db.IntField(required=False)
    description = db.StringField(required=False)
    
class Bulletin(db.Document):
    user = db.ReferenceField(User)
    title = db.StringField(required=True)
    content =  db.StringField(required=False)
    author = db.StringField(required=True)
    date = db.DateField(required=False)
    # course = db.ReferenceField(Course)