from flask import Flask, render_template, request, redirect
from scraper import get_jobs

app = Flask('Job Search in Flask')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/result')
def result():
    word = request.args.get('word')
    if word:
        word = word.lower()
        jobs = get_jobs(word)
        print(jobs)
    else:
        return redirect('/')
    return render_template('result.html', searching=word)


app.run(host='0.0.0.0')
