#-*- coding: utf-8 -*-

from flask import Flask
from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqla import ModelView

from apps.model import db
from apps.model.snip import Snip
from apps.settings import AppsSetupConfig


app = Flask(__name__)
app.config.from_object(AppsSetupConfig)
db.init_app(app)

snip_view = ModelView(Snip, db.session, url="/")
admin = Admin(app)
admin.add_view(snip_view)
