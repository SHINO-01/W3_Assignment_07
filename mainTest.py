import os
import time
import pandas as pd
from config.settings import BASE_URL, OUTPUT_FILE
from utils.browser_setup import get_driver
from utils.link_extractor import extract_links
from utils.excel_formatter import apply_excel_formatting
from tests.test_h1_tags import check_h1_tag
from tests.test_tag_sequence import check_html_tag_sequence
from tests.test_image_alt import check_image_alt_attributes
from tests.test_URL_status import check_url_status
from tests.test_data_scrape import scrape_script_data_once
from tests.test_currency_change import test_currency_filtering

def ensure_directory_exists(file_path):
    """
    Ensures the directory for the given file path exists.
    Creates it if it does not exist.
    """
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory: {directory}")

def main():

    ensure_directory_exists(OUTPUT_FILE)

    # Set up the WebDriver
    driver = get_driver()

    try:
        # Extract links from the base URL
        print("Extracting links...")
        internal_links, external_links = extract_links(driver, BASE_URL, BASE_URL)
        print(f"Internal Links: {len(internal_links)}")
        print(f"External Links: {len(external_links)}")

        # Scrape ScriptData once from the base page
        print("Scraping script data...")
        script_data_result = [scrape_script_data_once(driver, BASE_URL)]

        # Initialize test result containers
        h1_results = []
        html_tag_results = []
        image_alt_results = []
        url_status_results = []

        # Test internal links for H1, HTML tag sequence, image alt attributes, and URL status
        for link in internal_links:
            print(f"Testing internal link: {link}")

            # Run the H1 tag existence test
            h1_result = check_h1_tag(driver, link)
            h1_results.append(h1_result)

            # Run the HTML tag sequence test
            html_tag_result = check_html_tag_sequence(driver, link)
            html_tag_results.append(html_tag_result)

            # Run the image alt attribute test
            image_alt_result = check_image_alt_attributes(driver, link)
            image_alt_results.append(image_alt_result)

            # Test URL status for the same internal link
            url_status_result = check_url_status(link)
            url_status_results.append(url_status_result)

            time.sleep(1)  # Optional delay to avoid overwhelming the server

        # Test external links for URL status only
        for link in external_links:
            print(f"Testing external link URL status: {link}")
            url_status_result = check_url_status(link)
            url_status_results.append(url_status_result)

        # Perform currency filtering test once
        print("Testing currency filtering...")
        currency_results = test_currency_filtering(driver, BASE_URL)

        # Save results to an Excel file
        h1_df = pd.DataFrame(h1_results)
        html_tag_df = pd.DataFrame(html_tag_results)
        image_alt_df = pd.DataFrame(image_alt_results)
        url_status_df = pd.DataFrame(url_status_results)
        script_df = pd.DataFrame(script_data_result)
        currency_df = pd.DataFrame(currency_results)

        excel_file = OUTPUT_FILE.replace(".csv", ".xlsx")

        # Save each test result to a separate sheet
        with pd.ExcelWriter(excel_file, engine="openpyxl") as writer:
            h1_df.to_excel(writer, index=False, sheet_name="H1 Tag Test")
            html_tag_df.to_excel(writer, index=False, sheet_name="HTML Tag Sequence")
            image_alt_df.to_excel(writer, index=False, sheet_name="Image Alt Test")
            url_status_df.to_excel(writer, index=False, sheet_name="URL Status")
            script_df.to_excel(writer, index=False, sheet_name="Script Data")
            currency_df.to_excel(writer, index=False, sheet_name="Currency Filtering")

        print(f"Test completed. Results saved to '{excel_file}'.")

        # Beautify the "H1 Tag Test" sheet
        apply_excel_formatting(excel_file, column_to_format="passed/fail")
        print(f"Formatted Excel file saved to '{excel_file}'.")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
