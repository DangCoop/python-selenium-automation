from pages.base_page import Page
from pages.main_page import MainPage
from pages.header import Header
from pages.search_results_page import SearchResultsPage
from pages.cart_page import CartPage
from pages.account_side_menu import AccountSideMenu
from pages.sign_in_page import SignInPage
from pages.cart_side_menu import CartSideMenu

class Application:
    def __init__(self, driver):

        self.base_page = Page(driver)

        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.cart_page = CartPage(driver)
        self.account_side_menu = AccountSideMenu(driver)
        self.sign_in_page = SignInPage(driver)
        self.cart_side_menu = CartSideMenu(driver)


