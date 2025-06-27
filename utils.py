from enums import EXTRA_HEADERS, SPACES
import json
from dateutil.parser import parse
from datetime import timedelta

from rich import print


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
    items = dates.items()
    return sorted(items, key=lambda x: parse(x[0]).date())


def sort_by_time(entry):
    time = entry["time_range"]
    time = time.replace('Noon',  '12:00 PM')
    start, _ = time.split(" - ")
    return parse(f"{entry['date_range_start']} {start}")


def display(idx, entry, date_str):

    if 'Ages:' not in entry['ages']:
        if entry["ages"] == 'Any':
            entry.update(ages="")
        else:
            ages_str = "[green]Ages: {} ".format(entry["ages"].strip())
            entry.update(ages=ages_str)

    entry['time_range'] = entry['time_range'].replace('Noon', '12:00 PM')

    prefix = SPACES*11
    if idx == 0:
        prefix = '[yellow]{: <10} '.format(date_str)

    str_format = [
        "[cyan]{time_range: >18} ",
        "[bright_blue]{name} ",
        "[white]{openings}/{total_open} ",
        " {ages}"]
    print(prefix + "".join(str_format).format(**entry))
