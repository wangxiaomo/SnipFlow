#-*- coding: utf-8 -*-

from functools import wraps
from flask import json
from flask import request, Response

def jsonize(func):
    @wraps(func)
    def _(*args, **kw):
        resp = Response(json.dumps(func(*args, **kw)), status=200, mimetype='application/json')
        return resp
    return _
