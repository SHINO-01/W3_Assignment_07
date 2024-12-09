def scrape_script_data_once(driver, base_url):
    """
    Extracts ScriptData from the browser console on the base page.

    Parameters:
        driver: Selenium WebDriver instance.
        base_url: The base URL of the site to scrape.

    Returns:
        A dictionary with extracted data or default placeholders if ScriptData is not found.
    """
    try:
        driver.get(base_url)

        # Execute JavaScript to fetch the ScriptData object
        script_data = driver.execute_script(
            "return typeof ScriptData !== 'undefined' ? ScriptData : null;"
        )

        # Check if ScriptData was found
        if script_data:
            return {
                "SiteURL": script_data.get("config", {}).get("SiteUrl", "N/A"),
                "CampaignID": script_data.get("pageData", {}).get("CampaignId", "N/A"),
                "SiteName": script_data.get("config", {}).get("SiteName", "N/A"),
                "Browser": script_data.get("userInfo", {}).get("Browser", "N/A"),
                "CountryCode": script_data.get("userInfo", {}).get("CountryCode", "N/A"),
                "IP": script_data.get("userInfo", {}).get("IP", "N/A"),
            }
        else:
            return {
                "SiteURL": base_url,
                "CampaignID": "N/A",
                "SiteName": "N/A",
                "Browser": "N/A",
                "CountryCode": "N/A",
                "IP": "N/A",
                "Error": "ScriptData not found",
            }

    except Exception as e:
        return {
            "SiteURL": base_url,
            "CampaignID": "Error",
            "SiteName": "Error",
            "Browser": "Error",
            "CountryCode": "Error",
            "IP": f"Error: {str(e)}",
        }