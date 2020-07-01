import os
import pytest

# ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
# REPORT_PATH = os.path.join(ROOT_PATH, "output")
# REPORT_FILE = os.path.join(REPORT_PATH, 'demo_report.html')


if __name__ == '__main__':
    # pytest.main(["-m success", f"--html={REPORT_FILE}", '--alluredir=allreport'])
    pytest.main(["-m success", f"--html=report_new.html"])

