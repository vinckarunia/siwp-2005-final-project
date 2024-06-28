from flask import Blueprint
from flask_restful import Api
from resource.course import CourseAPI, CourseListAPI, BillingAPI, BillingListAPI, DashboardAPI, DashboardListAPI


course_blueprint = Blueprint("course_api", __name__)
course_blueprint_api = Api(course_blueprint)

billing_blueprint = Blueprint("billing_api", __name__)
billing_blueprint_api = Api(billing_blueprint)

dashboard_blueprint = Blueprint("dashboard_api", __name__)
dashboard_blueprint_api = Api(dashboard_blueprint)

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
