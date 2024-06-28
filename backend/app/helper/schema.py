from utils import ma
from marshmallow import fields, validate, validates, validates_schema, ValidationError, post_load, pre_load, post_dump
from marshmallow.validate import ContainsOnly
from flask import current_app as app
import config

class UserSchema(ma.Schema):
    id = fields.String(dump_only=True)
    username = fields.String(required=True, validate=validate.Length(max=64))
    password = fields.String(required=True, load_only=True, validate=validate.Length(min=6, max=64))
    userlevel = fields.Integer(default=0)
    description = fields.String()

    @validates_schema
    def validate_username(self, data, **kwargs):
        if not data["username"]:
            raise ValidationError("Username is required")
        if not isinstance(data["username"], str):
            raise ValidationError("Username must be a string")
        
    class Meta:
        ordered = True

class LoginSchema(ma.Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)

class RegisterSchema(ma.Schema):
    username = fields.String(required=True)
    password = fields.String(required=True, validate=validate.Length(min=6, max=64))
    userlevel = fields.Integer(default=0)
    description = fields.String()


class CourseSchema(ma.Schema):
    id = fields.String(dump_only=True)
    kode_mk = fields.String(required=True)
    semester = fields.String(required=True)
    nama_mk = fields.String(required=False)
    sks = fields.Integer(required=False)
    description = fields.String(required=False)
    user = fields.Nested(UserSchema, required=True, dump_only=True)
    

#TODO: add any schema here

class BulletinSchema(ma.Schema):
    id = fields.String(dump_only=True)
    title = fields.String(required=True)
    content = fields.String(required=False)
    author = fields.String(required=True)
    date = fields.Date(required=False)
    user = fields.Nested(UserSchema, required=True, dump_only=True)
    # course = fields.Nested(Course, dump_only=True)

class ClassesSchema(ma.Schema):
    id = fields.String(dump_only=True)
    course = fields.String(required=True)
    type = fields.String(required=True)
    sks = fields.Integer(required=True)
    date = fields.DateTime(required=True)
    room = fields.String(required=False)
    online_class = fields.String(required=False)
    lecture = fields.String(required=True)
    user = fields.Nested(UserSchema, required=True, dump_only=True)