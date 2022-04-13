import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class DemoGetText():
    def demo_gettext(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get('https://yatra.com')
        text = driver.find_element(By.LINK_TEXT, 'Yatra for Business').text
        print(text)
        time.sleep(2)


demobrowser = DemoGetText()
demobrowser.demo_gettext()

#new line added sdet1