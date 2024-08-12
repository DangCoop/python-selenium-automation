from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import Page
from time import sleep


class SearchResultsPage(Page):

    SEARCH_RESULTS_TXT = (By.XPATH, "//div[@data-test = 'resultsHeading']")
    FIRST_ITEM_ADD_BTN = (By.CSS_SELECTOR, "#addToCartButtonOrTextIdFor79545713")
    FAVORITES_BTN = (By.CSS_SELECTOR, "[data-test='FavoritesButton']")
    FAVORITES_TOOLTIP_TXT = (By.XPATH, "//*[text()='Click to sign in and save']")

    def hover_fav_icon(self):
        self.wait_for_element_appear(*self.FAVORITES_BTN) # Will replace sleep (2)
        self.hover_element(*self.FAVORITES_BTN)
        # fav_icon = self.find_element(*self.FAVORITES_BTN)
        # actions = ActionChains(self.driver)
        # actions.move_to_element(fav_icon)
        # actions.perform()
        # sleep(2)

    def verify_fav_tooltip(self):
        self.wait_for_element_appear(*self.FAVORITES_TOOLTIP_TXT)

    def verify_search_results(self, expected_product):
        self.verify_partial_text(expected_product, *self.SEARCH_RESULTS_TXT)

    def verify_product_in_url(self, expected_product):
        self.verify_partial_url(expected_product)
        # url = self.driver.current_url
        # assert expected_product in url, f'Expected {expected_product} not in {url}'

    def select_first_item(self):
        self.click(*self.FIRST_ITEM_ADD_BTN)
        sleep(6)