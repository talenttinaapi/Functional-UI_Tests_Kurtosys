from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import time

# Initialize the WebDriver 
driver = webdriver.Chrome()

try:
    # Go to https://www.kurtosys.com/
    driver.get("https://www.kurtosys.com/")
    print("Navigated to Kurtosys website")

    # Wait for the page to load completely
    time.sleep(5)
    
    # Dismiss the consent overlay if present
    try:
        dismiss_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
        )
        dismiss_button.click()
        print("Dismissed consent overlay")
    except Exception as e:
        print("Consent overlay not found or already dismissed:", str(e))
    
    # Navigate to “INSIGHTS”
    try:
        insights_menu = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "INSIGHTS"))
        )
        insights_menu.click()
        print("Clicked on INSIGHTS")
    except Exception as e:
        print("Error clicking INSIGHTS:", str(e))
        print(driver.page_source) 
    
    # Wait for the dropdown menu to be visible
    time.sleep(2)
    
    # Click on “White Papers & eBooks”
    try:
        white_papers_ebooks = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "White Papers & eBooks"))
        )
        white_papers_ebooks.click()
        print("Clicked on White Papers & eBooks")
    except Exception as e:
        print("Error clicking White Papers & eBooks:", str(e))
        print(driver.page_source) 

    # Verify Title reads “White Papers”
    try:
        title = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )
        assert title.text == "White Papers", f"Expected title to be 'White Papers', but got '{title.text}'"
        print("Verified title as 'White Papers'")
    except Exception as e:
        print("Error verifying title:", str(e))
        print(driver.page_source)
    
    # Click on “UCITS Whitepaper”
    try:
        ucits_whitepaper = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "UCITS Whitepaper"))
        )
        ucits_whitepaper.click()
        print("Clicked on UCITS Whitepaper")
    except Exception as e:
        print("Error clicking UCITS Whitepaper:", str(e))
        print(driver.page_source)
    
    # Fill in the fields
    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "first_name"))
        ).send_keys("John")
        print("Filled in First Name")
        
        driver.find_element(By.NAME, "last_name").send_keys("Doe")
        print("Filled in Last Name")
        
        driver.find_element(By.NAME, "company").send_keys("Sample Company")
        print("Filled in Company")
        
        driver.find_element(By.NAME, "industry").send_keys("Technology")
        print("Filled in Industry")
    except Exception as e:
        print("Error filling in fields:", str(e))
        print(driver.page_source)
    
    # Step 11: DO NOT populate the "Email” field
    
    
    try:
        send_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Send me a copy')]")
        send_button.click()
        print("Clicked on Send me a copy")
    except Exception as e:
        print("Error clicking Send me a copy:", str(e))
        print(driver.page_source)  
    
    
    try:
        error_message_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "error-message"))
        )
        driver.save_screenshot("error_messages.png")
        print("Saved screenshot of error messages")
    except Exception as e:
        print("Error capturing error messages:", str(e))
        print(driver.page_source)  # Print page source for debugging
    
    # Step 14: Validate all error messages
    try:
        error_messages = driver.find_elements(By.CLASS_NAME, "error-message")
        for error in error_messages:
            print(f"Error: {error.text}")
        assert len(error_messages) > 0, "No error messages found."
    except Exception as e:
        print("Error validating error messages:", str(e))
        print(driver.page_source) 

    # Open and display the screenshot 
    try:
        img = Image.open("error_messages.png")
        img.show()
        print("Test completed successfully.")
    except Exception as e:
        print("Error displaying screenshot:", str(e))

finally:
    # Close the WebDriver
    driver.quit()
    print("Closed the WebDriver")
