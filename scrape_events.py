import requests
import enums
from utils import get_headers, is_available
from rich import print


def get_data():
    answer = []
    for i in range(1, enums.MAX_PAGE):
        payload = enums.PAYLOAD_BASE
        payload.update(
            center_ids=[enums.BREAITHAUPT_CENTER]
        )
        headers = get_headers(i)
        resp = requests.post(enums.URL, json=payload, headers=headers)
        resp.raise_for_status()
        data = resp.json()
        entries = data["body"]["activity_items"]
        [answer.append(i) for i in entries]
    return filter(is_available, answer)


def main():
    data_available = get_data()

    for i in data_available:

        if i["ages"] == 'Any':
            i.update(ages="")

        str_format = ("[blue]{name} [white]{openings}/{total_open} "
                      "[green]{ages} [cyan]{time_range}")
        print(str_format.format(**i))


if __name__ == "__main__":
    main()
