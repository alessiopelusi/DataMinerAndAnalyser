from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def seleniumDriver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver