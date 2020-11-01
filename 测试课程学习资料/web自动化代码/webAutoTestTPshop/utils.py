from selenium import webdriver
import logging

# 获取弹出框的提示内容
def get_tips_msg():
    msg = DriverUtil.get_driver().find_element_by_class_name("layui-layer-content").text
    print("msg=", msg)
    # 关闭
    return msg


# 判断页面中是否包含指定的文字
def exist_text(text):
    logging.info("param text={}".format(text))
    try:
        xpath = "//*[contains(text(), '{}')]".format(text)
        element = DriverUtil.get_driver().find_element_by_xpath(xpath)
        return element is not None
    except Exception as e:
        logging.error("current page is not contains [{}]".format(text))
        logging.exception(e)
        return False


# 驱动工具类
class DriverUtil:
    _driver = None

    _auto_quit = True

    # 获取驱动
    @classmethod
    def get_driver(cls):
        if cls._driver is None:
            cls._driver = webdriver.Chrome()
            cls._driver.maximize_window()
            cls._driver.implicitly_wait(30)
            cls._driver.get("http://localhost")
        return cls._driver

    # 退出驱动
    @classmethod
    def quit_driver(cls):
        if cls._auto_quit:
            if cls._driver:
                cls._driver.quit()
                cls._driver = None

    # 设置是否自动退出驱动
    @classmethod
    def set_auto_quit(cls, auto_quit):
        cls._auto_quit = auto_quit
