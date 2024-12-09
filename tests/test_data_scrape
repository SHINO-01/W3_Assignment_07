def scrape_script_data_from_console(driver, url):
    """
    Extracts ScriptData from the browser console on the given page.

    Parameters:
        driver: Selenium WebDriver instance.
        url: The URL of the page to scrape.

    Returns:
        A dictionary with extracted data or default placeholders if ScriptData is not found.
    """
    try:
        driver.get(url)

        # Execute JavaScript to fetch the ScriptData object
        script_data = driver.execute_script(
            "return typeof ScriptData !== 'undefined' ? ScriptData : null;"
        )

        # Check if ScriptData was found
        if script_data:
            return {
                "SiteURL": url,
                "CampaignID": script_data.get("config", {}).get("CampaignID", "N/A"),
                "SiteName": script_data.get("config", {}).get("SiteName", "N/A"),
                "Browser": script_data.get("userInfo", {}).get("Platform", "N/A"),
                "CountryCode": script_data.get("userCurrency", {}).get("Country", "N/A"),
                "IP": script_data.get("userInfo", {}).get("IP", "N/A"),
            }
        else:
            return {
                "SiteURL": url,
                "CampaignID": "N/A",
                "SiteName": "N/A",
                "Browser": "N/A",
                "CountryCode": "N/A",
                "IP": "N/A",
                "Error": "ScriptData not found",
            }

    except Exception as e:
        return {
            "SiteURL": url,
            "CampaignID": "Error",
            "SiteName": "Error",
            "Browser": "Error",
            "CountryCode": "Error",
            "IP": f"Error: {str(e)}",
        }
