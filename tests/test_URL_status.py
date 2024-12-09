import requests

def check_url_status(url):
    """
    Checks if the URL returns a status code of 200.
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return {
                "page_url": url,
                "testcase": "URL Status Code",
                "passed/fail": "Pass",
                "comments": "Status code 200"
            }
        else:
            return {
                "page_url": url,
                "testcase": "URL Status Code",
                "passed/fail": "Fail",
                "comments": f"Status code {response.status_code}"
            }

    except Exception as e:
        return {
            "page_url": url,
            "testcase": "URL Status Code",
            "passed/fail": "Fail",
            "comments": f"Error: {str(e)}"
        }
