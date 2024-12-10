import requests

def check_url_status(url):
    """
    Checks if the URL returns a valid status code and fails only for 404 errors.
    """
    try:
        response = requests.get(url)
        if response.status_code == 404:
            return {
                "page_url": url,
                "testcase": "URL Status Code",
                "passed/fail": "Fail",
                "comments": "Status code 404 (Not Found)"
            }
        else:
            return {
                "page_url": url,
                "testcase": "URL Status Code",
                "passed/fail": "Pass",
                "comments": f"Status code {response.status_code}"
            }

    except requests.exceptions.RequestException:
        # Generic exception handling for connection issues or other errors
        return {
            "page_url": url,
            "testcase": "URL Status Code",
            "passed/fail": "Pass",
            "comments": "Connection Error (Non-404)"
        }
