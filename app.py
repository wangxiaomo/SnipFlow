#-*- coding: utf-8 -*-

from werkzeug.wsgi import DispatcherMiddleware
from werkzeug.serving import run_simple
from flask import Flask, render_template
from apps.backend.api import api
from apps.admin import app as admin
from apps.file import app as file


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


application = DispatcherMiddleware(app, {"/j": api, "/admin": admin, "/file": file})
run_simple("0.0.0.0", 5000, application, use_reloader=True, use_debugger=True,
        use_evalex=True)
