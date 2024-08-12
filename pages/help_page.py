from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import Page
from time import sleep


class HelpPage(Page):

    HEADER_RETURNS = (By.XPATH, "//h1[text()=' Returns']")
    HEADER_PROMOTIONS = (By.XPATH, "//h1[text()=' Current promotions']")
    HEADER = (By.XPATH, "//h1[text()=' {SUBSTRING}']")
    TOPIC_SELECTION = (By.CSS_SELECTOR, "select[id*='ViewHelpTopics']")

    # Dynamic Locators:
    def _get_locator(self, text):
        # OLD (By.XPATH, "//h1[text()=' {SUBSTRING}']")
        # => NEW  if text Current promotions (By.XPATH, "//h1[text()=' Current promotions']")
        # => NEW if text Returns (By.XPATH, "//h1[text()=' Returns']")
        return [self.HEADER[0], self.HEADER[1].replace('{SUBSTRING}', text)]

    def verify_header(self, expected_text):
        locator = self._get_locator(expected_text)
        self.wait_for_element_appear(*locator)

    def open_help_returns(self):
        self.open_url('https://help.target.com/help/subcategoryarticle?childcat=Returns&parentcat=Returns+%26+Exchanges&searchQuery=')

    def select_topic(self, option):
        dd = self.find_element(*self.TOPIC_SELECTION)
        select = Select(dd)
        select.select_by_value(option)

    # Replace it for dynamic function VERIFY_HEADER
    # def verify_returns(self):
    #     self.wait_for_element_appear(*self.HEADER_RETURNS)
    #
    #
    # def verify_promotions(self):
    #     self.wait_for_element_appear(*self.HEADER_PROMOTIONS)


