import utils
import api


def main():
    data_available = api.scrape_data()

    data_grouped = utils.group_by_date(data_available)

    for date_str, data_available in data_grouped:
        entries = sorted(data_available, key=utils.sort_by_time)
        for idx,  entry in enumerate(entries):
            utils.display(idx, entry, date_str)


if __name__ == "__main__":
    main()
