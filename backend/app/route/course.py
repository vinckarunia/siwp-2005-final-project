from flask import Blueprint
from flask_restful import Api
from resource.course import CourseAPI, CourseListAPI, BulletinAPI, BulletinListAPI, BillingAPI, BillingListAPI, DashboardAPI, DashboardListAPI, NewsAPI, NewsListAPI, ExamAPI, ExamListAPI, CampusEventAPI, CampusEventListAPI, InputKRSAPI, InputKRSListAPI, SoftskillAPI, SoftskillListAPI, ClassesAPI, ClassesListAPI, GuidanceAPI, GuidanceListAPI, ProfileAPI, ProfileListAPI

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

inputkrs_blueprint = Blueprint("inputkrs_api", __name__)
inputkrs_blueprint_api = Api(inputkrs_blueprint)

softskill_blueprint = Blueprint("softskill_api", __name__)
softskill_blueprint_api = Api(softskill_blueprint)

billing_blueprint = Blueprint("billing_api", __name__)
billing_blueprint_api = Api(billing_blueprint)

dashboard_blueprint = Blueprint("dashboard_api", __name__)
dashboard_blueprint_api = Api(dashboard_blueprint)

news_blueprint = Blueprint("news_api", __name__)
news_blueprint_api = Api(news_blueprint)

exam_blueprint = Blueprint("exam_api", __name__)
exam_blueprint_api = Api(exam_blueprint)

campusevent_blueprint = Blueprint("campusevent_api", __name__)
campusevent_blueprint_api = Api(campusevent_blueprint)


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
inputkrs_blueprint_api.add_resource(
    InputKRSListAPI, "/inputkrs"
)

inputkrs_blueprint_api.add_resource(
    InputKRSAPI, "/inputkrs/<string:inputkrs_id>"
)

softskill_blueprint_api.add_resource(
    SoftskillListAPI, "/softskill"
)

softskill_blueprint_api.add_resource(
    SoftskillAPI, "/softskill/<string:softskill_id>"
)

billing_blueprint_api.add_resource(
    BillingListAPI, "/billings"
)

billing_blueprint_api.add_resource(
    BillingAPI, "/billings/<string:billing_id>"
)
dashboard_blueprint_api.add_resource(
    DashboardListAPI, "/dashboard"
)

dashboard_blueprint_api.add_resource(
    DashboardAPI, "/dashboard/<string:dashboard_id>"
)

news_blueprint_api.add_resource(
    NewsListAPI, "/news"
)

news_blueprint_api.add_resource(
    NewsAPI, "/news/<string:news_id>"
)

exam_blueprint_api.add_resource(
    ExamListAPI, "/exam"
)

exam_blueprint_api.add_resource(
    ExamAPI, "/exam/<string:exam_id>"
)

campusevent_blueprint_api.add_resource(
    CampusEventListAPI, "/campusevent"
)

campusevent_blueprint_api.add_resource(
    CampusEventAPI, "/campusevent/<string:campusevent_id>"
)
