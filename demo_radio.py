import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class DemoRadio():
    def demo_radiobutton(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get('https://www.sugarcrm.com/au/request-demo/')
        driver.maximize_window()
        driver.find_element(By.ID, 'doi0').click()
        time.sleep(4)


state = DemoRadio()
state.demo_radiobutton()
