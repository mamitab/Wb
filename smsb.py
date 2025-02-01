from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import requests

# ChromeDriver path
chrome_driver_path = 'path/to/chromedriver'

# Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Initialize the WebDriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Open WhatsApp Web
    driver.get('https://web.whatsapp.com/')

    # Wait for the page to load
    time.sleep(15)  # Adjust this time according to your internet speed and page load time

    # Find and enter the phone number
    phone_input = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div/input')
    phone_input.send_keys('+905348305121')
    phone_input.send_keys(Keys.ENTER)

    # Wait for the SMS and Voice call options to appear
    time.sleep(10)

    # Click on the "SMS Gönder" button
    sms_button = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div/span')
    sms_button.click()

    # Wait before sending another request
    time.sleep(10)

    # Click on the "Sesli Arama Gönder" button
    voice_call_button = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[3]/div/span')
    voice_call_button.click()

finally:
    # Close the WebDriver
    driver.quit()

# Check if the latest commit was successful
repo_owner = 'mamitab'
repo_name = 'Wb'
branch = 'main'
url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/commits/{branch}'

response = requests.get(url)

if response.status_code == 200:
    print("En son commit başarılı oldu!")
else:
    print("En son commit başarısız oldu!")
