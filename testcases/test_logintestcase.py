import time

import pytest

from PageObject.LoginPage import Login
from utilies.readConfigData import ReadConfig
from utilies import customLogger
from utilies import excelUtils


class Test_Login:
    base_url = ReadConfig.getCommonData("commonData", "base_url")
    userName = ReadConfig.getCommonData("commonData", "userName")
    password = ReadConfig.getCommonData("commonData", "password")
    loggor = customLogger.get_logger("LoginPage")
    path = ".\\TestData\\loginData.xlsx"

    @pytest.mark.sanity
    @pytest.mark.smoke
    def test_home_page_validation(self, setup):
        self.loggor.info("==== TC01 verifying home title ========")
        self.driver = setup
        self.driver.get(self.base_url)
        title = self.driver.title
        self.loggor.info("==== getting title ="+title)
        if title == ReadConfig.getCommonData("message", "home_title"):
            self.driver.save_screenshot(".\\Screenshot\\home_title.png")
            self.loggor.info("==== successfuly home title ========")
            assert True
        else:
            self.loggor.info("==== failed home title ========")
            self.driver.save_screenshot(".\\Screenshot\\home_title_failed.png")
            assert False
        self.driver.close()

    @pytest.mark.smoke
    def test_login_page_validation(self, setup):
        self.loggor.info("==== TC02 verifying login title ========")
        self.driver = setup
        self.driver.get(self.base_url)
        self.lp = Login(self.driver)
        time.sleep(2)
        self.loggor.info("==== providing username ========")
        self.lp.setUserName(self.userName)
        self.loggor.info("==== providing password ========")
        self.lp.setPassword(self.password)
        self.lp.submitLogin()
        title = self.driver.title
        self.loggor.info("==== getting login title ="+title)
        if title == ReadConfig.getCommonData("message", "login_title"):
            self.loggor.info("==== success login title ========")
            self.driver.save_screenshot(".\\Screenshot\\login_title.png")
            assert True
        else:
            self.loggor.info("==== failed login title ========")
            self.driver.save_screenshot(".\\Screenshot\\login_title_failed.png")
            assert False
        self.driver.close()

    @pytest.mark.regression
    def test_excelLogin_page_validation(self, setup):

        rows_count = excelUtils.getRowCount(self.path, "Sheet1")
        list_status = []
        for r in range(2, rows_count+1):
            userName = excelUtils.readData(self.path, "Sheet1", r, 1)
            password = excelUtils.readData(self.path, "Sheet1", r, 2)
            result = excelUtils.readData(self.path, "Sheet1", r, 3)
            self.loggor.info("==== TC03 verifying login title ========")
            self.driver = setup
            self.driver.get(self.base_url)
            self.lp = Login(self.driver)
            time.sleep(2)
            self.loggor.info("==== providing username ========")
            self.lp.setUserName(userName)
            self.loggor.info("==== providing password ========")
            self.lp.setPassword(password)
            self.lp.submitLogin()
            title = self.driver.title
            self.loggor.info("==== getting login title ="+title)
            if title == ReadConfig.getCommonData("message", "login_title"):
                if result == "Pass":
                    self.loggor.info("==== success login title ========")
                    self.driver.save_screenshot(".\\Screenshot\\login_title.png")
                    list_status.append("Pass")
                elif result == "Fail":
                    self.loggor.info("==== Fail login title ========")
                    self.driver.save_screenshot(".\\Screenshot\\Failed_title.png")
                    list_status.append("Fail")
            elif title != ReadConfig.getCommonData("message", "login_title"):
                if result == "Pass":
                    self.loggor.info("==== success login title ========")
                    self.driver.save_screenshot(".\\Screenshot\\login_title.png")
                    list_status.append("Fail")
                elif result == "Fail":
                    self.loggor.info("==== Fail login title ========")
                    self.driver.save_screenshot(".\\Screenshot\\Failed_title.png")
                    list_status.append("Pass")

            if "Fail" not in list_status:
                self.loggor.info("Login is success")
                assert True
            else:
                self.loggor.info("Login is Failed")
                assert False
