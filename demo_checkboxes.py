import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class DemoCheckBox():
    def demo_checkboxes(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get('https://www.sugarcrm.com/au/request-demo/')
        driver.maximize_window()
        driver.find_element(By.ID, 'interest_market_c0').click()
        time.sleep(4)
        var1 = driver.find_element(By.ID, 'interest_market_c0').is_selected()
        print(var1)
        var2 =  driver.find_element(By.ID, 'interest_sell_c0').is_selected()
        print(var2)
        time.sleep(2)


state = DemoCheckBox()
state.demo_checkboxes()
