import csv


def save_to_file(jobs, word):
    """
    Write list jobs into csv
    :param jobs: list[dict[str, str]]
    :param word: str
    :return: None
    """
    file = open(f"{word}-Jobs.csv", mode="w", encoding="utf-8", newline="")
    writer = csv.writer(file)
    writer.writerow(["Title", "Company", "Location", "Link"])
    for job in jobs:
        writer.writerow(list(job.values()))
