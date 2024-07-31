from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class SearchResultsPage(Page):

    SEARCH_RESULTS_TXT = (By.XPATH, "//div[@data-test = 'resultsHeading']")
    FIRST_ITEM_ADD_BTN = (By.CSS_SELECTOR, "#addToCartButtonOrTextIdFor79545713")

    def verify_search_results(self, expected_product):
        self.verify_partial_text(expected_product, *self.SEARCH_RESULTS_TXT)

    def verify_product_in_url(self, expected_product):
        self.verify_partial_url(expected_product)
        # url = self.driver.current_url
        # assert expected_product in url, f'Expected {expected_product} not in {url}'

    def select_first_item(self):
        self.click(*self.FIRST_ITEM_ADD_BTN)
        sleep(6)