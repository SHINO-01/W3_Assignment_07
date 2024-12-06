from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def get_driver():
    """
    Sets up and returns a Selenium WebDriver instance.
    """
    return webdriver.Chrome(ChromeDriverManager().install())
