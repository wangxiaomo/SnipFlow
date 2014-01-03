#-*- coding: utf-8 -*-

from os.path import abspath, dirname, curdir

from flask import Flask
from flask.ext.autoindex import AutoIndex


app = Flask(__name__)
AutoIndex(app, browse_root=abspath(dirname(curdir)))
