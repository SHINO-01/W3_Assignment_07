from selenium.common.exceptions import NoSuchElementException

def check_h1_tag(driver, url):
    """
    Checks if an H1 tag exists on the given URL.
    """
    try:
        driver.get(url)
        driver.find_element("tag name", "h1")
        return {"page_url": url, "testcase": "H1 Tag Existence", "passed/fail": "Pass", "comments": "H1 tag found"}
    except NoSuchElementException:
        return {"page_url": url, "testcase": "H1 Tag Existence", "passed/fail": "Fail", "comments": "H1 tag not found"}
    except Exception as e:
        return {"page_url": url, "testcase": "H1 Tag Existence", "passed/fail": "Fail", "comments": f"Error: {str(e)}"}
