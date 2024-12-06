from selenium.webdriver.common.by import By

def extract_links(driver, url):
    """
    Extracts all unique links from the given page URL.
    """
    driver.get(url)
    links = set()
    try:
        elements = driver.find_elements(By.TAG_NAME, "a")
        for element in elements:
            href = element.get_attribute("href")
            if href and href.startswith("http"):
                links.add(href)
    except Exception as e:
        print(f"Error extracting links from {url}: {e}")
    return links
