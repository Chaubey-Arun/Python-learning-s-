import requests
import random
import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import csv
import os

# Read URLs from the JSON file
with open('C:\\Users\\chaub\\python files project\\Project1\\HandsonProject1.json', 'r') as file:
    web_url = json.load(file)

# Extract the list of URLs
links = web_url['url']

# List of user-agent headers
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
]

# Initialize list to store reviews
all_reviews = []

def fetch_url(url, retries=3):
    for attempt in range(retries):
        try:
            # Select a random user-agent header
            header = {
                "user-agent": random.choice(user_agents)
            }
            
            # Make request to the URL
            response = requests.get(url, headers=header)
            response.raise_for_status()  # Raise an error for bad status codes
            return response
        except requests.RequestException as e:
            print(f"Attempt {attempt + 1} failed for {url}: {e}")
            if attempt + 1 == retries:
                raise
            time.sleep(random.uniform(2.5, 4.5))  # Adjust the pause time between retries

def fetch_url_with_selenium(url):
    options = Options()
    options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
    options.add_argument("--window-size=1920,1200")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-features=IsolateOrigins,site-per-process")
    options.add_argument("--blink-settings=imagesEnabled=true")
    
    # Specify the correct path to chromedriver
    service = Service(executable_path='C:/Users/chaub/python files project/venv/chromedriver-win64/chromedriver.exe')  # Adjust path to chromedriver

    driver = webdriver.Chrome(service=service, options=options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    driver.get(url)
    
    try:
        # Wait until a certain element is loaded (adjust the locator to your needs)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body")))
        page_source = driver.page_source
    finally:
        driver.quit()

    return page_source

# Loop through each URL and scrape reviews
for link in links:
    print(f"Scraping reviews from: {link}\n")

    try:
        if "meesho.com" in link:
            response_text = fetch_url_with_selenium(link)
        else:
            response = fetch_url(link)
            response_text = response.text
    except requests.RequestException as e:
        print(f"Failed to fetch {link}: {e}")
        continue

    # Parse HTML
    soup = BeautifulSoup(response_text, 'html.parser')

    # Check the domain to apply the appropriate parsing logic
    if "amazon.in" in link:
        for index, review_section in enumerate(soup.find_all('div', {'data-hook': 'review'}), start=1):
            start_rating = review_section.find('i', {'data-hook': 'review-star-rating'})
            start_rating_text = start_rating.text.strip() if start_rating else 'No rating'

            time_and_place = review_section.find('span', {'data-hook': 'review-date'})
            time_and_place_text = time_and_place.text.strip() if time_and_place else 'No date'

            review = review_section.find('span', {'data-hook': 'review-body'})
            review_text = review.text.strip() if review else 'No review'

            all_reviews.append({
                'URL': link,
                'Index': index,
                'Rating': start_rating_text,
                'Time and Place': time_and_place_text,
                'Review': review_text
            })
            print('Review Number:', index)
            print('Rating:', start_rating_text)
            print('Time and Place:', time_and_place_text)
            print('Review:', review_text)
            print()
            
    elif "flipkart.com" in link:
        for index, review_section in enumerate(soup.find_all('div', {'class': 'cPHDOP col-12-12'}), start=1):
            start_rating = review_section.find('div', {'class': 'XQDdHH Ga3i8K'})
            start_rating_text = start_rating.text.strip() if start_rating else 'No rating'

            time_and_place = review_section.find('p', {'class': '_2NsDsF'})
            time_and_place_text = time_and_place.text.strip() if time_and_place else 'No date'

            review = review_section.find('div', {'class': 'row'})
            review_text = review.div.div.text.strip() if review else 'No review'

            all_reviews.append({
                'URL': link,
                'Index': index,
                'Rating': start_rating_text,
                'Time and Place': time_and_place_text,
                'Review': review_text
            })
            print('Review Number:', index)
            print('Rating:', start_rating_text)
            print('Time and Place:', time_and_place_text)
            print('Review:', review_text)
            print()
    
    elif "meesho.com" in link:
        for index, review_section in enumerate(soup.find_all('div', {'class': 'sc-bqWxrE hupGZf RatingReviewDrawer__StyledCard-sc-y5ksev-1 eyMVSu RatingReviewDrawer__StyledCard-sc-y5ksev-1 eyMVSu'}), start=1):
            start_rating = review_section.find('span', {'class': 'sc-iJnaPW fGVEwV'})
            start_rating_text = start_rating.text.strip() if start_rating else 'No rating'

            time_and_place = review_section.find('span', {'class': 'sc-eDvSVe XndEO'})
            time_and_place_text = time_and_place.text.strip() if time_and_place else 'No date'

            review = review_section.find('p', {'class': 'sc-eDvSVe gUjMRV Comment__CommentText-sc-1ju5q0e-3 cfdxfJ Comment__CommentText-sc-1ju5q0e-3 cfdxfJ'})
            review_text = review.text.strip() if review else 'No review'

            all_reviews.append({
                'URL': link,
                'Index': index,
                'Rating': start_rating_text,
                'Time and Place': time_and_place_text,
                'Review': review_text
            })
            print('Review Number:', index)
            print('Rating:', start_rating_text)
            print('Time and Place:', time_and_place_text)
            print('Review:', review_text)
            print()

# Save reviews to a CSV file
output_file = 'C:\\Users\\chaub\\python files project\\Project1\\reviews.csv'
output_columns = ['URL', 'Index', 'Rating', 'Time and Place', 'Review']

try:
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=output_columns)
        writer.writeheader()
        writer.writerows(all_reviews)
    print(f"All reviews saved to {output_file}.")
except IOError as e:
    print(f"Failed to save reviews to {output_file}: {e}")
