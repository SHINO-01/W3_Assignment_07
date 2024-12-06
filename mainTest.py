import time
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
def setup_driver():
    """Initialize and return the WebDriver."""
    driver = webdriver.Chrome()  # Use webdriver.Firefox() for Firefox
    driver.maximize_window()
    return driver

# H1 Tag Existence Test
def test_h1_existence(driver):
    """Check if an H1 tag exists on the page."""
    try:
        h1_tag = driver.find_element(By.TAG_NAME, "h1")
        return "Pass", "H1 tag found"
    except:
        return "Fail", "H1 tag missing"

# HTML Tag Sequence Test
def test_html_sequence(driver):
    """Validate the sequence of H1-H6 tags."""
    headers = driver.find_elements(By.XPATH, "//h1 | //h2 | //h3 | //h4 | //h5 | //h6")
    sequence = [int(tag.tag_name[1]) for tag in headers]
    if sequence == sorted(sequence):
        return "Pass", "HTML tag sequence correct"
    return "Fail", "HTML tag sequence broken"

# Image Alt Attribute Test
def test_image_alt(driver):
    """Check if all images have alt attributes."""
    images = driver.find_elements(By.TAG_NAME, "img")
    missing_alt = [img.get_attribute('src') for img in images if not img.get_attribute('alt')]
    if missing_alt:
        return "Fail", f"Images missing alt attributes: {missing_alt}"
    return "Pass", "All images have alt attributes"

# URL Status Code Test
def test_url_status(driver):
    """Check if all URLs are valid (not 404)."""
    links = driver.find_elements(By.TAG_NAME, "a")
    broken_urls = []
    for link in links:
        href = link.get_attribute('href')
        if href and href.startswith('http'):
            try:
                response = requests.head(href)
                if response.status_code == 404:
                    broken_urls.append(href)
            except requests.RequestException:
                broken_urls.append(href)
    if broken_urls:
        return "Fail", f"Broken URLs found: {broken_urls}"
    return "Pass", "All URLs are valid"

# Currency Filter Functionality Test
def test_currency_filter(driver):
    """Test if currency filter updates property tiles."""
    try:
        # Locate and click on the currency dropdown
        currency_dropdown = driver.find_element(By.ID, "currency-dropdown")  # Replace with actual ID
        currency_dropdown.click()
        time.sleep(1)
        # Select USD from the dropdown
        usd_option = driver.find_element(By.XPATH, "//option[@value='USD']")  # Replace with actual value
        usd_option.click()
        time.sleep(3)  # Wait for the page to update prices
        # Verify that property prices are displayed in USD
        prices = driver.find_elements(By.CLASS_NAME, "property-price")  # Replace with actual class
        if all("$" in price.text for price in prices):
            return "Pass", "Currency updated to USD"
        else:
            return "Fail", "Currency did not update to USD"
    except Exception as e:
        return "Fail", f"Error in currency filter: {e}"

# Scrape Data from Script Tags
def scrape_script_data(driver):
    """Scrape data from script tags."""
    script_data = driver.find_elements(By.TAG_NAME, "script")
    results = []
    for script in script_data:
        content = script.get_attribute("innerHTML")
        if "SiteURL" in content:  # Look for specific keys
            results.append(content)
    if results:
        return "Pass", results
    else:
        return "Fail", "No relevant script data found"

# Save Results to CSV
def save_results_to_csv(results):
    """Save test results to a CSV file."""
    df = pd.DataFrame(results, columns=["Page URL", "Test Case", "Result", "Comments"])
    df.to_csv("test_results.csv", index=False)

# Main Execution
if __name__ == "__main__":
    driver = setup_driver()
    url = "https://www.alojamiento.io/"
    driver.get(url)
    time.sleep(3)  # Allow the page to load

    test_cases = [
        ("H1 Tag Existence Test", test_h1_existence(driver)),
        ("HTML Tag Sequence Test", test_html_sequence(driver)),
        ("Image Alt Attribute Test", test_image_alt(driver)),
        ("URL Status Code Test", test_url_status(driver)),
        ("Currency Filter Functionality Test", test_currency_filter(driver)),
        ("Scrape Data from Script Tags", scrape_script_data(driver))
    ]

    results = [[url, test[0], test[1][0], test[1][1]] for test in test_cases]
    save_results_to_csv(results)
    driver.quit()
