import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class DemoFindElementByIdAndName():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get('https://secure.yatra.com/social/common/yatra/signin.htm')
        driver.find_element(By.XPATH, "//input[@id='login-input']").send_keys('test@test.com')
        time.sleep(4)
findbyid = DemoFindElementByIdAndName()
findbyid.locate_by_id_demo()
