from flask import Blueprint
from flask_restful import Api
from resource.course import CourseAPI, CourseListAPI, BulletinAPI, BulletinListAPI, ClassesAPI, ClassesListAPI, GuidanceAPI, GuidanceListAPI, ProfileAPI, ProfileListAPI


course_blueprint = Blueprint("course_api", __name__)
course_blueprint_api = Api(course_blueprint)

bulletin_blueprint = Blueprint("bulletin_api", __name__)
bulletin_blueprint_api = Api(bulletin_blueprint)

classes_blueprint = Blueprint("classes_api", __name__)
classes_blueprint_api = Api(classes_blueprint)

guidance_blueprint = Blueprint("guidance_api", __name__)
guidance_blueprint_api = Api(guidance_blueprint)

profile_blueprint = Blueprint("profile_api", __name__)
profile_blueprint_api = Api(profile_blueprint)

course_blueprint_api.add_resource(
    CourseAPI, "/courses/<string:course_id>"
)
course_blueprint_api.add_resource(
    CourseListAPI, "/courses"
)

bulletin_blueprint_api.add_resource(
    BulletinListAPI, "/bulletins"
)

bulletin_blueprint_api.add_resource(
    BulletinAPI, "/bulletins/<string:bulletin_id>"
)

classes_blueprint_api.add_resource(
    ClassesListAPI, "/classes"
)

classes_blueprint_api.add_resource(
    ClassesAPI, "/classes/<string:classes_id>"
)

guidance_blueprint_api.add_resource(
    GuidanceListAPI, "/guidance"
)

guidance_blueprint_api.add_resource(
    GuidanceAPI, "/guidance/<string:guidance_id>"
)

profile_blueprint_api.add_resource(
    ProfileListAPI, "/profile"
)

guidance_blueprint_api.add_resource(
    ProfileAPI, "/profile/<string:profile_id>"
)