VALID_PROPERTY_TYPES = ["SINGLE_FAMILY", "CONDO", "TOWNHOUSE", "ALL_PROPERTIES"]
VALID_PROPERTY_TYPES_UNIT_SEARCH = ["SINGLE_FAMILY", "CONDO", "TOWNHOUSE", "OTHER"]
VALID_ENTITY_NAMES = [
    "AMH",
    "TRICON",
    "INVITATION_HOMES",
    "HOME_PARTNERS_OF_AMERICA",
    "PROGRESS_RESIDENTIAL",
    "FIRSTKEY_HOMES",
    "AMHERST",
    "VINEBROOK_HOMES",
    "MAYMONT_HOMES",
    "SFR3",
]
VALID_PORTFOLIO_SIZES = [
    "PORTFOLIO_2_TO_9",
    "PORTFOLIO_10_TO_99",
    "PORTFOLIO_100_TO_999",
    "PORTFOLIO_1000_PLUS",
    "ALL_PORTFOLIOS",
]

ID_COLUMNS = ["parcl_id", "parcl_property_id"]
DATE_COLUMNS = ["date", "event_date"]

DELETE_FROM_OUTPUT = ["total", "limit", "offset", "links", "account"]

DEFAULT_LIMIT = 12
MAX_POST_LIMIT = 1000
DEFAULT_LIMIT_SMALL = 1000
DEFAULT_LIMIT_LARGE = 10000

VALID_LOCATION_TYPES = [
    "COUNTY",
    "CITY",
    "ZIP5",
    "CDP",
    "VILLAGE",
    "TOWN",
    "CBSA",
    "ALL",
]

VALID_US_REGIONS = [
    "EAST_NORTH_CENTRAL",
    "EAST_SOUTH_CENTRAL",
    "MIDDLE_ATLANTIC",
    "MOUNTAIN",
    "NEW_ENGLAND",
    "PACIFIC",
    "SOUTH_ATLANTIC",
    "WEST_NORTH_CENTRAL",
    "WEST_SOUTH_CENTRAL",
    "ALL",
]

VALID_US_STATE_ABBREV = [
    "AK",
    "AL",
    "AR",
    "AZ",
    "CA",
    "CO",
    "CT",
    "DC",
    "DE",
    "FL",
    "GA",
    "HI",
    "IA",
    "ID",
    "IL",
    "IN",
    "KS",
    "KY",
    "LA",
    "MA",
    "MD",
    "ME",
    "MI",
    "MN",
    "MO",
    "MS",
    "MT",
    "NC",
    "ND",
    "NE",
    "NH",
    "NJ",
    "NM",
    "NV",
    "NY",
    "OH",
    "OK",
    "OR",
    "PA",
    "PR",
    "RI",
    "SC",
    "SD",
    "TN",
    "TX",
    "UT",
    "VA",
    "VI",
    "VT",
    "WA",
    "WI",
    "WV",
    "WY",
    "ALL",
]

VALID_US_STATE_FIPS_CODES = [
    "01",
    "02",
    "04",
    "05",
    "06",
    "08",
    "09",
    "10",
    "11",
    "12",
    "13",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
    "23",
    "24",
    "25",
    "26",
    "27",
    "28",
    "29",
    "30",
    "31",
    "32",
    "33",
    "34",
    "35",
    "36",
    "37",
    "38",
    "39",
    "40",
    "41",
    "42",
    "44",
    "45",
    "46",
    "47",
    "48",
    "49",
    "50",
    "51",
    "53",
    "54",
    "55",
    "56",
    "60",
    "66",
    "69",
    "72",
    "78",
    "ALL",
]

VALID_SORT_BY = [
    "TOTAL_POPULATION",
    "MEDIAN_INCOME",
    "CASE_SHILLER_20_MARKET",
    "CASE_SHILLER_10_MARKET",
    "PRICEFEED_MARKET",
    "PARCL_EXCHANGE_MARKET",
]

VALID_SORT_ORDER = ["ASC", "DESC"]

VALID_EVENT_TYPES = ["SALE", "LISTING", "RENTAL", "ALL"]

PARCL_LABS_DASHBOARD_URL = "https://dashboard.parcllabs.com/signup"

NO_API_KEY_ERROR = f"API Key is required. Please visit {PARCL_LABS_DASHBOARD_URL} to get an API key."
