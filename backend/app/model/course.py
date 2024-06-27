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

class Classes(db.Document):
    user = db.ReferenceField(User)
    course = db.StringField(required=True)
    type = db.StringField(required=True)
    sks = db.IntField(required=True)
    date = db.DateTimeField(required=True)
    room = db.StringField(required=False)
    online_class = db.StringField(required=False)
    lecture = db.StringField(required=True)