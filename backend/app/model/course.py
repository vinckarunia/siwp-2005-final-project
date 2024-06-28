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
    # course = db.ReferenceField(Course)
    
class Softskill(db.Document):
    user = db.ReferenceField(User)
    title = db.StringField(required=True)
    deskripsi = db.StringField(required=True)
    tahun_kegiatan = db.DateField(required=False)
    file = db.StringField(required=True)
    # course = db.ReferenceField(Course)