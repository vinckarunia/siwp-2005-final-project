from flask import request, jsonify, abort, Response
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import current_app as app
from marshmallow.exceptions import ValidationError
from mongoengine.errors import NotUniqueError
from werkzeug.exceptions import UnprocessableEntity, Conflict

import helper.validator as validator
from model.course import Course, User, Billing, Dashboard, News, Exam, CampusEvent, InputKRS, Softskill
from helper.schema import CourseSchema, BillingSchema, DashboardSchema, NewsSchema, ExamSchema, CampusEventSchema, InputKRSSchema, SoftskillSchema

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
    
class SoftskillListAPI(Resource):
    @jwt_required()
    def get(self):
        softskill = Softskill.objects()
        serialized_payload = SoftskillSchema(many=True).dump(softskill)
        return serialized_payload, 200
    
    @jwt_required()
    def post(self):
        serialized_payload = validator.add_softskill()
        softskill = Softskill(**serialized_payload)
        softskill.save()
        serialized_payload = SoftskillSchema().dump(softskill)
        return serialized_payload, 200

class SoftskillAPI(Resource):
    @jwt_required()
    def get(self, softskill_id):
        app.logger.info("softskill id: {}".format(softskill_id))
        softskill = Softskill.objects.get(id=softskill_id)
        serialized_payload = SoftskillSchema().dump(softskill)
        return serialized_payload, 200
    
    @jwt_required()
    def put(self, softskill_id):
        softskill = Softskill.objects.get(id=softskill_id)
        user = User.objects.get(id=get_jwt_identity())
        serialized_payload = validator.add_softskill()
        for key, value in serialized_payload.items():
            setattr(softskill, key, value)
        softskill.save()
        serialized_payload = SoftskillSchema().dump(softskill)
        return serialized_payload, 200
    
    @jwt_required()
    def delete(self, softskill_id):        
        softskill = Softskill.objects.get(id=softskill_id)
        softskill.delete()
        app.logger.info("Softskill with id %s deleted", softskill_id)
        msg={"message": "Softskill: {} deleted".format(softskill_id)}
        return msg, 200
    
class BillingListAPI(Resource):
    @jwt_required()
    def get(self):
        billings = Billing.objects()
        serialized_payload = BillingSchema(many=True).dump(billings)
        return serialized_payload, 200
    
    @jwt_required()
    def post(self):
        serialized_payload = validator.add_billing()
        billing = Billing(**serialized_payload)
        billing.save()
        serialized_payload = BillingSchema().dump(billing)
        return serialized_payload, 200

class BillingAPI(Resource):
    @jwt_required()
    def get(self, billing_id):
        app.logger.info("billing id: {}".format(billing_id))
        billing = Billing.objects.get(id=billing_id)
        serialized_payload = BillingSchema().dump(billing)
        return serialized_payload, 200
    
    @jwt_required()
    def put(self, billing_id):
        billing = Billing.objects.get(id=billing_id)
        user = User.objects.get(id=get_jwt_identity())
        serialized_payload = validator.add_billing()
        for key, value in serialized_payload.items():
            setattr(billing, key, value)
        billing.save()
        serialized_payload = BillingSchema().dump(billing)
        return serialized_payload, 200
    
    @jwt_required()
    def delete(self, billing_id):        
        billing = Billing.objects.get(id=billing_id)
        billing.delete()
        app.logger.info("Billing with id %s deleted", billing_id)
        msg={"message": "Billing: {} deleted".format(billing_id)}
        return msg, 200
    
class DashboardListAPI(Resource):
    @jwt_required()
    def get(self):
        dashboard = Dashboard.objects()
        serialized_payload = DashboardSchema(many=True).dump(dashboard)
        return serialized_payload, 200
    
    @jwt_required()
    def post(self):
        serialized_payload = validator.add_dashboard()
        dashboard = Dashboard(**serialized_payload)
        dashboard.save()
        serialized_payload = DashboardSchema().dump(dashboard)
        return serialized_payload, 200

class DashboardAPI(Resource):
    @jwt_required()
    def get(self, dashboard_id):
        dashboard = Dashboard.objects.get(id=dashboard_id)
        serialized_payload = DashboardSchema().dump(dashboard)
        return serialized_payload, 200
    
    @jwt_required()
    def put(self, dashboard_id):
        dashboard = Dashboard.objects.get(id=dashboard_id)
        user = User.objects.get(id=get_jwt_identity())
        serialized_payload = validator.add_dashboard()
        for key, value in serialized_payload.items():
            setattr(dashboard, key, value)
        dashboard.save()
        serialized_payload = DashboardSchema().dump(dashboard)
        return serialized_payload, 200
    
    @jwt_required()
    def delete(self, dashboard_id):        
        dashboard = Dashboard.objects.get(id=dashboard_id)
        dashboard.delete()
        app.logger.info("Dashboard with id %s deleted", dashboard_id)
        msg={"message": "Dashboard: {} deleted".format(dashboard_id)}
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