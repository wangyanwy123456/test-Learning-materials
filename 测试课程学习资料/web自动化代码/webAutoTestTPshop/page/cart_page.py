from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class CartPage(BasePage):
    def __init__(self):
        super().__init__()

        self.check_all = (By.CLASS_NAME, "checkCartAll")
        self.go_balance = (By.LINK_TEXT, "去结算")

    def find_check_all(self):
        return self.find_element(self.check_all)

    def find_go_balance(self):
        return self.find_element(self.go_balance)

class CartHandle(BaseHandle):
    def __init__(self):
        self.cart_page = CartPage()

    # 全部选中
    def check_all_goods(self):
        if not self.cart_page.find_check_all().is_selected():
            self.cart_page.find_check_all().click()

    def click_go_balance(self):
        self.cart_page.find_go_balance().click()

class CartProxy:
    def __init__(self):
        self.cart_handle = CartHandle()

    # 去结算
    def go_balance(self):
        self.cart_handle.check_all_goods()
        self.cart_handle.click_go_balance()
