import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class DemoElementState():
    def demo_enable_disable(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get('https://training.openspan.com/login')
        demo_state = driver.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()
        print(demo_state)


state = DemoElementState()
state.demo_enable_disable()