from utils import db
from model.user import User

class Course(db.Document):
    user = db.ReferenceField(User)
    kode_mk = db.StringField(required=True, unique=True)
    semester = db.StringField(required=True)
    nama_mk = db.StringField(required=False)
    sks = db.IntField(required=False)
    description = db.StringField(required=False)
    
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

    # course = db.ReferenceField(Course)