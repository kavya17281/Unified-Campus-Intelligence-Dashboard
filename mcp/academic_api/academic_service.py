from pathlib import Path
import json
from datetime import datetime, date

TIMETABLE_FILE = Path(__file__).parent / "timetable.json"
EXAM_FILE = Path(__file__).parent / "exam_schedule.json"
OVERRIDE_FILE = Path(__file__).parent / "overrides.json"


# -----------------------------
# DATA LOADING
# -----------------------------

def load_timetable():
    with open(TIMETABLE_FILE, "r") as file:
        return json.load(file)


def load_exams():
    with open(EXAM_FILE, "r") as file:
        return json.load(file)


def load_overrides():
    with open(OVERRIDE_FILE, "r") as file:
        return json.load(file)


# -----------------------------
# HELPERS
# -----------------------------

def parse_time_range(time_range: str):
    start, end = time_range.split("-")
    return start, end


def today_name():
    return date.today().strftime("%A").lower()


def time_sort_key(item):
    start, _ = parse_time_range(item["time"])
    return start


# -----------------------------
# CORE TIMETABLE ENGINE (STRICT MODE)
# -----------------------------

def get_final_day_schedule(day: str):
    timetable = load_timetable()
    overrides = load_overrides()

    day = day.lower()

    base_classes = timetable.get(day, [])

    # STEP 1: apply cancellations
    cancelled = {
        (o["day"], o["time"])
        for o in overrides
        if o["type"] == "cancelled"
    }

    filtered = [
        c for c in base_classes
        if (day, c["time"]) not in cancelled
    ]

    # STEP 2: apply reschedules (remove old + add new)
    rescheduled = [
        o for o in overrides
        if o["type"] == "rescheduled"
    ]

    for r in rescheduled:
        if r["original_day"] == day:
            filtered = [
                c for c in filtered
                if c["time"] != r["original_time"]
            ]

        if r["new_day"] == day:
            filtered.append({
                "time": r["new_time"],
                "subject": r["subject"],
                "type": "Lecture",
                "room": r.get("room", "N/A")
            })

    # STEP 3: add extra classes
    extra = [
        o for o in overrides
        if o["type"] == "extra_class" and o["day"] == day
    ]

    for e in extra:
        filtered.append({
            "time": e["time"],
            "subject": e["subject"],
            "type": "Extra Class",
            "room": e.get("room", "N/A")
        })

    # STEP 4: sort final schedule
    filtered.sort(key=time_sort_key)

    return filtered


# -----------------------------
# DISCOVERY FUNCTIONS
# -----------------------------

def get_todays_classes():
    return get_final_day_schedule(today_name())


def get_tomorrows_classes():
    from datetime import timedelta

    tomorrow = (date.today() + timedelta(days=1)).strftime("%A").lower()
    return get_final_day_schedule(tomorrow)


def get_day_classes(day: str):
    return get_final_day_schedule(day)


def get_subject_schedule(subject: str):
    timetable = load_timetable()
    overrides = load_overrides()
    subject = subject.lower()

    result = []

    for day, classes in timetable.items():
        for c in classes:
            if c["subject"].lower() == subject:
                result.append({
                    "day": day,
                    "time": c["time"],
                    "room": c["room"]
                })

    # add extra/rescheduled appearances
    for o in overrides:
        if o["subject"].lower() == subject:
            if o["type"] == "extra_class":
                result.append({
                    "day": o["day"],
                    "time": o["time"],
                    "room": o.get("room", "N/A"),
                    "type": "Extra"
                })

            if o["type"] == "rescheduled":
                result.append({
                    "day": o["new_day"],
                    "time": o["new_time"],
                    "room": o.get("room", "N/A"),
                    "type": "Rescheduled"
                })

    return result


# -----------------------------
# EXAM FUNCTIONS
# -----------------------------

def get_upcoming_exams():
    exams = load_exams()

    def parse_date(d):
        return datetime.strptime(d["date"], "%d.%m.%Y")

    return sorted(exams, key=parse_date)


def get_next_exam():
    return get_upcoming_exams()[0] if get_upcoming_exams() else None


def get_next_exam_by_subject(subject: str):
    subject = subject.lower()
    exams = get_upcoming_exams()

    for e in exams:
        if e["subject"].lower() == subject:
            return e

    return None


def get_exam_schedule():
    return load_exams()


# -----------------------------
# ANALYTICS
# -----------------------------

def get_academic_stats():
    timetable = load_timetable()
    exams = load_exams()

    total_classes = sum(len(v) for v in timetable.values())

    return {
        "total_weekly_classes": total_classes,
        "total_exam_entries": len(exams),
        "subjects": len(set(
            c["subject"]
            for v in timetable.values()
            for c in v
        ))
    }