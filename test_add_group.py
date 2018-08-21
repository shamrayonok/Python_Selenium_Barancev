# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from group import Group

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)

    def open_home_page(self, driver):
        driver.get("http://localhost/addressbook/")

    def login(self, driver, username, password):
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()

    def open_groups_page(self, driver):
        driver.find_element_by_link_text("GROUPS").click()

    def create_group(self, driver, group):
        driver.find_element_by_name("new").click()
        driver.find_element_by_name("group_name").click()
        driver.find_element_by_name("group_name").clear()
        driver.find_element_by_name("group_name").send_keys(group.name)
        driver.find_element_by_name("group_header").click()
        driver.find_element_by_name("group_header").clear()
        driver.find_element_by_name("group_header").send_keys(group.header)
        driver.find_element_by_name("group_footer").click()
        driver.find_element_by_name("group_footer").clear()
        driver.find_element_by_name("group_footer").send_keys(group.footer)
        driver.find_element_by_name("submit").click()

    def return_to_groups_page(self, driver):
        driver.find_element_by_link_text("group page").click()

    def logout(self, driver):
        driver.find_element_by_link_text("LOGOUT").click()



    def test_add_groupe(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver, username="admin", password="secret")
        self.open_groups_page(driver)
        self.create_group(driver, Group(name="sdfgbdfg", header="fgbdfgbdfg", footer="dfgbdfgbdfg"))
        self.return_to_groups_page(driver)
        self.logout(driver)

    def test_add_empty_groupe(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver, username="admin", password="secret")
        self.open_groups_page(driver)
        self.create_group(driver, Group(name="", header="", footer=""))
        self.return_to_groups_page(driver)
        self.logout(driver)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
