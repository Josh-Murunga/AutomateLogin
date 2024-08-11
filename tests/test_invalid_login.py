import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Constants
url = "https://qa.kenyahmis.org/openmrs/spa/login"
driver_path = "./drivers/chromedriver.exe"

# Set up Chrome options
options = Options()
#options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Initialize WebDriver with Service
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service, options=options)

def test_login():
    driver.get(url)

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        )

        # Step 1: Input username and click "Continue"
        username_field = driver.find_element(By.ID, "username")
        continue_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        
        username_field.send_keys("invalid_username")
        continue_button.click()
        print("Username entered and Continue button clicked")
        
        # Step 2: Wait for the password field to be visible, then input the password
        password_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "password"))
        )
        password_field.send_keys("invalid_password")
        print("Password entered")
        
        # Step 3: Click the "Log in" button
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()
        print("Login button clicked")

        # Step 4: Verify Error message is displayed
        try:
            error_message = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Invalid username or password')]"))
            )
            assert error_message.is_displayed(), "Error message did not display"
        except Exception as e:
            pytest.fail(f"Login failed: {str(e)}")
        
    except Exception as e:
        pytest.fail(f"An error occured: {str(e)}")

    # Close the WebDriver session
    driver.quit()
    print("WebDriver session closed.")
