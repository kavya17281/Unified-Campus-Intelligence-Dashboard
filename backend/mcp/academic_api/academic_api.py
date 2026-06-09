from fastapi import FastAPI
from academic_service import *

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Academic MCP Running"}


# -----------------------------
# Timetable
# -----------------------------

@app.get("/today")
def today():
    return get_todays_classes()


@app.get("/tomorrow")
def tomorrow():
    return get_tomorrows_classes()


@app.get("/day")
def day(day: str):
    return get_day_classes(day)


@app.get("/subject")
def subject_schedule(subject: str):
    return get_subject_schedule(subject)


# -----------------------------
# Exams
# -----------------------------

@app.get("/exams")
def exams():
    return get_exam_schedule()


@app.get("/next-exam")
def next_exam():
    return get_next_exam()


@app.get("/next-exam-subject")
def next_exam_subject(subject: str):
    return get_next_exam_by_subject(subject)


# -----------------------------
# Stats
# -----------------------------

@app.get("/stats")
def stats():
    return get_academic_stats()