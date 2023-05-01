from selenium.webdriver.common.by import By


class Login:
    txt_login_name = "userName"
    txt_login_name_pwd = "password"
    btn_login_name = "submit"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, userName, txt_login_name=txt_login_name):
        self.driver.find_element(By.NAME, txt_login_name).clear()
        self.driver.find_element(By.NAME, txt_login_name).send_keys(userName)

    def setPassword(self, pwd, txt_login_name_pwd=txt_login_name_pwd):
        self.driver.find_element(By.NAME, txt_login_name_pwd).clear()
        self.driver.find_element(By.NAME, txt_login_name_pwd).send_keys(pwd)

    def submitLogin(self, btn_login_name=btn_login_name):
        self.driver.find_element(By.NAME, btn_login_name).click()
