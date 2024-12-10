from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import re

def clean_price(price_text):
    """
    Cleans the price string by removing dynamic prefixes (e.g., 'De', 'From').
    Retains currency symbols and numeric values.
    """
    prefixes = ["De ", "From "]
    for prefix in prefixes:
        if price_text.startswith(prefix):
            price_text = price_text[len(prefix):]
    return re.sub(r"[^\d\w\s.,€$£¥₹৳د.إ]", "", price_text).strip()


def test_currency_filtering(driver, url):
    """
    Modular test to validate currency filtering on the webpage.
    Returns test results as a list of dictionaries for compatibility with mainTest.py.
    """
    results = []
    try:
        print(f"Opening URL: {url}")
        driver.get(url)

        # Locate the currency dropdown
        print("Locating the currency dropdown...")
        dropdown = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "js-currency-sort-footer"))
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", dropdown)
        print("Dropdown located.")

        # Expand the dropdown
        print("Expanding the dropdown...")
        driver.execute_script("arguments[0].click();", dropdown)
        time.sleep(2)

        # Locate dropdown options
        print("Locating dropdown options...")
        options_container = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "select-ul"))
        )
        currency_options = options_container.find_elements(By.TAG_NAME, "li")

        if not currency_options:
            raise Exception("No currency options found in the dropdown.")

        print(f"Found {len(currency_options)} currency options.")

        # Fetch initial property prices
        print("Fetching initial prices...")
        initial_prices_elements = driver.find_elements(By.CLASS_NAME, "js-price-value")
        initial_prices = [
            {"text": clean_price(price.text.strip()), "data-usd-price": price.get_attribute("data-usd-price")}
            for price in initial_prices_elements
        ]
        print(f"Initial prices fetched: {initial_prices}")

        # Test each currency option
        for index, option in enumerate(currency_options, start=1):
            try:
                # Extract currency details
                currency_text = option.find_element(By.CSS_SELECTOR, "div.option p").get_attribute("innerText").strip()
                currency_country = option.get_attribute("data-currency-country") or "Unknown"
                print(f"Testing currency option {index}/{len(currency_options)}: {currency_text} ({currency_country})")

                # Select the currency option
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", option)
                driver.execute_script("arguments[0].click();", option)
                time.sleep(7)

                # Fetch updated prices
                updated_prices_elements = WebDriverWait(driver, 10).until(
                    lambda d: d.find_elements(By.CLASS_NAME, "js-price-value")
                )
                updated_prices = [
                    {"text": clean_price(price.text.strip()), "data-usd-price": price.get_attribute("data-usd-price")}
                    for price in updated_prices_elements
                ]
                print(f"Updated prices for {currency_text}: {updated_prices}")

                # Compare initial and updated prices
                status = "Passed" if [p["text"] for p in updated_prices] != [p["text"] for p in initial_prices] else "Failed"
                results.append({
                    "Currency": currency_text,
                    "CountryCode": currency_country,
                    "Status": status,
                    "Comment": "Prices updated successfully" if status == "Passed" else "Prices did not change",
                    "Initial Prices": [p["text"] for p in initial_prices],
                    "Updated Prices": [p["text"] for p in updated_prices],
                })

                # Re-fetch initial prices for consistency
                initial_prices = updated_prices

                # Reopen the dropdown
                driver.execute_script("arguments[0].click();", dropdown)
                time.sleep(2)

            except Exception as e:
                print(f"Error testing currency option {index}: {e}")
                results.append({
                    "Currency": "N/A",
                    "CountryCode": "N/A",
                    "Status": "Error",
                    "Comment": f"Test failed with error: {e}",
                    "Initial Prices": [p["text"] for p in initial_prices] if initial_prices else "N/A",
                    "Updated Prices": "N/A",
                })
                driver.execute_script("arguments[0].click();", dropdown)
                time.sleep(2)

    except Exception as e:
        print(f"Test failed with error: {e}")
        results.append({
            "Currency": "N/A",
            "CountryCode": "N/A",
            "Status": "Error",
            "Comment": f"Test failed with error: {e}",
            "Initial Prices": "N/A",
            "Updated Prices": "N/A",
        })

    return results
