#-*- coding: utf-8 -*-

from flask import Blueprint, request

from utils import jsonize
from lib.flask_sqlalchemy import SQLAlchemy

api = Blueprint('api', __name__)
db = SQLAlchemy()

class Snip(db.Model):
    __tablename__ = 'snips'
    id = db.Column('snip_id', db.Integer, primary_key=True)
    context = db.Column('snip_context', db.Text)

    def __init__(self, context):
        self.context = context


@api.route('/snips', methods=['GET'])
@jsonize
def show_snips():
    count = request.args.get('count')
    count = count and int(count) or 20
    snips = Snip.query.limit(count).all()
    all_snips = []
    for snip in snips:
        all_snips.append({
            'snip_id': snip.id,
            'snip_context': snip.context,
        })
    return all_snips

@api.route('/snips', methods=['POST'])
@jsonize
def create_snip():
    snip_context = request.form('snip_context')
    snip = Snip(snip_context)
    db.session.add(snip)
    db.session.commit()
    return {'snip_id':snip.id, 'snip_context':snip.context}

@api.route('/snips/<int:snip_id>', methods=['PUT', 'DELETE'])
@jsonize
def update_snip(snip_id):
    snip = Snip.query.get(snip_id)

    if request.method == 'PUT':
        snip_context = request.form('snip_context')
        snip.snip_context = snip_context
        db.session.commit()
        return {'snip_id':snip.id, 'snip_context':snip.context}
    else:
        db.session.delete(snip)
        db.session.commit()
        return {'snip_id':snip.id}
