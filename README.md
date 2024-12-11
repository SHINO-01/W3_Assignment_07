<body>
    <h1>Automated website Testing using Selenium</h1>
    <h2 id="introduction">1. Introduction</h2>
    <p>This project is a comprehensive test automation suite built using Selenium and Python. The suite tests various aspects of a web application, including H1 tag existence, HTML tag sequence validation, image alt attribute checks, URL status codes, and currency filtering. It also scrapes data dynamically and outputs detailed results in an Excel file for analysis.</p>
    <h2 id="contents">2. Contents</h2>
    <ul>
        <li><a href="#introduction">Introduction</a></li>
        <li><a href="#contents">Contents</a></li>
        <li><a href="#folder-structure">Project Folder Structure</a></li>
        <li><a href="#setup">Downloading and Setting up the Project</a></li>
        <li><a href="#how-to-run">How to Run</a></li>
        <li><a href="#sample-output">Sample Output</a></li>
        <li><a href="#documentation">Technical Documentation of All Functions</a></li>
        <li><a href="#known-issues">Known Issues</a></li>
        <li><a href="#summary">Summary</a></li>
    </ul>
    <h2 id="folder-structure">3. Project Folder Structure</h2>
    <pre>
    W3_Assignment_07
    ├── config
    │   └── settings.py
    ├── reports
    │   └── test_results.csv
    ├── tests
    │   ├── test_h1_tags.py
    │   ├── test_tag_sequence.py
    │   ├── test_image_alt.py
    │   ├── test_URL_status.py
    │   ├── test_data_scrape.py
    │   └── test_currency_change.py
    ├── utils
    │   ├── browser_setup.py
    │   ├── link_extractor.py
    │   └── excel_formatter.py
    ├── mainTest.py
    └── README.html
    </pre>
    <h2 id="setup">4. Downloading and Setting up the Project</h2>
    <ol>
        <li>Clone the repository:</li>
        <pre>git clone https://github.com/SHINO-01/W3_Assignment_07.git</pre>
        <li>Navigate to the project directory:</li>
        <pre>cd W3_Assignment_07</pre>
        <li>Create a virtual environment:</li>
        <pre>python -m venv .venv</pre>
        <li>Activate the virtual environment:</li>
        <pre>
            # Windows
            .venv\Scripts\activate
            # macOS/Linux
            source .venv/bin/activate
        </pre>
        <li>Install dependencies:</li>
        <pre>pip3 install -r requirements.txt</pre> or use pip for windows
    </ol>
    <h2 id="how-to-run">5. How to Run</h2>
    <ol>
        <li>Ensure the virtual environment is activated.</li>
        <li>Run the main test file:</li>
        <pre>python3 mainTest.py</pre> or use python for windows
        <li>The test results will be saved in the <code>reports</code> directory as an Excel file.</li>
        <li>If you want to change the target URL for testing, you can find the variable <code>BASE_URL</code> in the config/settings.py</li>
    </ol>
    <h2 id="sample-output">6. Sample Output</h2>
    <p>The test suite generates an Excel file with the following sheets:</p>
    <ul>
        <li><strong>H1 Tag Test:</strong> Validates the existence of H1 tags on all internal links.</li>
        <li><strong>HTML Tag Sequence:</strong> Checks the sequence of HTML tags (H1-H6).</li>
        <li><strong>Image Alt Test:</strong> Ensures all images have alt attributes and provides clickable links for missing ones.</li>
        <li><strong>URL Status:</strong> Validates the status codes for all internal and external links.</li>
        <li><strong>Script Data:</strong> Scrapes and records key metadata from the website.</li>
        <li><strong>Currency Filtering:</strong> Tests currency dropdown functionality and validates price updates.</li>
    </ul>
    <h2 id="documentation">7. All Functions</h2>
    <ul>
        <li><strong>check_h1_tag(driver, url):</strong> Checks for the existence of H1 tags on the specified URL.</li>
        <li><strong>check_html_tag_sequence(driver, url):</strong> Validates the correct sequence of HTML heading tags (H1-H6).</li>
        <li><strong>check_image_alt_attributes(driver, url):</strong> Ensures all images on the page have alt attributes. Reports missing ones with clickable links.</li>
        <li><strong>check_url_status(url):</strong> Verifies the status code of the given URL. Passes for all codes except 404.</li>
        <li><strong>scrape_script_data_once(driver, url):</strong> Extracts metadata like SiteURL, CampaignID, SiteName, Browser, CountryCode, and IP.</li>
        <li><strong>test_currency_filtering(driver, url):</strong> Tests the functionality of the currency dropdown and validates price changes.</li>
        <li><strong>extract_links(driver, base_url, main_domain):</strong> Extracts internal and external links from the given base URL.</li>
        <li><strong>apply_excel_formatting(file_path, column_to_format):</strong> Beautifies the Excel file by formatting specific columns.</li>
        <li><strong>get_driver():</strong> Configures and returns a Selenium WebDriver instance.</li>
    </ul>
    <h2 id="known-issues">8. Known Issues</h2>
    <ul>
        <li>Hyperlinks in Excel may render as plain text in certain viewers.</li>
        <li>Long-running tests may be affected by website changes during execution.</li>
        <li>Needs to have a account logged into facebook otherwise returns Connection error.</li>
    </ul>
    <h2 id="summary">9. Summary</h2>
    <p>This project provides a robust, modular and scalable framework for testing web applications using Selenium. It ensures a comprehensive analysis of web page elements, link statuses, and dynamic content. The structured output makes it easy for stakeholders to identify and address potential issues effectively.</p>
</body>
