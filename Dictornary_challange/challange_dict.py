from selenium import webdriver
from selenium.common.exceptions import WebDriverException

def check_chromedriver():
    chrome_driver_path = r'C:\path\to\chromedriver.exe'  # Update with your Chromedriver path
    
    try:
        # Configure Chrome options if needed
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")  # Optional: Run in headless mode

        # Initialize Chrome WebDriver
        driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_driver_path)
        
        # Example usage: Open a website and print page title
        driver.get('https://www.example.com')
        print(f"Page title: {driver.title}")
        
        # Close the WebDriver session
        driver.quit()
        
        print("Chromedriver check successful.")
    except WebDriverException as e:
        print(f"Error initializing Chromedriver: {e}")

if __name__ == "__main__":
    check_chromedriver()
