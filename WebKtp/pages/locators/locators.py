from selenium.webdriver.common.by import By


class LoginPageLocator:
    username_locator = (By.NAME, "account")
    pwd_locator = (By.NAME, "pass")
    login_btn_locator = ("xpath", '//a[contains(@class, "btn-btn")]')
    Join_course_btn_locator = ("xpath", '//div[contains(@class, "ktcon1l")]')


