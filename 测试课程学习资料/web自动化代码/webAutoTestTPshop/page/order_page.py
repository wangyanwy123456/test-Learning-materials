from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class OrderPage(BasePage):
    def __init__(self):
        super().__init__()

        self.submit_order = (By.LINK_TEXT, "提交订单")

    def find_submit_order(self):
        return self.find_element(self.submit_order)

class OrderHandle(BaseHandle):
    def __init__(self):
        self.order_page = OrderPage()

    def click_submit_order(self):
        self.order_page.find_submit_order().click()

class OrderProxy:
    def __init__(self):
        self.order_handle = OrderHandle()

    # 提交订单
    def submit_order(self):
        self.order_handle.click_submit_order()
