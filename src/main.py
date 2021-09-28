from flask import Flask, render_template

app = Flask('Job Search in Flask')


@app.route('/')
def home():
    return render_template('home.html')


app.run(host='0.0.0.0')
