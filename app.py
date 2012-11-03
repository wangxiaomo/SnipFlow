#-*- coding: utf-8 -*-

from flask import Flask, render_template
from backend.api import api, db

app = Flask(__name__)
app.config.from_pyfile('settings.py')
app.register_blueprint(api, url_prefix='/j')
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
