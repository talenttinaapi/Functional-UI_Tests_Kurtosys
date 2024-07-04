from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Initialize the WebDriver
driver = webdriver.Chrome()

try:
    # Go to https://www.kurtosys.com/
    driver.get("https://www.kurtosys.com/")
    print("Navigated to Kurtosys website")

    # Wait for the page to load completely
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler"))
    )

    # Dismiss the consent overlay if present
    try:
        
        dismiss_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
        )
        dismiss_button.click()
        print("Dismissed consent overlay")
    except TimeoutException:
        print("Consent overlay not found or already dismissed")

    # Navigate to “White Papers & eBooks” with retry mechanism
    try:
        white_papers_ebooks_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "White Papers & eBooks"))
        )
        white_papers_ebooks_link.click()
        print("Clicked on White Papers & eBooks")

        # Additional steps after clicking the link can be added here

    except TimeoutException:
        print("Timed out waiting for 'White Papers & eBooks' link to be clickable")

    # Step 4: Verify Page URL
    expected_url = "https://www.kurtosys.com/white-papers-ebooks"
    try:
        WebDriverWait(driver, 10).until(
            EC.url_to_be(expected_url)
        )
        assert driver.current_url == expected_url, f"Expected URL '{expected_url}', but got '{driver.current_url}'"
        print("Successfully verified URL for White Papers & eBooks page")
    except TimeoutException:
        print(f"Timed out waiting for URL to be '{expected_url}', current URL: '{driver.current_url}'")

finally:
    # Close the WebDriver
    driver.quit()
    print("Closed the WebDriver")

