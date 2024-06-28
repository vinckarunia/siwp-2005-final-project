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
       
def add_bulletin() -> dict:
    '''
    validation for bulletin seriliarized
    '''
    try:
        serialized_payload = schema.BulletinSchema().load(request.get_json())
        return serialized_payload
    except ValidationError as e:
        abort(400, {'errors': e.messages})
    except FieldDoesNotExist:
        abort(400, {'error': 'Request is missing required fields'})
  
def add_classes() -> dict:
    '''
    validation for classes seriliarized
    '''
    try:
        serialized_payload = schema.ClassesSchema().load(request.get_json())
        return serialized_payload
    except ValidationError as e:
        abort(400, {'errors': e.messages})
    except FieldDoesNotExist:
        abort(400, {'error': 'Request is missing required fields'})