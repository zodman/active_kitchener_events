from enums import EXTRA_HEADERS
import json
from dateutil.parser import parse
from datetime import timedelta


def get_headers(page):
    headers = EXTRA_HEADERS
    headers.update(page_number=page)
    return {'page_info': json.dumps(headers)}


def is_available(x):
    if x["sub_activity_ids"] == []:
        return False
    return int(x.get("openings", 0)) > 0


def group_by_date(data):
    dates = {}
    for i in data:
        date_range_start = i["date_range_start"]
        data_range_end = i["date_range_end"]
        if data_range_end != '':
            date_start = parse(date_range_start).date()
            date_end = parse(data_range_end).date()
            delta = date_end - date_start
            for day in range(delta.days):
                date_obj = date_start + timedelta(days=day)
                date_str = date_obj.strftime("%Y-%m-%d")
                dates.setdefault(date_str, [])
                dates[date_str].append(i)
        else:
            dates.setdefault(date_range_start, [])
            dates[date_range_start].append(i)
    return dates


def sort_by_time(entry):
    time = entry["time_range"]
    start, _ = time.split(" - ")
    if 'Noon' in start:
        start = '12:00 PM'
    return parse(f"{entry['date_range_start']} {start}")
