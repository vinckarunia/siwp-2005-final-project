
from utils import db
from model.user import User

class Course(db.Document):
    user = db.ReferenceField(User)
    kode_mk = db.StringField(required=True, unique=True)
    semester = db.StringField(required=True)
    nama_mk = db.StringField(required=False)
    sks = db.IntField(required=False)
    description = db.StringField(required=False)
    
class InputKRS(db.Document):
    user = db.ReferenceField(User)
    course = db.StringField(required=True)
    sks = db.StringField(required=True)
    day = db.DateField(required=False)
    kelas = db.StringField(required=True)
    type = db.StringField(required=True)
    room = db.StringField(required=True)
    
class Softskill(db.Document):
    user = db.ReferenceField(User)
    title = db.StringField(required=True)
    deskripsi = db.StringField(required=True)
    tahun_kegiatan = db.DateField(required=False)
    file = db.StringField(required=True)

class Billing(db.Document):
    user = db.ReferenceField(User)
    nim = db.IntField(required=True)
    nama =  db.StringField(required=True)
    tagihan = db.IntField(required=True)
    date = db.DateField(required=False)

class Dashboard(db.Document):
    user = db.ReferenceField(User)
    nim = db.IntField(required=True)
    nama = db.StringField(required=True)
    IPK = db.StringField(required=True)
    totaltagihan = db.IntField(required=True)
    schedule = db.DateField(required=True)

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
