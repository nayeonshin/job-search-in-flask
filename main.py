from flask import Flask

app = Flask('Job Search in Flask')


@app.route('/')
def home():
    return 'Hello, welcome to the root!'


@app.route('/contact')
def contact():
    return 'Contact me!'


app.run(host='0.0.0.0')
