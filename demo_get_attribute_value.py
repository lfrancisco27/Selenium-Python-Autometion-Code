import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class DemoGetAttributeValue():
    def demo_gettext(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get('https://yatra.com')
        attr_value = driver.find_element(By.XPATH,"//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']").get_attribute('value')
        print(attr_value)
        time.sleep(2)


attropr = DemoGetAttributeValue()
attropr.demo_gettext()