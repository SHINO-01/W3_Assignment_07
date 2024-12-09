from selenium.webdriver.common.by import By

def check_html_tag_sequence(driver, url):
    """
    Checks if the H1-H6 tag sequence is correct on the given URL.
    """
    try:
        driver.get(url)
        headers = driver.find_elements(By.XPATH, "//h1 | //h2 | //h3 | //h4 | //h5 | //h6")
        header_tags = [header.tag_name for header in headers]
        expected_sequence = ["h1", "h2", "h3", "h4", "h5", "h6"]

        for i, tag in enumerate(header_tags):
            if tag != expected_sequence[i]:
                return {
                    "page_url": url,
                    "testcase": "HTML Tag Sequence",
                    "passed/fail": "Fail",
                    "comments": f"Tag sequence broken at {tag}"
                }

        return {
            "page_url": url,
            "testcase": "HTML Tag Sequence",
            "passed/fail": "Pass",
            "comments": "Correct sequence"
        }

    except Exception as e:
        return {
            "page_url": url,
            "testcase": "HTML Tag Sequence",
            "passed/fail": "Fail",
            "comments": f"Error: {str(e)}"
        }
