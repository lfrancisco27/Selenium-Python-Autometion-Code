from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver = webdriver.Chrome(executable_path=r"D:\usuarios\alumno\descargas\drivers\chromedriver.exe")

driver.get('http://rcvacademy.com')
driver.maximize_window()
print(driver.title)
