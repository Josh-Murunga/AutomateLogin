# AutomateLogin

This is an automated test login script for running on the OpenMRS platform. The script contains two tests. One is the test_login script that tests the ability to access the login page, input the credentials and on successfull login, be able to see the home page. The second script is the test_invalid_login that tests whether we are able to see the invalid login error message on credentails failure.

The choice of technology stack is python and selenium. The assumptions made are of the familiarity of the language and framework library respectively.

## Setting up

1. **Python Installation**
    Download Python from the official website and follow the installation prompts suitable for your operating system. Verify installation by running

    ```bash
     python --version
     ```

2. **pip Installation**
    Pip usually comes bundled with Python. Verify installation by running

    ```bash
     pip --version
     ```

3. **Install Selenium and Other Dependancies**
    Selenium and the test reports dependancies are indicated in the requirements.txt file. Any other dependancy can also be included and then run the script as follows

    ```bash
     pip install -r requirements.txt
     ```

4. **Download WebDriver**
    Depending on your preferred browser, download the corresponding WebDriver. For this example, we make use of Chrome:

    * Download ChromeDriver: https://googlechromelabs.github.io/chrome-for-testing/#stable
    * Ensure Compatibility: The ChromeDriver version should match your installed Chrome browser version.
    * Place the Driver in the directory named drivers in your project root and place the downloaded chromedriver executable there.


## Running Tests

**Run Test With Report**

    ```bash
     pytest --html=reports/report.html --self-contained-html
    ```


