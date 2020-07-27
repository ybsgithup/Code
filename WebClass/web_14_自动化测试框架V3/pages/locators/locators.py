from selenium.webdriver.common.by import By


class LoginPageLocator:
    mobile_locator = (By.NAME, "phone")
    pwd_locator = (By.NAME, "password")
    login_btn_locator = ("xpath", '//button[contains(@class, "btn-special")]')
    error_msg_locator = ("xpath", '//div[@class="form-error-info"]')
    invalid_msg_locator = ("xpath", '//div[@class="layui-layer-content"]')