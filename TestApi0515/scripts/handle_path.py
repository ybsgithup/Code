import os


# one_path = os.path.abspath(__file__)
# two_path = os.path.dirname(one_path)
# BASE_DIR = os.path.dirname(two_path)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CASES_PATH = os.path.join(BASE_DIR, "cases")

CONF_PATH = os.path.join(BASE_DIR, "confs")

CONF_FILE_PATH = os.path.join(CONF_PATH, "testcases.yaml")

DATA_PATH = os.path.join(BASE_DIR, "data")

LOG_PATH = os.path.join(BASE_DIR, "logs")

REPORTS_PATH = os.path.join(BASE_DIR, "reports")

SCRIPTS_PATH = os.path.join(BASE_DIR, "scripts")

pass
