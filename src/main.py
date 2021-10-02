from flask import Flask, render_template, request, redirect
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
        from_db = db.get(word)
        if from_db:
            jobs = from_db
        else:
            jobs = get_jobs(word)
            db[word] = jobs
    else:
        return redirect('/')
    return render_template('result.html',
                           searching=word,
                           result_num=len(jobs)
                           )


app.run(host='0.0.0.0')
