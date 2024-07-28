from selenium.webdriver.common.by import By
from pages.base_page import Page

class SearchResultsPage(Page):

    SEARCH_RESULTS_TXT = (By.XPATH, "//div[@data-test = 'resultsHeading']")
    def verify_text(self):
        actual_text = self.driver.find_element(*self.SEARCH_RESULTS_TXT).text
        assert 'speaker' in actual_text, f'Expected speaker is not in actual text {actual_text}'

    def verify_url(self):
        url = self.driver.current_url
        assert 'speaker' in url, f'Expected speaker not in {url}'
