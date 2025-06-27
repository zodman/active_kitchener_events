import enums
from utils import get_headers, is_available
import requests


def scrape_data():
    answer = []
    for i in range(1, enums.MAX_PAGE+1):
        entries = _fetch_page(i)
        [answer.append(i) for i in entries]
    return answer  # filter(is_available, answer)


def _fetch_page(page):
    payload = enums.PAYLOAD_BASE
    payload.update(
        center_ids=[str(enums.BREAITHAUPT_CENTER)]
    )
    headers = get_headers(page)
    json_data = {
        'activity_search_pattern': payload,
        'activity_transfer_pattern': {},
    }
    resp = requests.post(enums.URL,
                         json=json_data, headers=headers)
    resp.raise_for_status()
    data = resp.json()

    entries = data["body"]["activity_items"]
    results = []

    for i in entries:
        subs = i['sub_activity_ids']
        if subs:
            results.extend(_fetch_sub_activities(i["id"]))

    return entries + results


def _fetch_sub_activities(id):
    url = f"{enums.URL_BASE}subs/{id}?locale=en-US"
    resp = requests.post(url.format(id), json={
        "sub_activity_ids": "",
        "activity_transfer_pattern": {},
        "open_spots": 1
    })
    resp.raise_for_status()
    data = resp.json()

    return [i for i in data['body']["sub_activities"]]
