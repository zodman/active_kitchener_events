import enums
from utils import get_headers, is_available
import requests


def get_data():
    answer = []
    for i in range(1, enums.MAX_PAGE):
        entries = fetch_page(i)
        [answer.append(i) for i in entries]
    return filter(is_available, answer)


def fetch_page(page):
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
    return entries
