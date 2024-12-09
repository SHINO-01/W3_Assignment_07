from selenium.webdriver.common.by import By

def check_image_alt_attributes(driver, url):
    """
    Checks if any image is missing the alt attribute on the given URL.
    """
    try:
        driver.get(url)
        images = driver.find_elements(By.TAG_NAME, "img")
        missing_alt = [img.get_attribute("src") for img in images if not img.get_attribute("alt")]

        if missing_alt:
            return {
                "page_url": url,
                "testcase": "Image Alt Attribute",
                "passed/fail": "Fail",
                "comments": f"Missing alt for images: {', '.join(missing_alt[:5])}..."
            }

        return {
            "page_url": url,
            "testcase": "Image Alt Attribute",
            "passed/fail": "Pass",
            "comments": "All images have alt attributes"
        }

    except Exception as e:
        return {
            "page_url": url,
            "testcase": "Image Alt Attribute",
            "passed/fail": "Fail",
            "comments": f"Error: {str(e)}"
        }
