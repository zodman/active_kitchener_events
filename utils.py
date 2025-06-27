from enums import EXTRA_HEADERS
import json


def get_headers(page):
    headers = EXTRA_HEADERS
    headers.update(page_number=page)
    return {'page_info': json.dumps(headers)}


def is_available(x):
    return int(x.get("openings", 0)) > 0
