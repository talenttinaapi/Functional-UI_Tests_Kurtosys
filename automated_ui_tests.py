from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Initialize the ChromeDriver 
driver = webdriver.Chrome()

try:
    # Go to kurtosys home page
    driver.get("https://www.kurtosys.com/")
    print("Navigated to Kurtosys website")
    driver.save_screenshot("step1_homepage.png")

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler"))
    )

    # Dismiss the consent overlay
    try:
        dismiss_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
        )
        dismiss_button.click()
        print("Dismissed consent overlay")
        driver.save_screenshot("step2_dismiss_consent.png")
    except TimeoutException:
        print("Consent overlay not found or already dismissed")

    # Navigating to White Papers & eBooks
    try:
        white_papers_ebooks_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "White Papers & eBooks"))
        )
        white_papers_ebooks_link.click()
        print("Clicked on White Papers & eBooks")
        driver.save_screenshot("step3_white_papers_ebooks.png")


        try:
            ucits_whitepaper_link = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "UCITS Whitepaper"))
            )
            ucits_whitepaper_link.click()
            print("Clicked on UCITS Whitepaper")
            driver.save_screenshot("step4_ucits_whitepaper.png")
            
            # page to load after clicking 'UCITS Whitepaper'
            WebDriverWait(driver, 20).until(
                EC.url_contains("/white-papers/eu-rule-change-bolsters-need-for-fast-localized-fund-website-platforms-2/")
            )
            print("Successfully loaded UCITS Whitepaper page")
            driver.save_screenshot("step5_ucits_whitepaper_loaded.png")

        except TimeoutException:
            print("Timed out waiting for 'UCITS Whitepaper' link to be clickable")

    except TimeoutException:
        print("Timed out waiting for 'White Papers & eBooks' link to be clickable")

    # Verify Page URL
    expected_url = "https://www.kurtosys.com/white-papers-ebooks"
    try:
        WebDriverWait(driver, 10).until(
            EC.url_to_be(expected_url)
        )
        assert driver.current_url == expected_url, f"Expected URL '{expected_url}', but got '{driver.current_url}'"
        print("Successfully verified URL for White Papers & eBooks page")
        driver.save_screenshot("step_verified_url.png")
    except TimeoutException:
        print(f"Timed out waiting for URL to be '{expected_url}', current URL: '{driver.current_url}'")
        driver.save_screenshot("timed_out_waiting_for_verified_url.png")

finally:
    driver.quit()
    print("Closed the WebDriver")
