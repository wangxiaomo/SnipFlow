#-*- coding: utf-8 -*-

from apps.model import db


class Snip(db.Model):
    __tablename__ = 'snips'
    id = db.Column('snip_id', db.Integer, primary_key=True)
    context = db.Column('snip_context', db.Text)

    def __init__(self, context):
        self.context = context
