from flask import Flask,  redirect, render_template, request, send_file

from exceptions import *
from exporter import *
from scraper import get_jobs

app = Flask('Job Search in Flask')

db = {}


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/result')
def result():
    word = request.args.get('word')
    if word:
        word = word.lower()
        existing_jobs = db.get(word)
        if existing_jobs:
            jobs = existing_jobs
        else:
            jobs = get_jobs(word)
            db[word] = jobs
    else:
        return redirect('/')
    return render_template('result.html',
                           searching=word.capitalize(),
                           result_num=len(jobs),
                           jobs=jobs,
                           can_export=True if len(jobs) > 0 else False
                           )


@app.route('/export')
def export():
    try:
        word = request.args.get('word')
        if word:
            word = word.lower()
            jobs = db.get(word)
        else:
            raise NoInputError
        if jobs:
            capitalized_word = word.capitalize()
            save_to_file(jobs, capitalized_word)
            return send_file(f'{capitalized_word}-Jobs.csv')
    except NoInputError:
        return redirect('/')


app.run(host='0.0.0.0')
