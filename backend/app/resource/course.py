from flask import request, jsonify, abort, Response
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import current_app as app
from marshmallow.exceptions import ValidationError
from mongoengine.errors import NotUniqueError
from werkzeug.exceptions import UnprocessableEntity, Conflict

import helper.validator as validator
from model.course import Course, User, Bulletin, Classes, Guidance, Profile
from helper.schema import CourseSchema, BulletinSchema, ClassesSchema, GuidanceSchema, ProfileSchema

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

# Academic Guidance
class GuidanceListAPI(Resource):
    @jwt_required()
    def get(self):
        guidance = Guidance.objects()
        serialized_payload = GuidanceSchema(many=True).dump(guidance)
        return serialized_payload, 200
    
    @jwt_required()
    def post(self):
        serialized_payload = validator.add_guidance()
        guidance = Guidance(**serialized_payload)
        guidance.save()
        serialized_payload = GuidanceSchema().dump(guidance)
        return serialized_payload, 200

class GuidanceAPI(Resource):
    @jwt_required()
    def get(self, guidance_id):
        app.logger.info("guidance id: {}".format(guidance_id))
        guidance = Guidance.objects.get(id=guidance_id)
        serialized_payload = GuidanceSchema().dump(guidance)
        return serialized_payload, 200
    
    @jwt_required()
    def put(self, guidance_id):
        guidance = Guidance.objects.get(id=guidance_id)
        user = User.objects.get(id=get_jwt_identity())
        serialized_payload = validator.add_guidance()
        for key, value in serialized_payload.items():
            setattr(guidance, key, value)
        guidance.save()
        serialized_payload = GuidanceSchema().dump(guidance)
        return serialized_payload, 200
    
    @jwt_required()
    def delete(self, guidance_id):        
        guidance = Guidance.objects.get(id=guidance_id)
        guidance.delete()
        app.logger.info("Guidance with id %s deleted", guidance_id)
        msg={"message": "Guidance: {} deleted".format(guidance_id)}
        return msg, 200


# Profile
class ProfileListAPI(Resource):
    @jwt_required()
    def get(self):
        profile = Profile.objects()
        serialized_payload = ProfileSchema(many=True).dump(profile)
        return serialized_payload, 200
    
    @jwt_required()
    def post(self):
        serialized_payload = validator.add_profile()
        profile = Profile(**serialized_payload)
        profile.save()
        serialized_payload = ProfileSchema().dump(profile)
        return serialized_payload, 200

class ProfileAPI(Resource):
    @jwt_required()
    def get(self, profile_id):
        app.logger.info("profile id: {}".format(profile_id))
        profile = Profile.objects.get(id=profile_id)
        serialized_payload = ProfileSchema().dump(profile)
        return serialized_payload, 200
    
    @jwt_required()
    def put(self, profile_id):
        profile = Profile.objects.get(id=profile_id)
        user = User.objects.get(id=get_jwt_identity())
        serialized_payload = validator.add_profile()
        for key, value in serialized_payload.items():
            setattr(profile, key, value)
        profile.save()
        serialized_payload = ProfileSchema().dump(profile)
        return serialized_payload, 200
    
    @jwt_required()
    def delete(self, profile_id):        
        profile = Profile.objects.get(id=profile_id)
        profile.delete()
        app.logger.info("Profile with id %s deleted", profile_id)
        msg={"message": "Profile: {} deleted".format(profile_id)}
        return msg, 200