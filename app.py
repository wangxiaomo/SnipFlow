#-*- coding: utf-8 -*-

from flask import Flask, request, flash, jsonify
from lib.flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('settings.py')
db = SQLAlchemy(app)

class Snip(db.Model):
    __tablename__ = 'snips'
    id = db.Column('snip_id', db.Integer, primary_key=True)
    context = db.Column('snip_context', db.Text)

    def __init__(self, context):
        self.context = context


@app.route('/')
def index():
    return "Hello World"

@app.route('/snips')
def show_snips():
    count = request.args.get('count')
    count = count and int(count) or 20
    snips = Snip.query.limit(count).all()
    if not snips:
        flash('没有数据', 'warning')
    all_snips = []
    for snip in snips:
        all_snips.append({
            'snip_id': snip.id,
            'snip_context': snip.context,
        })
    return jsonify(data=all_snips)

@app.route('/snip', methods=['POST'])
def create_snip():
    snip_context = request.form('snip_context')
    snip = Snip(snip_context)
    db.session.add(snip)
    db.session.commit()
    return jsonify(snip_id=snip.id, snip_context=snip.context)

@app.route('/snip/<int:snip_id>', methods=['PUT', 'DELETE'])
def update_snip(snip_id):
    snip = Snip.query.get(snip_id)

    if request.method == 'PUT':
        """ 修改 snip """
        snip_context = request.form('snip_context')
        snip.snip_context = snip_context
        db.session.commit()
        return jsonify(snip_id=snip.id, snip_context=snip.context)
    else:
        """ 删除 snip """
        db.session.delete(snip)
        db.session.commit()
        return jsonify(snip_id=snip.id)


if __name__ == '__main__':
    app.run(debug=True)
