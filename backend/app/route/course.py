from flask import Blueprint
from flask_restful import Api
from resource.course import CourseAPI, CourseListAPI, InputKRSAPI, InputKRSListAPI, SoftskillAPI, SoftskillListAPI


course_blueprint = Blueprint("course_api", __name__)
course_blueprint_api = Api(course_blueprint)

course_blueprint_api.add_resource(
    CourseAPI, "/courses/<string:course_id>"
)
course_blueprint_api.add_resource(
    CourseListAPI, "/courses"
)

course_blueprint_api.add_resource(
    InputKRSListAPI, "/inputkrs"
)

course_blueprint_api.add_resource(
    InputKRSAPI, "/inputkrs/<string:inputkrs_id>"
)

course_blueprint_api.add_resource(
    SoftskillListAPI, "/softskill"
)

course_blueprint_api.add_resource(
    SoftskillAPI, "/softskill/<string:softskill_id>"
)