from flask import request, jsonify, abort, Response
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import current_app as app
from marshmallow.exceptions import ValidationError
from mongoengine.errors import NotUniqueError
from werkzeug.exceptions import UnprocessableEntity, Conflict

import helper.validator as validator
from model.course import Course, User, InputKRS
from helper.schema import CourseSchema, InputKRSSchema

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
    
class InputKRSListAPI(Resource):
    @jwt_required()
    def get(self):
        inputkrs = InputKRS.objects()
        serialized_payload = InputKRSSchema(many=True).dump(inputkrs)
        return serialized_payload, 200
    
    @jwt_required()
    def post(self):
        serialized_payload = validator.add_inputkrs()
        inputkrs = InputKRS(**serialized_payload)
        inputkrs.save()
        serialized_payload = InputKRSSchema().dump(inputkrs)
        return serialized_payload, 200

class InputKRSAPI(Resource):
    @jwt_required()
    def get(self, inputkrs_id):
        app.logger.info("inputkrs id: {}".format(inputkrs_id))
        inputkrs = InputKRS.objects.get(id=inputkrs_id)
        serialized_payload = InputKRSSchema().dump(inputkrs)
        return serialized_payload, 200
    
    @jwt_required()
    def put(self, inputkrs_id):
        inputkrs = InputKRS.objects.get(id=inputkrs_id)
        user = User.objects.get(id=get_jwt_identity())
        serialized_payload = validator.add_inputkrs()
        for key, value in serialized_payload.items():
            setattr(inputkrs, key, value)
        inputkrs.save()
        serialized_payload = InputKRSSchema().dump(inputkrs)
        return serialized_payload, 200
    
    @jwt_required()
    def delete(self, inputkrs_id):        
        inputkrs = InputKRS.objects.get(id=inputkrs_id)
        inputkrs.delete()
        app.logger.info("InputKRS with id %s deleted", inputkrs_id)
        msg={"message": "InputKRS: {} deleted".format(inputkrs_id)}
        return msg, 200
    #TODO:
    # CRUD


        

            