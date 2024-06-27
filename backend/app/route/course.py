from flask import Blueprint
from flask_restful import Api
from resource.course import CourseAPI, CourseListAPI, BulletinAPI, BulletinListAPI, ClassesAPI, ClassesListAPI


course_blueprint = Blueprint("course_api", __name__)
course_blueprint_api = Api(course_blueprint)

course_blueprint_api.add_resource(
    CourseAPI, "/courses/<string:course_id>"
)
course_blueprint_api.add_resource(
    CourseListAPI, "/courses"
)

course_blueprint_api.add_resource(
    BulletinListAPI, "/bulletins"
)

course_blueprint_api.add_resource(
    BulletinAPI, "/bulletins/<string:bulletin_id>"
)

course_blueprint_api.add_resource(
    ClassesListAPI, "/classes"
)

course_blueprint_api.add_resource(
    ClassesAPI, "/classes/<string:classes_id>"
)

