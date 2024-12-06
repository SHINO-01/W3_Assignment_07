import time
import pandas as pd
from config.settings import BASE_URL, OUTPUT_FILE
from utils.browser_setup import get_driver
from utils.link_extractor import extract_links
from tests.test_h1_tags import check_h1_tag

def main():
    # Set up the WebDriver
    driver = get_driver()

    try:
        # Extract all links from the base URL
        print("Extracting links...")
        child_links = extract_links(driver, BASE_URL)
        print(f"Found {len(child_links)} links.")

        # Run the H1 tag test on each link
        print("Running H1 tag tests...")
        results = []
        for link in child_links:
            print(f"Testing: {link}")
            result = check_h1_tag(driver, link)
            results.append(result)
            time.sleep(1)  # Optional delay to avoid overwhelming the server

        # Save results to CSV
        df = pd.DataFrame(results)
        df.to_csv(OUTPUT_FILE, index=False)
        print(f"Test completed. Results saved to '{OUTPUT_FILE}'.")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
