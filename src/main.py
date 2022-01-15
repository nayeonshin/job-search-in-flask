from flask import Flask, redirect, render_template, request, send_file

from exception import *
from exporter import *
from scraper import get_jobs

app = Flask("Job Search in Flask")

db = {}


@app.route("/")
def home() -> str:
    """Render the homepage"""
    return render_template("home.html")


@app.route("/result")
def result():
    """Show the search's result page
    :return: Response or str
    """
    word = request.args.get("word")
    if word:
        word = word.lower()
        existing_jobs = db.get(word)
        if existing_jobs:
            jobs = existing_jobs
        else:
            jobs = get_jobs(word)
            db[word] = jobs
    else:
        return redirect("/")
    return render_template(
        "result.html",
        searching=word.capitalize(),
        result_num=len(jobs),
        jobs=jobs,
        can_export=True if len(jobs) > 0 else False,
    )


@app.route("/export")
def export():
    """Allow exporting result into a CSV file
    :return: Response
    """
    try:
        word = request.args.get("word")
        if word:
            word = word.lower()
            jobs = db.get(word)
        else:
            raise NoInputError
        if jobs:
            capitalized_word = word.capitalize()
            save_to_file(jobs, capitalized_word)
            return send_file(f"{capitalized_word}-Jobs.csv")
    except NoInputError:
        return redirect("/")


if __name__ == "__main__":
    app.run()
