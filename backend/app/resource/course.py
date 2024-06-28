from flask import request, jsonify, abort, Response
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import current_app as app
from marshmallow.exceptions import ValidationError
from mongoengine.errors import NotUniqueError
from werkzeug.exceptions import UnprocessableEntity, Conflict

import helper.validator as validator
from model.course import Course, User, News, Exam, CampusEvent
from helper.schema import CourseSchema, NewsSchema, ExamSchema, CampusEventSchema

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
    
class NewsListAPI(Resource):
    @jwt_required()
    def get(self):
        news = News.objects()
        serialized_payload = NewsSchema(many=True).dump(news)
        return serialized_payload, 200
    
    @jwt_required()
    def post(self):
        serialized_payload = validator.add_news()
        news = News(**serialized_payload)
        news.save()
        serialized_payload = NewsSchema().dump(news)
        return serialized_payload, 200

class NewsAPI(Resource):
    @jwt_required()
    def get(self, news_id):
        app.logger.info("news id: {}".format(news_id))
        news = News.objects.get(id=news_id)
        serialized_payload = NewsSchema().dump(news)
        return serialized_payload, 200
    
    @jwt_required()
    def put(self, news_id):
        news = News.objects.get(id=news_id)
        user = User.objects.get(id=get_jwt_identity())
        serialized_payload = validator.add_news()
        for key, value in serialized_payload.items():
            setattr(news, key, value)
        news.save()
        serialized_payload = NewsSchema().dump(news)
        return serialized_payload, 200
    
    @jwt_required()
    def delete(self, news_id):        
        news = News.objects.get(id=news_id)
        news.delete()
        app.logger.info("News with id %s deleted", news_id)
        msg={"message": "News: {} deleted".format(news_id)}
        return msg, 200

class ExamListAPI(Resource):
    @jwt_required()
    def get(self):
        exam = Exam.objects()
        serialized_payload = ExamSchema(many=True).dump(exam)
        return serialized_payload, 200
    
    @jwt_required()
    def post(self):
        serialized_payload = validator.add_exam()
        exam = Exam(**serialized_payload)
        exam.save()
        serialized_payload = ExamSchema().dump(exam)
        return serialized_payload, 200

class ExamAPI(Resource):
    @jwt_required()
    def get(self, exam_id):
        app.logger.info("exam id: {}".format(exam_id))
        exam = exam.objects.get(id=exam_id)
        serialized_payload = ExamSchema().dump(exam)
        return serialized_payload, 200
    
    @jwt_required()
    def put(self, exam_id):
        exam = Exam.objects.get(id=exam_id)
        user = User.objects.get(id=get_jwt_identity())
        serialized_payload = validator.add_exam()
        for key, value in serialized_payload.items():
            setattr(exam, key, value)
        exam.save()
        serialized_payload = ExamSchema().dump(exam)
        return serialized_payload, 200
    
    @jwt_required()
    def delete(self, exam_id):        
        exam = Exam.objects.get(id=exam_id)
        exam.delete()
        app.logger.info("Exam with id %s deleted", exam_id)
        msg={"message": "Exam: {} deleted".format(exam_id)}
        return msg, 200

class CampusEventListAPI(Resource):
    @jwt_required()
    def get(self):
        campusevent = CampusEvent.objects()
        serialized_payload = CampusEventSchema(many=True).dump(campusevent)
        return serialized_payload, 200
    
    @jwt_required()
    def post(self):
        serialized_payload = validator.add_campusevent()
        campusevent = CampusEvent(**serialized_payload)
        campusevent.save()
        serialized_payload = CampusEventSchema().dump(campusevent)
        return serialized_payload, 200

class CampusEventAPI(Resource):
    @jwt_required()
    def get(self, campusevent_id):
        app.logger.info("campusevent id: {}".format(campusevent_id))
        campusevent = campusevent.objects.get(id=campusevent_id)
        serialized_payload = CampusEventSchema().dump(campusevent)
        return serialized_payload, 200
    
    @jwt_required()
    def put(self, campusevent_id):
        campusevent = CampusEvent.objects.get(id=campusevent_id)
        user = User.objects.get(id=get_jwt_identity())
        serialized_payload = validator.add_campusevent()
        for key, value in serialized_payload.items():
            setattr(campusevent, key, value)
        campusevent.save()
        serialized_payload = CampusEventSchema().dump(campusevent)
        return serialized_payload, 200
    
    @jwt_required()
    def delete(self, campusevent_id):        
        campusevent = CampusEvent.objects.get(id=campusevent_id)
        campusevent.delete()
        app.logger.info("CampusEvent with id %s deleted", campusevent_id)
        msg={"message": "CampusEvent: {} deleted".format(campusevent_id)}
        return msg, 200


    #TODO:
    # CRUD


        

            