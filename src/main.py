from flask import Flask,  redirect, render_template, request, send_file

from exporter import *
from scraper import get_jobs

app = Flask('Job Search in Flask')

db = {}


@app.route('/')
def home():
    """
    Render the homepage
    :return: str
    """
    return render_template('home.html')


@app.route('/result')
def result():
    """
    Show the search's result page
    :return: Response or str
    """
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
                           searching=word,
                           result_num=len(jobs),
                           jobs=jobs)


@app.route('/export')
def export():
    """
    Allow exporting result into a CSV file
    :return: Response
    """
    try:
        word = request.args.get('word')
        if word:
            word = word.lower()
            jobs = db.get(word)
        else:
            raise Exception()
        if jobs:
            save_to_file(jobs)
            return send_file('Python-Jobs.csv')
        raise Exception()
    except AttributeError:
        return redirect('/')


app.run(host='0.0.0.0')
