import requests
import json

from enums import URL, PAYLOAD_BASE


def main():
    payload = PAYLOAD_BASE
    payload.update(
        center_ids=["4"]
    )
    resp = requests.post(URL, json=payload)
    print(json.dumps(resp.json()))


if __name__ == "__main__":
    main()
