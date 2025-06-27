import enums
from utils import get_headers, is_available, group_by_date, sort_by_time
from rich import print
import api


def main():
    data_available = api.get_data()

    data_grouped = group_by_date(data_available)

    for date_str, data_available in data_grouped.items():
        for idx,  i in enumerate(sorted(data_available, key=sort_by_time)):
            if i["ages"] == 'Any':
                i.update(ages="")
            else:
                ages_str = "[green]Ages: {} ".format(i["ages"])
                i.update(ages=ages_str)

            prefix = '[yellow]{}  '.format(
                date_str) if idx == 0 else enums.SPACES
            str_format = (
                "[cyan]{time_range} "
                "[bright_blue]{name} "
                "[white]{openings}/{total_open} "
                " ")
            print(prefix + str_format.format(**i))


if __name__ == "__main__":
    main()
