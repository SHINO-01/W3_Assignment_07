from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def get_driver():
    """
    Sets up and returns a Selenium WebDriver instance with appropriate options.
    """
    # Set up Chrome options
    options = Options()
    options.add_argument("--start-maximized")  # Open browser in maximized mode
    options.add_argument("--disable-infobars")  # Disable the infobar message
    options.add_argument("--disable-extensions")  # Disable extensions for simplicity
    options.add_argument("--headless")  # Uncomment if you want headless mode
    options.add_argument("--no-sandbox")  # For Linux environments
    options.add_argument("--disable-dev-shm-usage")  # For Linux environments

    # Initialize WebDriver with Service and Options
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    return driver
