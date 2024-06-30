# import os
# import json
# import random
# import time
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# def get_proxy_list():
#     api_url = "https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc&protocols=http"
#     try:
#         response = requests.get(api_url)
#         response.raise_for_status()  # Raises an HTTPError for bad responses
#         return response.json()['data']
#     except requests.RequestException as e:
#         print(f"Error fetching proxy list: {e}")
#         return []  # Return an empty list in case of error

# def random_proxy(proxy_list):
#     return random.choice(proxy_list)

# def proxy_obj_to_link(proxy_obj):
#     link = f"{proxy_obj['protocols'][0]}://{proxy_obj['ip']}:{proxy_obj['port']}"
#     return link

# def fetch_url_with_selenium(url):
#     proxy_list = get_proxy_list()
#     proxy_obj = random_proxy(proxy_list)
#     proxy_link = proxy_obj_to_link(proxy_obj=proxy_obj)
#     if not proxy_link.startswith("http://"):
#         proxy_link = "http://" + proxy_link

#     options = Options()
#     options.add_argument(f"--proxy-server={proxy_link}")
#     options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
#     options.add_argument("--window-size=1920,1200")
#     options.add_argument("--disable-gpu")
#     options.add_argument("--no-sandbox")
#     options.add_argument("--disable-features=IsolateOrigins,site-per-process")
#     options.add_argument("--blink-settings=imagesEnabled=true")

#     chromedriver_path = 'C:/Users/chaub/python files project/venv/chromedriver-win64/chromedriver-win64/chromedriver.exe'
#     service = Service(executable_path=chromedriver_path)

#     SELENIUM_HUB_LINK = os.environ.get('SELENIUM_HUB_LINK', 'http://localhost:4444/wd/hub')
#     print(f"SELENIUM_HUB_LINK: {SELENIUM_HUB_LINK}")
#     print(f"Using proxy: {proxy_link}")

#     driver = webdriver.Chrome(service=service, options=options)
#     driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
#     driver.get(url)

#     try:
#         WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body")))
#         page_source = driver.page_source
#     finally:
#         driver.quit()

#     return page_source

# # Read URLs from the JSON file
# with open('C:\\Users\\chaub\\python files project\\Project1\\HandsonProject1.json', 'r') as file:
#     web_url = json.load(file)

# # Extract the list of URLs
# links = web_url['url']

# # List of user-agent headers
# user_agents = [
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
# ]

# # Initialize list to store reviews
# all_reviews = []

# def fetch_url(url, retries=3):
#     proxy_list = get_proxy_list()
#     for attempt in range(retries):
#         try:
#             header = {
#                 "user-agent": random.choice(user_agents)
#             }
#             proxy_obj = random_proxy(proxy_list)
#             proxy = {
#                 'http': proxy_obj_to_link(proxy_obj),
#                 'https': proxy_obj_to_link(proxy_obj)
#             }
#             response = requests.get(url, headers=header, proxies=proxy)
#             response.raise_for_status()  # Raise an error for bad status codes
#             return response
#         except requests.RequestException as e:
#             print(f"Attempt {attempt + 1} failed for {url}: {e}")
#             if attempt + 1 == retries:
#                 raise
#             time.sleep(random.uniform(1, 3))

# # Loop through each URL and scrape reviews
# for link in links:
#     print(f"Scraping reviews from: {link}\n")

#     try:
#         if "meesho.com" in link:
#             response_text = fetch_url_with_selenium(link)
#         else:
#             response = fetch_url(link)
#             response_text = response.text
#     except requests.RequestException as e:
#         print(f"Failed to fetch {link}: {e}")
#         continue

#     soup = BeautifulSoup(response_text, 'html.parser')

#     if "amazon.in" in link:
#         for index, review_section in enumerate(soup.find_all('div', {'data-hook': 'review'}), start=1):
#             start_rating = review_section.find('i', {'data-hook': 'review-star-rating'})
#             start_rating_text = start_rating.text.strip() if start_rating else 'No rating'

#             time_and_place = review_section.find('span', {'data-hook': 'review-date'})
#             time_and_place_text = time_and_place.text.strip() if time_and_place else 'No date'

#             review = review_section.find('span', {'data-hook': 'review-body'})
#             review_text = review.text.strip() if review else 'No review'

#             all_reviews.append({
#                 'URL': link,
#                 'Index': index,
#                 'Rating': start_rating_text,
#                 'Time and Place': time_and_place_text,
#                 'Review': review_text
#             })
#             print('Review Number:', index)
#             print('Rating:', start_rating_text)
#             print('Time and Place:', time_and_place_text)
#             print('Review:', review_text)
#             print()

#     elif "flipkart.com" in link:
#         for index, review_section in enumerate(soup.find_all('div', {'class': 'cPHDOP col-12-12'}), start=1):
#             start_rating = review_section.find('div', {'class': 'XQDdHH Ga3i8K'})
#             start_rating_text = start_rating.text.strip() if start_rating else 'No rating'

#             time_and_place = review_section.find('p', {'class': '_2NsDsF'})
#             time_and_place_text = time_and_place.text.strip() if time_and_place else 'No date'

#             review = review_section.find('div', {'class': 'row'})
#             review_text = review.div.div.text.strip() if review else 'No review'

#             all_reviews.append({
#                 'URL': link,
#                 'Index': index,
#                 'Rating': start_rating_text,
#                 'Time and Place': time_and_place_text,
#                 'Review': review_text
#             })
#             print('Review Number:', index)
#             print('Rating:', start_rating_text)
#             print('Time and Place:', time_and_place_text)
#             print('Review:', review_text)
#             print()
    
#     elif "meesho.com" in link:
#         for index, review_section in enumerate(soup.find_all('div', {'class': 'sc-bqWxrE hupGZf RatingReviewDrawer__StyledCard-sc-y5ksev-1 eyMVSu RatingReviewDrawer__StyledCard-sc-y5ksev-1 eyMVSu'}), start=1):
#             start_rating = review_section.find('span', {'class': 'sc-iJnaPW fGVEwV'})
#             start_rating_text = start_rating.text.strip() if start_rating else 'No rating'

#             time_and_place = review_section.find('span', {'class': 'sc-eDvSVe XndEO'})
#             time_and_place_text = time_and_place.text.strip() if time_and_place else 'No date'

#             review = review_section.find('p', {'class': 'sc-eDvSVe gUjMRV Comment__CommentText-sc-1ju5q0e-3 cfdxfJ Comment__CommentText-sc-1ju5q0e-3 cfdxfJ'})
#             review_text = review.text.strip() if review else 'No review'

#             all_reviews.append({
#                 'URL': link,
#                 'Index': index,
#                 'Rating': start_rating_text,
#                 'Time and Place': time_and_place_text,
#                 'Review': review_text
#             })
#             print('Review Number:', index)
#             print('Rating:', start_rating_text)
#             print('Time and Place:', time_and_place_text)
#             print('Review:', review_text)
#             print()
    
#     elif "makemytrip.com" in link:
#         for index, review_section in enumerate(soup.find_all('div', {'class': 'col-xs-12 reviewUnit'}), start=1):
#             start_rating = review_section.find('span', {'class': 'sprite rating_fill'})
#             start_rating_text = start_rating.text.strip() if start_rating else 'No rating'

#             time_and_place = review_section.find('span', {'class': 'dateAndTime'})
#             time_and_place_text = time_and_place.text.strip() if time_and_place else 'No date'

#             review = review_section.find('p', {'class': 'userRvs__reviewDescription'})
#             review_text = review.text.strip() if review else 'No review'

#             all_reviews.append({
#                 'URL': link,
#                 'Index': index,
#                 'Rating': start_rating_text,
#                 'Time and Place': time_and_place_text,
#                 'Review': review_text
#             })
#             print('Review Number:', index)
#             print('Rating:', start_rating_text)
#             print('Time and Place:', time_and_place_text)
#             print('Review:', review_text)
#             print()

#     time.sleep(random.uniform(2.5, 4.5))  # Adjust the pause time between scrolls

# # Create DataFrame from all reviews
# df = pd.DataFrame(all_reviews)

# # Save the reviews to a CSV file
# df.to_csv('reviews.csv', index=False)

# print("Reviews have been saved to reviews.csv")
import os
import json
import random
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_manual_proxy_list():
    return [
        "http://123.456.789.000:8080",
        "http://234.567.890.123:8080",
        "http://345.678.901.234:8080",
        # Add more proxies here
    ]

def random_manual_proxy(proxy_list):
    return random.choice(proxy_list)

def fetch_url_with_selenium(url):
    proxy_list = get_manual_proxy_list()
    proxy_link = random_manual_proxy(proxy_list)
    if not proxy_link.startswith("http://"):
        proxy_link = "http://" + proxy_link

    options = Options()
    options.add_argument(f"--proxy-server={proxy_link}")
    options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
    options.add_argument("--window-size=1920,1200")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-features=IsolateOrigins,site-per-process")
    options.add_argument("--blink-settings=imagesEnabled=true")

    chromedriver_path = 'C:/Users/chaub/python files project/venv/chromedriver-win64/chromedriver-win64/chromedriver.exe'
    service = Service(executable_path=chromedriver_path)

    SELENIUM_HUB_LINK = os.environ.get('SELENIUM_HUB_LINK', 'http://localhost:4444/wd/hub')
    print(f"SELENIUM_HUB_LINK: {SELENIUM_HUB_LINK}")
    print(f"Using proxy: {proxy_link}")

    driver = webdriver.Chrome(service=service, options=options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    driver.get(url)

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body")))
        page_source = driver.page_source
    finally:
        driver.quit()

    return page_source

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
    proxy_list = get_manual_proxy_list()
    for attempt in range(retries):
        try:
            header = {
                "user-agent": random.choice(user_agents)
            }
            proxy_link = random_manual_proxy(proxy_list)
            proxy = {
                'http': proxy_link,
                'https': proxy_link
            }
            response = requests.get(url, headers=header, proxies=proxy)
            response.raise_for_status()  # Raise an error for bad status codes
            return response
        except requests.RequestException as e:
            print(f"Attempt {attempt + 1} failed for {url}: {e}")
            if attempt + 1 == retries:
                raise
            time.sleep(random.uniform(1, 3))

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

    soup = BeautifulSoup(response_text, 'html.parser')

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
        for index, review_section in enumerate(soup.find_all('div', {'class': 'col _2wzgFH K0kLPL'}), start=1):
            start_rating = review_section.find('div', {'class': '_3LWZlK _1BLPMq'})
            start_rating_text = start_rating.text.strip() if start_rating else 'No rating'

            time_and_place = review_section.find('p', {'class': '_2sc7ZR'})
            time_and_place_text = time_and_place.text.strip() if time_and_place else 'No date'

            review = review_section.find('div', {'class': 't-ZTKy'})
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

    elif "meesho.com" in link:
        for index, review_section in enumerate(soup.find_all('div', {'class': 'Card__BaseCard-sc-b3n78k-0 cBridq jDZRPp'}), start=1):
            start_rating = review_section.find('span', {'class': 'Rating__Text-sc-1rhvpxz-1 kXRkZt'})
            start_rating_text = start_rating.text.strip() if start_rating else 'No rating'

            time_and_place = review_section.find('p', {'class': 'Text__StyledText-sc-oo0kvp-0 giyKoe'})
            time_and_place_text = time_and_place.text.strip() if time_and_place else 'No date'

            review = review_section.find('p', {'class': 'Text__StyledText-sc-oo0kvp-0 hLKHtQ'})
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
    
    elif "makemytrip.com" in link:
        for index, review_section in enumerate(soup.find_all('div', {'class': 'col-xs-12 reviewUnit'}), start=1):
            start_rating = review_section.find('span', {'class': 'sprite rating_fill'})
            start_rating_text = start_rating.text.strip() if start_rating else 'No rating'

            time_and_place = review_section.find('span', {'class': 'dateAndTime'})
            time_and_place_text = time_and_place.text.strip() if time_and_place else 'No date'

            review = review_section.find('p', {'class': 'userRvs__reviewDescription'})
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

    time.sleep(random.uniform(2.5, 4.5))  # Adjust the pause time between scrolls

# Create DataFrame from all reviews
df = pd.DataFrame(all_reviews)

# Save the reviews to a CSV file
df.to_csv('reviews.csv', index=False)

print("Reviews have been saved to reviews.csv")
