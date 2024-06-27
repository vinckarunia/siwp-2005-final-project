from flask import request, jsonify, abort, Response
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import current_app as app
from marshmallow.exceptions import ValidationError
from mongoengine.errors import NotUniqueError
from werkzeug.exceptions import UnprocessableEntity, Conflict

import helper.validator as validator
from model.course import Course, User, Bulletin, Classes
from helper.schema import CourseSchema, BulletinSchema, ClassesSchema

# Course
class CourseListAPI(Resource):
    @jwt_required()
    def get(self):
        courses = Course.objects()
        serialized_payload = CourseSchema(many=True).dump(courses)
        return serialized_payload, 200
    
    @jwt_required()
    def post(self):
        serialized_payload = validator.add_course()
        course = Course(**serialized_payload)
        course.save()
        serialized_payload = CourseSchema().dump(course)
        return serialized_payload, 200

class CourseAPI(Resource):
    @jwt_required()
    def get(self, course_id):
        course = Course.objects.get(id=course_id)
        serialized_payload = CourseSchema().dump(course)
        return serialized_payload, 200
    
    @jwt_required()
    def put(self, course_id):
        course = Course.objects.get(id=course_id)
        user = User.objects.get(id=get_jwt_identity())
        serialized_payload = validator.add_course()
        for key, value in serialized_payload.items():
            setattr(course, key, value)
        course.save()
        serialized_payload = CourseSchema().dump(course)
        return serialized_payload, 200
    
    @jwt_required()
    def delete(self, course_id):        
        course = Course.objects.get(id=course_id)
        course.delete()
        app.logger.info("Course with id %s deleted", course_id)
        msg={"message": "Course: {} deleted".format(course_id)}
        return msg, 200

# Bulletin 
class BulletinListAPI(Resource):
    @jwt_required()
    def get(self):
        bulletins = Bulletin.objects()
        serialized_payload = BulletinSchema(many=True).dump(bulletins)
        return serialized_payload, 200
    
    @jwt_required()
    def post(self):
        serialized_payload = validator.add_bulletin()
        bulletin = Bulletin(**serialized_payload)
        bulletin.save()
        serialized_payload = BulletinSchema().dump(bulletin)
        return serialized_payload, 200

class BulletinAPI(Resource):
    @jwt_required()
    def get(self, bulletin_id):
        app.logger.info("bulletin id: {}".format(bulletin_id))
        bulletin = Bulletin.objects.get(id=bulletin_id)
        serialized_payload = BulletinSchema().dump(bulletin)
        return serialized_payload, 200
    
    @jwt_required()
    def put(self, bulletin_id):
        bulletin = Bulletin.objects.get(id=bulletin_id)
        user = User.objects.get(id=get_jwt_identity())
        serialized_payload = validator.add_bulletin()
        for key, value in serialized_payload.items():
            setattr(bulletin, key, value)
        bulletin.save()
        serialized_payload = BulletinSchema().dump(bulletin)
        return serialized_payload, 200
    
    @jwt_required()
    def delete(self, bulletin_id):        
        bulletin = Bulletin.objects.get(id=bulletin_id)
        bulletin.delete()
        app.logger.info("Bulletin with id %s deleted", bulletin_id)
        msg={"message": "Bulletin: {} deleted".format(bulletin_id)}
        return msg, 200

# Class Schedule
class ClassesListAPI(Resource):
    @jwt_required()
    def get(self):
        classes = Classes.objects()
        serialized_payload = ClassesSchema(many=True).dump(classes)
        return serialized_payload, 200
    
    @jwt_required()
    def post(self):
        serialized_payload = validator.add_classes()
        classes = Classes(**serialized_payload)
        classes.save()
        serialized_payload = ClassesSchema().dump(classes)
        return serialized_payload, 200

class ClassesAPI(Resource):
    @jwt_required()
    def get(self, classes_id):
        app.logger.info("classes id: {}".format(classes_id))
        classes = Classes.objects.get(id=classes_id)
        serialized_payload = ClassesSchema().dump(classes)
        return serialized_payload, 200
    
    @jwt_required()
    def put(self, classes_id):
        classes = Classes.objects.get(id=classes_id)
        user = User.objects.get(id=get_jwt_identity())
        serialized_payload = validator.add_classes()
        for key, value in serialized_payload.items():
            setattr(classes, key, value)
        classes.save()
        serialized_payload = ClassesSchema().dump(classes)
        return serialized_payload, 200
    
    @jwt_required()
    def delete(self, classes_id):        
        classes = Classes.objects.get(id=classes_id)
        classes.delete()
        app.logger.info("Classes with id %s deleted", classes_id)
        msg={"message": "Classes: {} deleted".format(classes_id)}
        return msg, 200


        

            