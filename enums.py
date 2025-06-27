URL_BASE = 'https://anc.ca.apm.activecommunities.com/activekitchener/rest/activities/'

URL = f'{URL_BASE}list?locale=en-US'


BREAITHAUPT_CENTER = 4  # Breithaupt Centre
MAX_PAGE = 1
EXTRA_HEADERS = {
    "order_by": "Date range",
    "page_number": 1,
    "total_records_per_page": 20
}

SPACES = ' '

PAYLOAD_BASE = {
    "skills": [],
    "time_after_str": "",
    "days_of_week": None,
    "activity_select_param": 0,
    "center_ids": [],
    "time_before_str": "",
    "open_spots": None,
    "activity_id": None,
    "activity_category_ids": [],
    "date_before": "",
    "min_age": None,
    "date_after": "",
    "activity_type_ids": [],
    "site_ids": [],
    "for_map": False,
    "geographic_area_ids": [],
    "season_ids": [],
    "activity_department_ids": [],
    "activity_other_category_ids": [],
    "child_season_ids": [],
    "activity_keyword": "",
    "instructor_ids": [],
    "max_age": None,
    "custom_price_from": "",
    "custom_price_to": ""
}
