# # import os
# # import json
# # import random
# # import time
# # import requests
# # from bs4 import BeautifulSoup
# # import pandas as pd
# # from selenium import webdriver
# # from selenium.webdriver.chrome.service import Service
# # from selenium.webdriver.chrome.options import Options
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC

# # def get_proxy_list():
# #     api_url = "https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc&protocols=http"
# #     try:
# #         response = requests.get(api_url)
# #         response.raise_for_status()  # Raises an HTTPError for bad responses
# #         return response.json()['data']
# #     except requests.RequestException as e:
# #         print(f"Error fetching proxy list: {e}")
# #         return []  # Return an empty list in case of error

# # def random_proxy(proxy_list):
# #     return random.choice(proxy_list)

# # def proxy_obj_to_link(proxy_obj):
# #     link = f"{proxy_obj['protocols'][0]}://{proxy_obj['ip']}:{proxy_obj['port']}"
# #     return link

# # def fetch_url_with_selenium(url):
# #     proxy_list = get_proxy_list()
# #     proxy_obj = random_proxy(proxy_list)
# #     proxy_link = proxy_obj_to_link(proxy_obj=proxy_obj)
# #     if not proxy_link.startswith("http://"):
# #         proxy_link = "http://" + proxy_link

# #     options = Options()
# #     options.add_argument(f"--proxy-server={proxy_link}")
# #     options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
# #     options.add_argument("--window-size=1920,1200")
# #     options.add_argument("--disable-gpu")
# #     options.add_argument("--no-sandbox")
# #     options.add_argument("--disable-features=IsolateOrigins,site-per-process")
# #     options.add_argument("--blink-settings=imagesEnabled=true")

# #     chromedriver_path = 'C:/Users/chaub/python files project/venv/chromedriver-win64/chromedriver-win64/chromedriver.exe'
# #     service = Service(executable_path=chromedriver_path)

# #     SELENIUM_HUB_LINK = os.environ.get('SELENIUM_HUB_LINK', 'http://localhost:4444/wd/hub')
# #     print(f"SELENIUM_HUB_LINK: {SELENIUM_HUB_LINK}")
# #     print(f"Using proxy: {proxy_link}")

# #     driver = webdriver.Chrome(service=service, options=options)
# #     driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
# #     driver.get(url)

# #     try:
# #         WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body")))
# #         page_source = driver.page_source
# #     finally:
# #         driver.quit()

# #     return page_source

# # # Read URLs from the JSON file
# # with open('C:\\Users\\chaub\\python files project\\Project1\\HandsonProject1.json', 'r') as file:
# #     web_url = json.load(file)

# # # Extract the list of URLs
# # links = web_url['url']

# # # List of user-agent headers
# # user_agents = [
# #     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
# #     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
# #     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
# # ]

# # # Initialize list to store reviews
# # all_reviews = []

# # def fetch_url(url, retries=3):
# #     proxy_list = get_proxy_list()
# #     for attempt in range(retries):
# #         try:
# #             header = {
# #                 "user-agent": random.choice(user_agents)
# #             }
# #             proxy_obj = random_proxy(proxy_list)
# #             proxy = {
# #                 'http': proxy_obj_to_link(proxy_obj),
# #                 'https': proxy_obj_to_link(proxy_obj)
# #             }
# #             response = requests.get(url, headers=header, proxies=proxy)
# #             response.raise_for_status()  # Raise an error for bad status codes
# #             return response
# #         except requests.RequestException as e:
# #             print(f"Attempt {attempt + 1} failed for {url}: {e}")
# #             if attempt + 1 == retries:
# #                 raise
# #             time.sleep(random.uniform(1, 3))

# # # Loop through each URL and scrape reviews
# # for link in links:
# #     print(f"Scraping reviews from: {link}\n")

# #     try:
# #         if "meesho.com" in link:
# #             response_text = fetch_url_with_selenium(link)
# #         else:
# #             response = fetch_url(link)
# #             response_text = response.text
# #     except requests.RequestException as e:
# #         print(f"Failed to fetch {link}: {e}")
# #         continue

# #     soup = BeautifulSoup(response_text, 'html.parser')

# #     if "amazon.in" in link:
# #         for index, review_section in enumerate(soup.find_all('div', {'data-hook': 'review'}), start=1):
# #             start_rating = review_section.find('i', {'data-hook': 'review-star-rating'})
# #             start_rating_text = start_rating.text.strip() if start_rating else 'No rating'

# #             time_and_place = review_section.find('span', {'data-hook': 'review-date'})
# #             time_and_place_text = time_and_place.text.strip() if time_and_place else 'No date'

# #             review = review_section.find('span', {'data-hook': 'review-body'})
# #             review_text = review.text.strip() if review else 'No review'

# #             all_reviews.append({
# #                 'URL': link,
# #                 'Index': index,
# #                 'Rating': start_rating_text,
# #                 'Time and Place': time_and_place_text,
# #                 'Review': review_text
# #             })
# #             print('Review Number:', index)
# #             print('Rating:', start_rating_text)
# #             print('Time and Place:', time_and_place_text)
# #             print('Review:', review_text)
# #             print()

# #     elif "flipkart.com" in link:
# #         for index, review_section in enumerate(soup.find_all('div', {'class': 'cPHDOP col-12-12'}), start=1):
# #             start_rating = review_section.find('div', {'class': 'XQDdHH Ga3i8K'})
# #             start_rating_text = start_rating.text.strip() if start_rating else 'No rating'

# #             time_and_place = review_section.find('p', {'class': '_2NsDsF'})
# #             time_and_place_text = time_and_place.text.strip() if time_and_place else 'No date'

# #             review = review_section.find('div', {'class': 'row'})
# #             review_text = review.div.div.text.strip() if review else 'No review'

# #             all_reviews.append({
# #                 'URL': link,
# #                 'Index': index,
# #                 'Rating': start_rating_text,
# #                 'Time and Place': time_and_place_text,
# #                 'Review': review_text
# #             })
# #             print('Review Number:', index)
# #             print('Rating:', start_rating_text)
# #             print('Time and Place:', time_and_place_text)
# #             print('Review:', review_text)
# #             print()
    
# #     elif "meesho.com" in link:
# #         for index, review_section in enumerate(soup.find_all('div', {'class': 'sc-bqWxrE hupGZf RatingReviewDrawer__StyledCard-sc-y5ksev-1 eyMVSu RatingReviewDrawer__StyledCard-sc-y5ksev-1 eyMVSu'}), start=1):
# #             start_rating = review_section.find('span', {'class': 'sc-iJnaPW fGVEwV'})
# #             start_rating_text = start_rating.text.strip() if start_rating else 'No rating'

# #             time_and_place = review_section.find('span', {'class': 'sc-eDvSVe XndEO'})
# #             time_and_place_text = time_and_place.text.strip() if time_and_place else 'No date'

# #             review = review_section.find('p', {'class': 'sc-eDvSVe gUjMRV Comment__CommentText-sc-1ju5q0e-3 cfdxfJ Comment__CommentText-sc-1ju5q0e-3 cfdxfJ'})
# #             review_text = review.text.strip() if review else 'No review'

# #             all_reviews.append({
# #                 'URL': link,
# #                 'Index': index,
# #                 'Rating': start_rating_text,
# #                 'Time and Place': time_and_place_text,
# #                 'Review': review_text
# #             })
# #             print('Review Number:', index)
# #             print('Rating:', start_rating_text)
# #             print('Time and Place:', time_and_place_text)
# #             print('Review:', review_text)
# #             print()
    
# #     elif "makemytrip.com" in link:
# #         for index, review_section in enumerate(soup.find_all('div', {'class': 'col-xs-12 reviewUnit'}), start=1):
# #             start_rating = review_section.find('span', {'class': 'sprite rating_fill'})
# #             start_rating_text = start_rating.text.strip() if start_rating else 'No rating'

# #             time_and_place = review_section.find('span', {'class': 'dateAndTime'})
# #             time_and_place_text = time_and_place.text.strip() if time_and_place else 'No date'

# #             review = review_section.find('p', {'class': 'userRvs__reviewDescription'})
# #             review_text = review.text.strip() if review else 'No review'

# #             all_reviews.append({
# #                 'URL': link,
# #                 'Index': index,
# #                 'Rating': start_rating_text,
# #                 'Time and Place': time_and_place_text,
# #                 'Review': review_text
# #             })
# #             print('Review Number:', index)
# #             print('Rating:', start_rating_text)
# #             print('Time and Place:', time_and_place_text)
# #             print('Review:', review_text)
# #             print()

# #     time.sleep(random.uniform(2.5, 4.5))  # Adjust the pause time between scrolls

# # # Create DataFrame from all reviews
# # df = pd.DataFrame(all_reviews)

# # # Save the reviews to a CSV file
# # df.to_csv('reviews.csv', index=False)

# # print("Reviews have been saved to reviews.csv")
# import requests
# from bs4 import BeautifulSoup

# # Define the URL of the Flipkart product reviews page
# url = 'https://www.meesho.com/cotton-hand-block-printed-short-kurti-kurta-shirt-top-for-women/p/6nh5x6'

# # Make a request to the URL
# response = requests.get(url)
# print(response)
#  # Check that the request was successful
# all_reviews =[]
# # Parse the page content with BeautifulSoup
# soup = BeautifulSoup(response, 'html.parser')
# print(soup.prittify)
# for index, review_section in enumerate(soup.find_all('div', {'class': 'cPHDOP col-12-12'}), start=1):
#             start_rating_text = review_section.find('div', {'class': 'XQDdHH Ga3i8K'})
             

#             time_and_place_text = review_section.find('p', {'class': '_2NsDsF'})
            

#             review_text = review_section.find('div', {'class': 'row'})
             

#             all_reviews.append({
#                 'URL': url,
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


#-------------------------------------------------------------------
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.makemytrip.com/hotels/hotel-details/?hotelId=201101141522264305&_uCurrency=INR&checkin=07222024&checkout=07232024&city=CTDEL&cmp=SEO&country=IN&lat=28.66757&lng=77.09158&locusId=CTDEL&locusType=city&modifyDates=true&rank=2&roomStayQualifier=2e0e&searchText=Delhi&seoDS=true&seoReq=1719441108389&mtkeys=defaultMtkey'

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}

# List to store all reviews
all_reviews = []

print(f'Scraping reviews from: {url}\n')

response = requests.get(url, headers=headers)
response.raise_for_status()
soup = BeautifulSoup(response.text, 'html.parser')


for index, review_section in enumerate(soup.find_all('div', {'class': 'userRvs__item'}), start=1):
    rating_text = review_section.find('span', {'class': 'userRvs__rtng'}).text
    

    date_text1 = review_section.find('div', {'class': 'userRvs__rvdtl'})
    date_text = ''
    for date_text1 in date_text1 : 
         if 'titText' not in date_text1.get('class', []) and 'grayDot' not in date_text1.get('class', []):
            date_text = date_text1.text
            break
    

    review_text= review_section.find('p', {'class': 'font14 lineHight20'}).text
    

    all_reviews.append({
                'URL': url,
                'Index': index,
                'Rating': rating_text,
                'Time and Place': date_text,
                'Review': review_text
            })

    print('Review Number:', index)
    print('Rating:', rating_text)
    print('Time and Place:', date_text)
    print('Review:', review_text)
    print()

df = pd.DataFrame(all_reviews)

# Write DataFrame to CSV file
df.to_csv('reviews_data.csv', index=False)
print('Data saved to reviews1_data.csv')

# Display DataFrame
print('\nDataFrame with all reviews:')
print(df)