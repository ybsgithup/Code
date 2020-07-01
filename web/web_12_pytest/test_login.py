import pytest
import sys


@pytest.mark.skipif(sys.platform=="linux", reason="window 系统因为环境不同跳过。")
@pytest.mark.success
def test_login_success():
    pass


def test_login_error():
    pass


def test_login_invalid():
    pass

