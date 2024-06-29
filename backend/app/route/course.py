from flask import Blueprint
from flask_restful import Api
from resource.course import CourseAPI, CourseListAPI, BillingAPI, BillingListAPI, DashboardAPI, DashboardListAPI, NewsAPI, NewsListAPI, ExamAPI, ExamListAPI, CampusEventAPI, CampusEventListAPI

course_blueprint = Blueprint("course_api", __name__)
course_blueprint_api = Api(course_blueprint)

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
