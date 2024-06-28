from flask import abort, request, make_response, jsonify
import helper.schema  as schema
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist
from marshmallow.exceptions import ValidationError
from genson import SchemaBuilder
from jsonschema import validate
from marshmallow import INCLUDE, EXCLUDE

from flask import current_app as app


def add_course() -> dict:
    '''
    Validation for add course
    '''
    try:
        serialized_payload = schema.CourseSchema().load(request.get_json())
        return serialized_payload
    except ValidationError as e:
        abort(400, {'errors': e.messages})
    except FieldDoesNotExist:
        abort(400, {'error': 'Request is missing required fields'})
    except NotUniqueError:
        abort(400, {'error': 'kode_mk already exists, please try another kode_mk'})

def add_inputkrs() -> dict:
    '''
    validation for inputkrs seriliarized
    '''
    try:
        serialized_payload = schema.InputKRSSchema().load(request.get_json())
        return serialized_payload
    except ValidationError as e:
        abort(400, {'errors': e.messages})
    except FieldDoesNotExist:
        abort(400, {'error': 'Request is missing required fields'})
  
def add_softskill() -> dict:
    '''
    validation for softskill seriliarized
    '''
    try:
        serialized_payload = schema.SoftskillSchema().load(request.get_json())
        return serialized_payload
    except ValidationError as e:
        abort(400, {'errors': e.messages})
    except FieldDoesNotExist:
        abort(400, {'error': 'Request is missing required fields'})
       
def add_billing() -> dict:
    '''
    validation for billing seriliarized
    '''
    try:
        serialized_payload = schema.BillingSchema().load(request.get_json())
        return serialized_payload
    except ValidationError as e:
        abort(400, {'errors': e.messages})
    except FieldDoesNotExist:
        abort(400, {'error': 'Request is missing required fields'})

def add_dashboard() -> dict:
    '''
    Validation for dashboard serialized
    '''
    try:
        serialized_payload = schema.DashboardSchema().load(request.get_json())
    except ValidationError as e:
        abort(400, {'errors': e.messages})
    except FieldDoesNotExist:
        abort(400, {'error': 'Request is missing required fields'})

def add_news() -> dict:
    '''
    validation for news seriliarized
    '''
    try:
        serialized_payload = schema.NewsSchema().load(request.get_json())
        return serialized_payload
    except ValidationError as e:
        abort(400, {'errors': e.messages})
    except FieldDoesNotExist:
        abort(400, {'error': 'Request is missing required fields'})

def add_exam() -> dict:
    '''
    validation for exam seriliarized
    '''
    try:
        serialized_payload = schema.ExamSchema().load(request.get_json())
        return serialized_payload
    except ValidationError as e:
        abort(400, {'errors': e.messages})
    except FieldDoesNotExist:
        abort(400, {'error': 'Request is missing required fields'})

def add_campusevent() -> dict:
    '''
    validation for campusevent seriliarized
    '''
    try:
        serialized_payload = schema.CampusEventSchema().load(request.get_json())
        return serialized_payload
    except ValidationError as e:
        abort(400, {'errors': e.messages})
    except FieldDoesNotExist:
        abort(400, {'error': 'Request is missing required fields'})
  
