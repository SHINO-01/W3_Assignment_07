from selenium.webdriver.common.by import By
from urllib.parse import urlparse, urljoin, parse_qs, urlunparse, urlencode

def is_internal_link(base_url, link):
    """
    Checks if a link is internal to the base URL.
    """
    base_netloc = urlparse(base_url).netloc
    link_netloc = urlparse(link).netloc
    return base_netloc == link_netloc

def normalize_url(url):
    """
    Normalizes a URL by removing fragments and sorting query parameters.
    """
    parsed = urlparse(url)
    sorted_query = urlencode(sorted(parse_qs(parsed.query).items()))
    normalized = urlunparse((parsed.scheme, parsed.netloc, parsed.path, parsed.params, sorted_query, ""))
    return normalized

def should_ignore_link(link):
    """
    Determines whether a link should be ignored based on patterns or query parameters.
    """
    ignore_patterns = [
        "redirect",       # Generic redirect links
        "track",          # Tracking links
        "partner",        # Partner referral links
        "referral",       # Referral links
        "feed",           # Feed links
        "epc",            # Tracking query params
        "eplId",          # Partner API identifiers
    ]

    # Check for patterns in the link's path and query parameters
    path = urlparse(link).path
    query_params = parse_qs(urlparse(link).query)

    for pattern in ignore_patterns:
        if pattern in path or pattern in query_params:
            return True

    return False

def extract_links(driver, url, base_url):
    """
    Extracts all unique internal links from the given page URL, filtering out unwanted links.
    Parameters:
        driver: Selenium WebDriver instance.
        url: The URL of the page to extract links from.
        base_url: The base URL of the website (used to validate internal links).
    Returns:
        A tuple of (internal_links, external_links).
    """
    internal_links = set()
    external_links = set()

    try:
        driver.get(url)

        # Scroll to ensure all content is loaded
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Extract links
        elements = driver.find_elements(By.TAG_NAME, "a")
        for element in elements:
            href = element.get_attribute("href")
            if href:
                # Convert relative URLs to absolute URLs
                absolute_url = urljoin(base_url, href)

                # Skip links that should be ignored
                if should_ignore_link(absolute_url):
                    #print(f"Ignored link: {absolute_url}")
                    continue

                if is_internal_link(base_url, absolute_url):
                    internal_links.add(normalize_url(absolute_url))
                else:
                    external_links.add(normalize_url(absolute_url))

    except Exception as e:
        print(f"Error extracting links from {url}: {e}")

    return internal_links, external_links
