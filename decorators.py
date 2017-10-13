from flask import make_response
from functools import wraps

import json
import traceback

response_header = {"Content-Type": "application/json charset=utf-8"}

def api_wrapper(f):
    """Decorator used to return a json response from an api endpoint"""
    @wraps(f)
    def wrapper(*args, **kwargs):
        result = {}
        response = 200
        try:
            result = f(*args, **kwargs)
        except:
            traceback.print_exc()
            result = {"success": False, "message": "Something went wrong"}
        result = (json.dumps(result), response, response_header)
        return make_response(result)
    return wrapper
