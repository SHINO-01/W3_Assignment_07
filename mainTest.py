import time
import pandas as pd
from config.settings import BASE_URL, OUTPUT_FILE
from utils.browser_setup import get_driver
from utils.link_extractor import extract_links
from tests.test_h1_tags import check_h1_tag
from tests.test_tag_sequence import check_html_tag_sequence
from tests.test_image_alt import check_image_alt_attributes
from tests.test_URL_status import check_url_status
from utils.excel_formatter import apply_excel_formatting

def main():
    # Set up the WebDriver
    driver = get_driver()

    try:
        # Extract links from the base URL
        print("Extracting links...")
        internal_links, external_links = extract_links(driver, BASE_URL, BASE_URL)
        print(f"Internal Links: {len(internal_links)}")
        print(f"External Links: {len(external_links)}")

        # Initialize test results
        results = []

        # Test internal links for H1, HTML tag sequence, and image alt attributes
        for link in internal_links:
            print(f"Testing internal link: {link}")

            # Run the H1 tag existence test
            h1_result = check_h1_tag(driver, link)
            results.append(h1_result)

            # Run the HTML tag sequence test
            html_tag_result = check_html_tag_sequence(driver, link)
            results.append(html_tag_result)

            # Run the image alt attribute test
            image_alt_result = check_image_alt_attributes(driver, link)
            results.append(image_alt_result)

            time.sleep(1)  # Optional delay to avoid overwhelming the server

        # Test all links (internal and external) for URL status code
        all_links = internal_links.union(external_links)
        for link in all_links:
            print(f"Testing URL status: {link}")
            url_status_result = check_url_status(link)
            results.append(url_status_result)

        # Save results to an Excel file
        df = pd.DataFrame(results)
        excel_file = OUTPUT_FILE.replace(".csv", ".xlsx")
        df.to_excel(excel_file, index=False)
        print(f"Test completed. Results saved to '{excel_file}'.")

        # Beautify the Excel file
        apply_excel_formatting(excel_file, column_to_format="passed/fail")
        print(f"Formatted Excel file saved to '{excel_file}'.")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
