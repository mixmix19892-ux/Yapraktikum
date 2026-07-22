from flask import Flask
from flask.json import jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)

# Применять только символы из набора ASCII? Нет!
app.json.ensure_ascii = False


class Story(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    text = db.Column(db.Text, unique=True, nullable=False)

@app.route('/')
def index_view():
    stories = Story.query.all()
    dicts = []

    for item in stories:
        dicts.append({item.id: item.text})

    return jsonify(dicts)


@app.route('/add')
def add_view():
    return 'Это страница для добавления рассказа'


@app.route('/story')
def random_story_view():
    return 'Это страница со случайным рассказом'

if __name__ == '__main__':
    app.run()