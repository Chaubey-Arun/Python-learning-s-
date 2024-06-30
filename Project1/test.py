# # # # # # # # # # # # # # import json
# # # # # # # # # # # # # # import requests
# # # # # # # # # # # # # # from bs4 import BeautifulSoup

# # # # # # # # # # # # # # # Load URLs from the JSON file
# # # # # # # # # # # # # # with open('C:\\Users\\chaub\\python files project\\Project1\\HandsonProject1.json', 'r') as file:
# # # # # # # # # # # # # #     web_url = json.loads(file.read())

# # # # # # # # # # # # # # # Extract the list of URLs
# # # # # # # # # # # # # # urls = web_url['url']

# # # # # # # # # # # # # # # User-agent header
# # # # # # # # # # # # # # header = {
# # # # # # # # # # # # # #     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
# # # # # # # # # # # # # # }

# # # # # # # # # # # # # # # Function to scrape reviews from a given URL
# # # # # # # # # # # # # # def scrape_reviews(linkid, url):
# # # # # # # # # # # # # #     reviews = []
# # # # # # # # # # # # # #     try:
# # # # # # # # # # # # # #         response = requests.get(url, headers=header)
# # # # # # # # # # # # # #         response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
# # # # # # # # # # # # # #         soup = BeautifulSoup(response.text, 'html.parser')

# # # # # # # # # # # # # #         # Iterate over each review section
# # # # # # # # # # # # # #         for index, review_section in enumerate(soup.find_all('div', {'class': 'review'}), start=1):  # Update with correct selector
# # # # # # # # # # # # # #             # Extract the star rating
# # # # # # # # # # # # # #             start_rating = review_section.find('span', {'class': 'review-star-rating'})  # Update with correct selector
# # # # # # # # # # # # # #             start_rating_text = start_rating.text.strip() if start_rating else 'No rating'

# # # # # # # # # # # # # #             # Extract the date and place of the review
# # # # # # # # # # # # # #             time_and_place = review_section.find('span', {'class': 'review-date'})  # Update with correct selector
# # # # # # # # # # # # # #             time_and_place_text = time_and_place.text.strip() if time_and_place else 'No date'

# # # # # # # # # # # # # #             # Extract the review text
# # # # # # # # # # # # # #             review = review_section.find('div', {'class': 'review-text'})  # Update with correct selector
# # # # # # # # # # # # # #             review_text = review.text.strip() if review else 'No review'

# # # # # # # # # # # # # #             # Append a dictionary with the extracted information to the reviews list
# # # # # # # # # # # # # #             reviews.append({
# # # # # # # # # # # # # #                 'linkid': linkid,
# # # # # # # # # # # # # #                 'index': index,
# # # # # # # # # # # # # #                 'rating': start_rating_text,
# # # # # # # # # # # # # #                 'time_and_place': time_and_place_text,
# # # # # # # # # # # # # #                 'review': review_text
# # # # # # # # # # # # # #             })
# # # # # # # # # # # # # #     except requests.exceptions.RequestException as e:
# # # # # # # # # # # # # #         print(f"Error fetching reviews from {url}: {str(e)}")

# # # # # # # # # # # # # #     return reviews

# # # # # # # # # # # # # # # Loop through each URL and scrape reviews
# # # # # # # # # # # # # # for linkid, link in enumerate(urls):
# # # # # # # # # # # # # #     print(f"Scraping reviews from {link}...")
# # # # # # # # # # # # # #     reviews = scrape_reviews(linkid, link)

# # # # # # # # # # # # # #     # Print all reviews
# # # # # # # # # # # # # #     for review in reviews:
# # # # # # # # # # # # # #         print('Review Number :-    ', review['index'])
# # # # # # # # # # # # # #         print('Rating :-           ', review['rating'])
# # # # # # # # # # # # # #         print('Time and Place :-   ', review['time_and_place'])
# # # # # # # # # # # # # #         print('Review :-           ', review['review'])
# # # # # # # # # # # # # #         print('linkid :-           ', review['linkid'])
# # # # # # # # # # # # # #         print()  # Add a blank line for readability
# # # # # # # # # # # # # import json
# # # # # # # # # # # # # import requests
# # # # # # # # # # # # # from bs4 import BeautifulSoup
# # # # # # # # # # # # # import pandas as pd

# # # # # # # # # # # # # # Read URLs from the JSON file
# # # # # # # # # # # # # with open('C:\\Users\\chaub\\python files project\\Project1\\HandsonProject1.json', 'r') as file:
# # # # # # # # # # # # #     web_url = json.load(file)

# # # # # # # # # # # # # # Extract the list of URLs
# # # # # # # # # # # # # links = web_url['url']

# # # # # # # # # # # # # # User-agent header
# # # # # # # # # # # # # header = {
# # # # # # # # # # # # #     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
# # # # # # # # # # # # # }

# # # # # # # # # # # # # # Initialize list to store reviews
# # # # # # # # # # # # # all_reviews = []

# # # # # # # # # # # # # # Loop through each URL and scrape reviews
# # # # # # # # # # # # # for link in links:
# # # # # # # # # # # # #     print(f"Scraping reviews from: {link}\n")

# # # # # # # # # # # # #     # Make request to the URL
# # # # # # # # # # # # #     response = requests.get(link, headers=header)
# # # # # # # # # # # # #     response_text = response.text

# # # # # # # # # # # # #     # Parse HTML
# # # # # # # # # # # # #     soup = BeautifulSoup(response_text, 'html.parser')

# # # # # # # # # # # # #     # Check the domain to apply the appropriate parsing logic
# # # # # # # # # # # # #     if "amazon.in" in link:
# # # # # # # # # # # # #         # Iterate over each review section for Amazon
# # # # # # # # # # # # #         for index, review_section in enumerate(soup.find_all('div', {'data-hook': 'review'}), start=1):
# # # # # # # # # # # # #             start_rating = review_section.find('i', {'data-hook': 'review-star-rating'})
# # # # # # # # # # # # #             start_rating_text = start_rating.text.strip() if start_rating else 'No rating'

# # # # # # # # # # # # #             time_and_place = review_section.find('span', {'data-hook': 'review-date'})
# # # # # # # # # # # # #             time_and_place_text = time_and_place.text.strip() if time_and_place else 'No date'

# # # # # # # # # # # # #             review = review_section.find('span', {'data-hook': 'review-body'})
# # # # # # # # # # # # #             review_text = review.text.strip() if review else 'No review'

# # # # # # # # # # # # #             all_reviews.append({
# # # # # # # # # # # # #                 'URL': link,
# # # # # # # # # # # # #                 'Index': index,
# # # # # # # # # # # # #                 'Rating': start_rating_text,
# # # # # # # # # # # # #                 'Time and Place': time_and_place_text,
# # # # # # # # # # # # #                 'Review': review_text
# # # # # # # # # # # # #             })
# # # # # # # # # # # # #             print('Review Number:', index)
# # # # # # # # # # # # #             print('Rating:', start_rating_text)
# # # # # # # # # # # # #             print('Time and Place:', time_and_place_text)
# # # # # # # # # # # # #             print('Review:', review_text)
# # # # # # # # # # # # #             print()
            
# # # # # # # # # # # # #     elif "flipkart.com" in link:
# # # # # # # # # # # # #         # Iterate over each review section for Flipkart
# # # # # # # # # # # # #         for index, review_section in enumerate(soup.find_all('div', {'class': 'cPHDOP col-12-12'}), start=1):
# # # # # # # # # # # # #             start_rating = review_section.find('div', {'class': 'XQDdHH Ga3i8K'})
# # # # # # # # # # # # #             start_rating_text = start_rating.text.strip() if start_rating else 'No rating'

# # # # # # # # # # # # #             time_and_place = review_section.find('p', {'class': '_2NsDsF'})
# # # # # # # # # # # # #             time_and_place_text = time_and_place.text.strip() if time_and_place else 'No date'

# # # # # # # # # # # # #             review = review_section.find('div', {'class': 'row'})
# # # # # # # # # # # # #             review_text = review.div.div.text.strip() if review else 'No review'

# # # # # # # # # # # # #             all_reviews.append({
# # # # # # # # # # # # #                 'URL': link,
# # # # # # # # # # # # #                 'Index': index,
# # # # # # # # # # # # #                 'Rating': start_rating_text,
# # # # # # # # # # # # #                 'Time and Place': time_and_place_text,
# # # # # # # # # # # # #                 'Review': review_text
# # # # # # # # # # # # #             })
# # # # # # # # # # # # #             print('Review Number:', index)
# # # # # # # # # # # # #             print('Rating:', start_rating_text)
# # # # # # # # # # # # #             print('Time and Place:', time_and_place_text)
# # # # # # # # # # # # #             print('Review:', review_text)
# # # # # # # # # # # # #             print()
    
# # # # # # # # # # # # #     elif "meesho.com" in link:
# # # # # # # # # # # # #         # Iterate over each review section for Meesho
# # # # # # # # # # # # #         for index, review_section in enumerate(soup.find_all('div', {'class': 'sc-bqWxrE hupGZf RatingReviewDrawer__StyledCard-sc-y5ksev-1 eyMVSu RatingReviewDrawer__StyledCard-sc-y5ksev-1 eyMVSu'}), start=1):
# # # # # # # # # # # # #             start_rating = review_section.find('span', {'class': 'sc-iJnaPW fGVEwV'})
# # # # # # # # # # # # #             start_rating_text = start_rating.text.strip() if start_rating else 'No rating'

# # # # # # # # # # # # #             time_and_place = review_section.find('span', {'class': 'sc-eDvSVe XndEO'})
# # # # # # # # # # # # #             time_and_place_text = time_and_place.text.strip() if time_and_place else 'No date'

# # # # # # # # # # # # #             review = review_section.find('p', {'class': 'sc-eDvSVe gUjMRV Comment__CommentText-sc-1ju5q0e-3 cfdxfJ Comment__CommentText-sc-1ju5q0e-3 cfdxfJ'})
# # # # # # # # # # # # #             review_text = review.text.strip() if review else 'No review'

# # # # # # # # # # # # #             all_reviews.append({
# # # # # # # # # # # # #                 'URL': link,
# # # # # # # # # # # # #                 'Index': index,
# # # # # # # # # # # # #                 'Rating': start_rating_text,
# # # # # # # # # # # # #                 'Time and Place': time_and_place_text,
# # # # # # # # # # # # #                 'Review': review_text
# # # # # # # # # # # # #             })
# # # # # # # # # # # # #             print('Review Number:', index)
# # # # # # # # # # # # #             print('Rating:', start_rating_text)
# # # # # # # # # # # # #             print('Time and Place:', time_and_place_text)
# # # # # # # # # # # # #             print('Review:', review_text)
# # # # # # # # # # # # #             print()
    
# # # # # # # # # # # # #     elif "makemytrip.com" in link:
# # # # # # # # # # # # #         # Iterate over each review section for MakeMyTrip
# # # # # # # # # # # # #         for index, review_section in enumerate(soup.find_all('div', {'class': 'userRvs '}), start=1):
# # # # # # # # # # # # #             start_rating = review_section.find('span', {'class': 'userRvs__rtng'})
# # # # # # # # # # # # #             start_rating_text = start_rating.text.strip() if start_rating else 'No rating'

# # # # # # # # # # # # #             time_and_place = review_section.find('p', {'class': 'userRvs__rvdtlPoints'})
# # # # # # # # # # # # #             time_and_place_text = time_and_place.text.strip() if time_and_place else 'No date'

# # # # # # # # # # # # #             review = review_section.find('p', {'class': 'font14 lineHight20'})
# # # # # # # # # # # # #             review_text = review.text.strip() if review else 'No review'

# # # # # # # # # # # # #             all_reviews.append({
# # # # # # # # # # # # #                 'URL': link,
# # # # # # # # # # # # #                 'Index': index,
# # # # # # # # # # # # #                 'Rating': start_rating_text,
# # # # # # # # # # # # #                 'Time and Place': time_and_place_text,
# # # # # # # # # # # # #                 'Review': review_text
# # # # # # # # # # # # #             })
# # # # # # # # # # # # #             print('Review Number:', index)
# # # # # # # # # # # # #             print('Rating:', start_rating_text)
# # # # # # # # # # # # #             print('Time and Place:', time_and_place_text)
# # # # # # # # # # # # #             print('Review:', review_text)
# # # # # # # # # # # # #             print()

# # # # # # # # # # # # # # Convert all_reviews list to a Pandas DataFrame
# # # # # # # # # # # # # df = pd.DataFrame(all_reviews)

# # # # # # # # # # # # # # Write DataFrame to Excel file
# # # # # # # # # # # # # excel_file_path = 'C:\\Users\\chaub\\python files project\\Project1\\reviews.xlsx'
# # # # # # # # # # # # # df.to_excel(excel_file_path, index=False)

# # # # # # # # # # # # # print(f'Excel file saved at: {excel_file_path}')
# # # # # # # # # # # # Your code is looking good so far, but it seems incomplete. You need to handle cases where the server might be down and when the retries are exhausted. Additionally, you should ensure that all the required libraries are imported and handle potential exceptions more gracefully. Here's the completed version of your script:

# # # # # # # # # # # # ```python
# # # # # # # # # # # # import requests
# # # # # # # # # # # # from bs4 import BeautifulSoup
# # # # # # # # # # # # import time

# # # # # # # # # # # # def scrape_flipkart_reviews(url, retries=3):
# # # # # # # # # # # #     headers = {
# # # # # # # # # # # #         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
# # # # # # # # # # # #     }
# # # # # # # # # # # #     for attempt in range(retries):
# # # # # # # # # # # #         try:
# # # # # # # # # # # #             response = requests.get(url, headers=headers)
# # # # # # # # # # # #             response.raise_for_status()
# # # # # # # # # # # #             soup = BeautifulSoup(response.content, 'html.parser')
# # # # # # # # # # # #             reviews = soup.find_all("div", {"class": "t-ZTKy"})
# # # # # # # # # # # #             for review in reviews:
# # # # # # # # # # # #                 print(review.get_text().strip())
# # # # # # # # # # # #             return  # Exit if successful
# # # # # # # # # # # #         except requests.exceptions.HTTPError as http_err:
# # # # # # # # # # # #             if response.status_code == 500:
# # # # # # # # # # # #                 print(f"Server error (attempt {attempt + 1}): {http_err}. Retrying...")
# # # # # # # # # # # #                 time.sleep(5)  # Wait for 5 seconds before retrying
# # # # # # # # # # # #             else:
# # # # # # # # # # # #                 print(f"HTTP error occurred: {http_err}")
# # # # # # # # # # # #                 break  # Break the loop for other HTTP errors
# # # # # # # # # # # #         except requests.exceptions.RequestException as req_err:
# # # # # # # # # # # #             print(f"Request error: {req_err}")
# # # # # # # # # # # #             break  # Break the loop for non-HTTP errors
# # # # # # # # # # # #     print("Failed to retrieve reviews after several attempts.")

# # # # # # # # # # # # # Example usage:
# # # # # # # # # # # # url = "https://www.flipkart.com/product-reviews-page-url"  # Replace with the actual URL
# # # # # # # # # # # # scrape_flipkart_reviews(url)
# # # # # # # # # # # # ```

# # # # # # # # # # # # **Key Changes:**
# # # # # # # # # # # # 1. The script now prints and strips the review text to remove any leading/trailing whitespace.
# # # # # # # # # # # # 2. It handles HTTP errors more explicitly by breaking the loop for non-500 status codes.
# # # # # # # # # # # # 3. It catches all request exceptions to handle non-HTTP related errors.
# # # # # # # # # # # # 4. It prints a message when it fails to retrieve reviews after exhausting retries.

# # # # # # # # # # # # Replace `"https://www.flipkart.com/product-reviews-page-url"` with the actual URL of the Flipkart product review page you want to scrape.import requests
# # # # # # # # # # # from bs4 import BeautifulSoup
# # # # # # # # # # # import time

# # # # # # # # # # # def scrape_flipkart_reviews(url, retries=3):
# # # # # # # # # # #     headers = {
# # # # # # # # # # #         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
# # # # # # # # # # #     }
# # # # # # # # # # #     for attempt in range(retries):
# # # # # # # # # # #         try:
# # # # # # # # # # #             response = requests.get(url, headers=headers, timeout=10)
# # # # # # # # # # #             response.raise_for_status()
# # # # # # # # # # #             soup = BeautifulSoup(response.content, 'html.parser')
# # # # # # # # # # #             reviews = soup.find_all("div", {"class": "t-ZTKy"})
# # # # # # # # # # #             if not reviews:
# # # # # # # # # # #                 print("No reviews found. The structure of the page might have changed.")
# # # # # # # # # # #                 return
# # # # # # # # # # #             for review in reviews:
# # # # # # # # # # #                 print(review.get_text().strip())
# # # # # # # # # # #             return  # Exit if successful
# # # # # # # # # # #         except requests.exceptions.HTTPError as http_err:
# # # # # # # # # # #             if response.status_code == 500:
# # # # # # # # # # #                 print(f"Server error (attempt {attempt + 1}): {http_err}. Retrying...")
# # # # # # # # # # #                 time.sleep(5)  # Wait for 5 seconds before retrying
# # # # # # # # # # #             elif response.status_code == 403:
# # # # # # # # # # #                 print(f"Access forbidden (attempt {attempt + 1}): {http_err}. Check User-Agent.")
# # # # # # # # # # #                 break
# # # # # # # # # # #             elif response.status_code == 404:
# # # # # # # # # # #                 print(f"Page not found: {http_err}. Check the URL.")
# # # # # # # # # # #                 break
# # # # # # # # # # #             else:
# # # # # # # # # # #                 print(f"HTTP error occurred: {http_err}")
# # # # # # # # # # #                 break  # Break the loop for other HTTP errors
# # # # # # # # # # #         except requests.exceptions.RequestException as req_err:
# # # # # # # # # # #             print(f"Request error: {req_err}")
# # # # # # # # # # #             break  # Break the loop for non-HTTP errors
# # # # # # # # # # #         except Exception as e:
# # # # # # # # # # #             print(f"An error occurred: {e}")
# # # # # # # # # # #             break
# # # # # # # # # # #     print("Failed to retrieve reviews after several attempts.")

# # # # # # # # # # # # Example usage:
# # # # # # # # # # # url = "https://www.flipkart.com/product-reviews-page-url"  # Replace with the actual URL
# # # # # # # # # # # scrape_flipkart_reviews(url)
# # # # # # # # # # import requests
# # # # # # # # # # from bs4 import BeautifulSoup
# # # # # # # # # # import time

# # # # # # # # # # def scrape_flipkart_reviews(url, retries=3):
# # # # # # # # # #     headers = {
# # # # # # # # # #         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
# # # # # # # # # #     }
# # # # # # # # # #     for attempt in range(retries):
# # # # # # # # # #         try:
# # # # # # # # # #             response = requests.get(url, headers=headers, timeout=10)
# # # # # # # # # #             response.raise_for_status()
# # # # # # # # # #             soup = BeautifulSoup(response.content, 'html.parser')
# # # # # # # # # #             reviews = soup.find_all("div", {"class": "t-ZTKy"})
# # # # # # # # # #             if not reviews:
# # # # # # # # # #                 print("No reviews found. The structure of the page might have changed.")
# # # # # # # # # #                 return
# # # # # # # # # #             for review in reviews:
# # # # # # # # # #                 print(review.get_text().strip())
# # # # # # # # # #             return  # Exit if successful
# # # # # # # # # #         except requests.exceptions.HTTPError as http_err:
# # # # # # # # # #             if response.status_code == 500:
# # # # # # # # # #                 print(f"Server error (attempt {attempt + 1}): {http_err}. Retrying...")
# # # # # # # # # #                 time.sleep(5)  # Wait for 5 seconds before retrying
# # # # # # # # # #             elif response.status_code == 403:
# # # # # # # # # #                 print(f"Access forbidden (attempt {attempt + 1}): {http_err}. Check User-Agent.")
# # # # # # # # # #                 break
# # # # # # # # # #             elif response.status_code == 404:
# # # # # # # # # #                 print(f"Page not found: {http_err}. Check the URL.")
# # # # # # # # # #                 break
# # # # # # # # # #             else:
# # # # # # # # # #                 print(f"HTTP error occurred: {http_err}")
# # # # # # # # # #                 break  # Break the loop for other HTTP errors
# # # # # # # # # #         except requests.exceptions.RequestException as req_err:
# # # # # # # # # #             print(f"Request error: {req_err}")
# # # # # # # # # #             break  # Break the loop for non-HTTP errors
# # # # # # # # # #         except Exception as e:
# # # # # # # # # #             print(f"An error occurred: {e}")
# # # # # # # # # #             break
# # # # # # # # # #     print("Failed to retrieve reviews after several attempts.")

# # # # # # # # # # # Example usage:
# # # # # # # # # # url = "https://www.flipkart.com/product-reviews-page-url"  # Replace with the actual URL
# # # # # # # # # # scrape_flipkart_reviews(url)
# # # # # # # # # import json
# # # # # # # # # import requests
# # # # # # # # # from bs4 import BeautifulSoup
# # # # # # # # # import pandas as pd
# # # # # # # # # import random
# # # # # # # # # import time

# # # # # # # # # # Read URLs from the JSON file
# # # # # # # # # with open('C:\\Users\\chaub\\python files project\\Project1\\HandsonProject1.json', 'r') as file:
# # # # # # # # #     web_url = json.load(file)

# # # # # # # # # # Extract the list of URLs
# # # # # # # # # links = web_url['url']

# # # # # # # # # # List of user-agent headers
# # # # # # # # # user_agents = [
# # # # # # # # #     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
# # # # # # # # #     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
# # # # # # # # #     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
# # # # # # # # # ]

# # # # # # # # # # Initialize list to store reviews
# # # # # # # # # all_reviews = []

# # # # # # # # # def fetch_url(url, retries=3):
# # # # # # # # #     for attempt in range(retries):
# # # # # # # # #         try:
# # # # # # # # #             # Select a random user-agent header
# # # # # # # # #             header = {
# # # # # # # # #                 "user-agent": random.choice(user_agents)
# # # # # # # # #             }
# # # # # # # # #             # Make request to the URL
# # # # # # # # #             response = requests.get(url, headers=header)
# # # # # # # # #             response.raise_for_status()  # Raise an error for bad status codes
# # # # # # # # #             return response
# # # # # # # # #         except requests.RequestException as e:
# # # # # # # # #             print(f"Attempt {attempt + 1} failed for {url}: {e}")
# # # # # # # # #             if attempt + 1 == retries:
# # # # # # # # #                 raise
# # # # # # # # #             time.sleep(random.uniform(1, 3))

# # # # # # # # # # Loop through each URL and scrape reviews
# # # # # # # # # for link in links:
# # # # # # # # #     print(f"Scraping reviews from: {link}\n")

# # # # # # # # #     try:
# # # # # # # # #         response = fetch_url(link)
# # # # # # # # #         response_text = response.text
# # # # # # # # #     except requests.RequestException as e:
# # # # # # # # #         print(f"Failed to fetch {link}: {e}")
# # # # # # # # #         continue

# # # # # # # # #     # Parse HTML
# # # # # # # # #     soup = BeautifulSoup(response_text, 'html.parser')

# # # # # # # # #     # Check the domain to apply the appropriate parsing logic
# # # # # # # # #     if "amazon.in" in link:
# # # # # # # # #         for index, review_section in enumerate(soup.find_all('div', {'data-hook': 'review'}), start=1):
# # # # # # # # #             start_rating = review_section.find('i', {'data-hook': 'review-star-rating'})
# # # # # # # # #             start_rating_text = start_rating.text.strip() if start_rating else 'No rating'

# # # # # # # # #             time_and_place = review_section.find('span', {'data-hook': 'review-date'})
# # # # # # # # #             time_and_place_text = time_and_place.text.strip() if time_and_place else 'No date'

# # # # # # # # #             review = review_section.find('span', {'data-hook': 'review-body'})
# # # # # # # # #             review_text = review.text.strip() if review else 'No review'

# # # # # # # # #             all_reviews.append({
# # # # # # # # #                 'URL': link,
# # # # # # # # #                 'Index': index,
# # # # # # # # #                 'Rating': start_rating_text,
# # # # # # # # #                 'Time and Place': time_and_place_text,
# # # # # # # # #                 'Review': review_text
# # # # # # # # #             })
# # # # # # # # #             print('Review Number:', index)
# # # # # # # # #             print('Rating:', start_rating_text)
# # # # # # # # #             print('Time and Place:', time_and_place_text)
# # # # # # # # #             print('Review:', review_text)
# # # # # # # # #             print()
            
# # # # # # # # #     elif "flipkart.com" in link:
# # # # # # # # #         for index, review_section in enumerate(soup.find_all('div', {'class': 'cPHDOP col-12-12'}), start=1):
# # # # # # # # #             start_rating = review_section.find('div', {'class': 'XQDdHH Ga3i8K'})
# # # # # # # # #             start_rating_text = start_rating.text.strip() if start_rating else 'No rating'

# # # # # # # # #             time_and_place = review_section.find('p', {'class': '_2NsDsF'})
# # # # # # # # #             time_and_place_text = time_and_place.text.strip() if time_and_place else 'No date'

# # # # # # # # #             review = review_section.find('div', {'class': 'row'})
# # # # # # # # #             review_text = review.div.div.text.strip() if review else 'No review'

# # # # # # # # #             all_reviews.append({
# # # # # # # # #                 'URL': link,
# # # # # # # # #                 'Index': index,
# # # # # # # # #                 'Rating': start_rating_text,
# # # # # # # # #                 'Time and Place': time_and_place_text,
# # # # # # # # #                 'Review': review_text
# # # # # # # # #             })
# # # # # # # # #             print('Review Number:', index)
# # # # # # # # #             print('Rating:', start_rating_text)
# # # # # # # # #             print('Time and Place:', time_and_place_text)
# # # # # # # # #             print('Review:', review_text)
# # # # # # # # #             print()
    
# # # # # # # # #     elif "meesho.com" in link:
# # # # # # # # #         for index, review_section in enumerate(soup.find_all('div', {'class': 'sc-bqWxrE hupGZf RatingReviewDrawer__StyledCard-sc-y5ksev-1 eyMVSu RatingReviewDrawer__StyledCard-sc-y5ksev-1 eyMVSu'}), start=1):
# # # # # # # # #             start_rating = review_section.find('span', {'class': 'sc-iJnaPW fGVEwV'})
# # # # # # # # #             start_rating_text = start_rating.text.strip() if start_rating else 'No rating'

# # # # # # # # #             time_and_place = review_section.find('span', {'class': 'sc-eDvSVe XndEO'})
# # # # # # # # #             time_and_place_text = time_and_place.text.strip() if time_and_place else 'No date'

# # # # # # # # #             review = review_section.find('p', {'class': 'sc-eDvSVe gUjMRV Comment__CommentText-sc-1ju5q0e-3 cfdxfJ Comment__CommentText-sc-1ju5q0e-3 cfdxfJ'})
# # # # # # # # #             review_text = review.text.strip() if review else 'No review'

# # # # # # # # #             all_reviews.append({
# # # # # # # # #                 'URL': link,
# # # # # # # # #                 'Index': index,
# # # # # # # # #                 'Rating': start_rating_text,
# # # # # # # # #                 'Time and Place': time_and_place_text,
# # # # # # # # #                 'Review': review_text
# # # # # # # # #             })
# # # # # # # # #             print('Review Number:', index)
# # # # # # # # #             print('Rating:', start_rating_text)
# # # # # # # # #             print('Time and Place:', time_and_place_text)
# # # # # # # # #             print('Review:', review_text)
# # # # # # # # #             print()
    
# # # # # # # # #     elif "makemytrip.com" in link:
# # # # # # # # #         for index, review_section in enumerate(soup.find_all('div', {'class': 'userRvs '}), start=1):
# # # # # # # # #             start_rating = review_section.find('span', {'class': 'userRvs__rtng'})
# # # # # # # # #             start_rating_text = start_rating.text.strip() if start_rating else 'No rating'

# # # # # # # # #             time_and_place = review_section.find('p', {'class': 'userRvs__rvdtlPoints'})
# # # # # # # # #             time_and_place_text = time_and_place.text.strip() if time_and_place else 'No date'

# # # # # # # # #             review = review_section.find('p', {'class': 'font14 lineHight20'})
# # # # # # # # #             review_text = review.text.strip() if review else 'No review'

# # # # # # # # #             all_reviews.append({
# # # # # # # # #                 'URL': link,
# # # # # # # # #                 'Index': index,
# # # # # # # # #                 'Rating': start_rating_text,
# # # # # # # # #                 'Time and Place': time_and_place_text,
# # # # # # # # #                 'Review': review_text
# # # # # # # # #             })
# # # # # # # # #             print('Review Number:', index)
# # # # # # # # #             print('Rating:', start_rating_text)
# # # # # # # # #             print('Time and Place:', time_and_place_text)
# # # # # # # # #             print('Review:', review_text)
# # # # # # # # #             print()

# # # # # # # # #     # Implement rate limiting
# # # # # # # # #     time.sleep(random.uniform(1, 3))

# # # # # # # # # # Convert all_reviews list to a Pandas DataFrame
# # # # # # # # # df = pd.DataFrame(all_reviews)

# # # # # # # # # # Write DataFrame to Excel file
# # # # # # # # # excel_file_path = 'C:\\Users\\chaub\\python files project\\Project1\\reviews.xlsx'
# # # # # # # # # df.to_excel(excel_file_path, index=False)

# # # # # # # # # print(f'Excel file saved at: {excel_file_path}')
# # # # # # # # import requests
# # # # # # # # from bs4 import BeautifulSoup
# # # # # # # # import time

# # # # # # # # def scrape_flipkart_reviews(url, retries=3, timeout=20):
# # # # # # # #     headers = {
# # # # # # # #         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
# # # # # # # #     }
# # # # # # # #     backoff_factor = 1

# # # # # # # #     for attempt in range(retries):
# # # # # # # #         try:
# # # # # # # #             response = requests.get(url, headers=headers, timeout=timeout)
# # # # # # # #             response.raise_for_status()
# # # # # # # #             soup = BeautifulSoup(response.content, 'html.parser')
# # # # # # # #             reviews = soup.find_all("div", {"class": "t-ZTKy"})
# # # # # # # #             if not reviews:
# # # # # # # #                 print("No reviews found. The structure of the page might have changed.")
# # # # # # # #                 return
# # # # # # # #             for review in reviews:
# # # # # # # #                 print(review.get_text().strip())
# # # # # # # #             return  # Exit if successful
# # # # # # # #         except requests.exceptions.HTTPError as http_err:
# # # # # # # #             print(f"HTTP error occurred: {http_err}")
# # # # # # # #             break  # Break the loop for HTTP errors
# # # # # # # #         except requests.exceptions.RequestException as req_err:
# # # # # # # #             print(f"Request error (attempt {attempt + 1}): {req_err}. Retrying in {backoff_factor ** attempt} seconds...")
# # # # # # # #             time.sleep(backoff_factor ** attempt)  # Exponential backoff
# # # # # # # #     print("Failed to retrieve reviews after several attempts.")

# # # # # # # # # Example usage:
# # # # # # # # url = "https://www.flipkart.com/product-reviews-page-url"  # Replace with the actual URL
# # # # # # # # scrape_flipkart_reviews(url)
# # # # # # # import json
# # # # # # # import requests
# # # # # # # from bs4 import BeautifulSoup
# # # # # # # import pandas as pd
# # # # # # # import random
# # # # # # # import time
# # # # # # # from selenium import webdriver
# # # # # # # from selenium.webdriver.chrome.service import Service
# # # # # # # from selenium.webdriver.common.by import By
# # # # # # # from selenium.webdriver.chrome.options import Options
# # # # # # # from selenium.webdriver.support.ui import WebDriverWait
# # # # # # # from selenium.webdriver.support import expected_conditions as EC

# # # # # # # # Read URLs from the JSON file
# # # # # # # with open('C:\\Users\\chaub\\python files project\\Project1\\HandsonProject1.json', 'r') as file:
# # # # # # #     web_url = json.load(file)

# # # # # # # # Extract the list of URLs
# # # # # # # links = web_url['url']

# # # # # # # # List of user-agent headers
# # # # # # # user_agents = [
# # # # # # #     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
# # # # # # #     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
# # # # # # #     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
# # # # # # # ]

# # # # # # # # List of proxies
# # # # # # # proxies = [
# # # # # # #     # Add proxies here in the form 'http://user:password@ip:port' or just 'http://ip:port'
# # # # # # # ]

# # # # # # # # Initialize list to store reviews
# # # # # # # all_reviews = []

# # # # # # # def fetch_url(url, retries=3):
# # # # # # #     for attempt in range(retries):
# # # # # # #         try:
# # # # # # #             # Select a random user-agent header
# # # # # # #             header = {
# # # # # # #                 "user-agent": random.choice(user_agents)
# # # # # # #             }
# # # # # # #             # Select a random proxy
# # # # # # #             proxy = {
# # # # # # #                 'http': random.choice(proxies),
# # # # # # #                 'https': random.choice(proxies)
# # # # # # #             } if proxies else None
            
# # # # # # #             # Make request to the URL
# # # # # # #             response = requests.get(url, headers=header, proxies=proxy)
# # # # # # #             response.raise_for_status()  # Raise an error for bad status codes
# # # # # # #             return response
# # # # # # #         except requests.RequestException as e:
# # # # # # #             print(f"Attempt {attempt + 1} failed for {url}: {e}")
# # # # # # #             if attempt + 1 == retries:
# # # # # # #                 raise
# # # # # # #             time.sleep(random.uniform(1, 3))

# # # # # # # def fetch_url_with_selenium(url):
# # # # # # #     options = Options()
# # # # # # #     options.headless = True
# # # # # # #     options.add_argument(f"user-agent={random.choice(user_agents)}")
# # # # # # #     service = Service(executable_path='path/to/chromedriver')  # Adjust path to chromedriver

# # # # # # #     driver = webdriver.Chrome(service=service, options=options)
# # # # # # #     driver.get(url)
    
# # # # # # #     try:
# # # # # # #         # Wait until a certain element is loaded (adjust the locator to your needs)
# # # # # # #         WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "some-css-selector")))
# # # # # # #         page_source = driver.page_source
# # # # # # #     finally:
# # # # # # #         driver.quit()

# # # # # # #     return page_source

# # # # # # # # Loop through each URL and scrape reviews
# # # # # # # for link in links:
# # # # # # #     print(f"Scraping reviews from: {link}\n")

# # # # # # #     try:
# # # # # # #         if "meesho.com" in link:
# # # # # # #             response_text = fetch_url_with_selenium(link)
# # # # # # #         else:
# # # # # # #             response = fetch_url(link)
# # # # # # #             response_text = response.text
# # # # # # #     except requests.RequestException as e:
# # # # # # #         print(f"Failed to fetch {link}: {e}")
# # # # # # #         continue

# # # # # # #     # Parse HTML
# # # # # # #     soup = BeautifulSoup(response_text, 'html.parser')

# # # # # # #     # Check the domain to apply the appropriate parsing logic
# # # # # # #     if "amazon.in" in link:
# # # # # # #         for index, review_section in enumerate(soup.find_all('div', {'data-hook': 'review'}), start=1):
# # # # # # #             start_rating = review_section.find('i', {'data-hook': 'review-star-rating'})
# # # # # # #             start_rating_text = start_rating.text.strip() if start_rating else 'No rating'

# # # # # # #             time_and_place = review_section.find('span', {'data-hook': 'review-date'})
# # # # # # #             time_and_place_text = time_and_place.text.strip() if time_and_place else 'No date'

# # # # # # #             review = review_section.find('span', {'data-hook': 'review-body'})
# # # # # # #             review_text = review.text.strip() if review else 'No review'

# # # # # # #             all_reviews.append({
# # # # # # #                 'URL': link,
# # # # # # #                 'Index': index,
# # # # # # #                 'Rating': start_rating_text,
# # # # # # #                 'Time and Place': time_and_place_text,
# # # # # # #                 'Review': review_text
# # # # # # #             })
# # # # # # #             print('Review Number:', index)
# # # # # # #             print('Rating:', start_rating_text)
# # # # # # #             print('Time and Place:', time_and_place_text)
# # # # # # #             print('Review:', review_text)
# # # # # # #             print()
            
# # # # # # #     elif "flipkart.com" in link:
# # # # # # #         for index, review_section in enumerate(soup.find_all('div', {'class': 'cPHDOP col-12-12'}), start=1):
# # # # # # #             start_rating = review_section.find('div', {'class': 'XQDdHH Ga3i8K'})
# # # # # # #             start_rating_text = start_rating.text.strip() if start_rating else 'No rating'

# # # # # # #             time_and_place = review_section.find('p', {'class': '_2NsDsF'})
# # # # # # #             time_and_place_text = time_and_place.text.strip() if time_and_place else 'No date'

# # # # # # #             review = review_section.find('div', {'class': 'row'})
# # # # # # #             review_text = review.div.div.text.strip() if review else 'No review'

# # # # # # #             all_reviews.append({
# # # # # # #                 'URL': link,
# # # # # # #                 'Index': index,
# # # # # # #                 'Rating': start_rating_text,
# # # # # # #                 'Time and Place': time_and_place_text,
# # # # # # #                 'Review': review_text
# # # # # # #             })
# # # # # # #             print('Review Number:', index)
# # # # # # #             print('Rating:', start_rating_text)
# # # # # # #             print('Time and Place:', time_and_place_text)
# # # # # # #             print('Review:', review_text)
# # # # # # #             print()
    
# # # # # # #     elif "meesho.com" in link:
# # # # # # #         for index, review_section in enumerate(soup.find_all('div', {'class': 'sc-bqWxrE hupGZf RatingReviewDrawer__StyledCard-sc-y5ksev-1 eyMVSu RatingReviewDrawer__StyledCard-sc-y5ksev-1 eyMVSu'}), start=1):
# # # # # # #             start_rating = review_section.find('span', {'class': 'sc-iJnaPW fGVEwV'})
# # # # # # #             start_rating_text = start_rating.text.strip() if start_rating else 'No rating'

# # # # # # #             time_and_place = review_section.find('span', {'class': 'sc-eDvSVe XndEO'})
# # # # # # #             time_and_place_text = time_and_place.text.strip() if time_and_place else 'No date'

# # # # # # #             review = review_section.find('p', {'class': 'sc-eDvSVe gUjMRV Comment__CommentText-sc-1ju5q0e-3 cfdxfJ Comment__CommentText-sc-1ju5q0e-3 cfdxfJ'})
# # # # # # #             review_text = review.text.strip() if review else 'No review'

# # # # # # #             all_reviews.append({
# # # # # # #                 'URL': link,
# # # # # # #                 'Index': index,
# # # # # # #                 'Rating': start_rating_text,
# # # # # # #                 'Time and Place': time_and_place_text,
# # # # # # #                 'Review': review_text
# # # # # # #             })
# # # # # # #             print('Review Number:', index)
# # # # # # #             print('Rating:', start_rating_text)
# # # # # # #             print('Time and Place:', time_and_place_text)
# # # # # # #             print('Review:', review_text)
# # # # # # #             print()
    
# # # # # # #     elif "makemytrip.com" in link:
# # # # # # #         for index, review_section in enumerate(soup.find_all('div', {'class': 'userRvs '}), start=1):
# # # # # # #             start_rating = review_section.find('span', {'class': 'userRvs__rtng'})
# # # # # # #             start_rating_text = start_rating.text.strip() if start_rating else 'No rating'

# # # # # # #             time_and_place = review_section.find('p', {'class': 'userRvs__rvdtlPoints'})
# # # # # # #             time_and_place_text = time_and_place.text.strip() if time_and_place else 'No date'

# # # # # # #             review = review_section.find('p', {'class': 'font14 lineHight20'})
# # # # # # #             review_text = review.text.strip() if review else 'No review'

# # # # # # #             all_reviews.append({
# # # # # # #                 'URL': link,
# # # # # # #                 'Index': index,
# # # # # # #                 'Rating': start_rating_text,
# # # # # # #                 'Time and Place': time_and_place_text,
# # # # # # #                 'Review': review_text
# # # # # # #             })
# # # # # # #             print('Review Number:', index)
# # # # # # #             print('Rating:', start_rating_text)
# # # # # # #             print('Time and Place:', time_and_place_text)
# # # # # # #             print('Review:', review_text)
# # # # # # #             print()

# # # # # # #     # Implement rate limiting
# # # # # # #     time.sleep(random.uniform(1, 3))

# # # # # # # # Convert all_reviews list to a Pandas DataFrame
# # # # # # # df = pd.DataFrame(all_reviews)

# # # # # # # # Write DataFrame to Excel file
# # # # # # # excel_file_path = 'C:\\Users\\chaub\\python files project\\Project1\\reviews.xlsx'
# # # # # # # df.to_excel(excel_file_path, index=False)

# # # # # # # print(f'Excel file saved at: {excel_file_path}')
# # # # # # test_url = "https://www.google.com"
# # # # # # try:
# # # # # #     test_response = requests.get(test_url, proxies=proxies, timeout=10)
# # # # # #     print(test_response.status_code)
# # # # # # except Exception as e:
# # # # # #     print(f"Proxy test failed: {e}")
# # # # # import json
# # # # # import requests
# # # # # from bs4 import BeautifulSoup
# # # # # import pandas as pd
# # # # # import random
# # # # # import time
# # # # # from selenium import webdriver
# # # # # from selenium.webdriver.chrome.service import Service
# # # # # from selenium.webdriver.common.by import By
# # # # # from selenium.webdriver.chrome.options import Options
# # # # # from selenium.webdriver.support.ui import WebDriverWait
# # # # # from selenium.webdriver.support import expected_conditions as EC

# # # # # # Read URLs from the JSON file
# # # # # with open('C:\\Users\\chaub\\python files project\\Project1\\HandsonProject1.json', 'r') as file:
# # # # #     web_url = json.load(file)

# # # # # # Extract the list of URLs
# # # # # links = web_url['url']

# # # # # # List of user-agent headers
# # # # # user_agents = [
# # # # #     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
# # # # #     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
# # # # #     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
# # # # # ]

# # # # # # List of free proxies
# # # # # proxies = [
# # # # #     'http://165.22.61.13:8080',
# # # # #     'http://167.172.180.46:3388',
# # # # #     'http://103.231.202.126:43786',
# # # # #     'http://165.227.71.60:80',
# # # # #     'http://45.76.149.231:3128'
# # # # # ]

# # # # # # Initialize list to store reviews
# # # # # all_reviews = []

# # # # # def fetch_url(url, retries=3):
# # # # #     for attempt in range(retries):
# # # # #         try:
# # # # #             # Select a random user-agent header
# # # # #             header = {
# # # # #                 "user-agent": random.choice(user_agents)
# # # # #             }
# # # # #             # Select a random proxy
# # # # #             proxy = {
# # # # #                 'http': random.choice(proxies),
# # # # #                 'https': random.choice(proxies)
# # # # #             }
            
# # # # #             # Make request to the URL
# # # # #             response = requests.get(url, headers=header, proxies=proxy)
# # # # #             response.raise_for_status()  # Raise an error for bad status codes
# # # # #             return response
# # # # #         except requests.RequestException as e:
# # # # #             print(f"Attempt {attempt + 1} failed for {url}: {e}")
# # # # #             if attempt + 1 == retries:
# # # # #                 raise
# # # # #             time.sleep(random.uniform(1, 3))

# # # # # def fetch_url_with_selenium(url):
# # # # #     options = Options()
# # # # #     options.headless = True
# # # # #     options.add_argument(f"user-agent={random.choice(user_agents)}")
# # # # #     service = Service(executable_path='path/to/chromedriver')  # Adjust path to chromedriver

# # # # #     driver = webdriver.Chrome(service=service, options=options)
# # # # #     driver.get(url)
    
# # # # #     try:
# # # # #         # Wait until a certain element is loaded (adjust the locator to your needs)
# # # # #         WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "some-css-selector")))
# # # # #         page_source = driver.page_source
# # # # #     finally:
# # # # #         driver.quit()

# # # # #     return page_source

# # # # # # Loop through each URL and scrape reviews
# # # # # for link in links:
# # # # #     print(f"Scraping reviews from: {link}\n")

# # # # #     try:
# # # # #         if "meesho.com" in link:
# # # # #             response_text = fetch_url_with_selenium(link)
# # # # #         else:
# # # # #             response = fetch_url(link)
# # # # #             response_text = response.text
# # # # #     except requests.RequestException as e:
# # # # #         print(f"Failed to fetch {link}: {e}")
# # # # #         continue

# # # # #     # Parse HTML
# # # # #     soup = BeautifulSoup(response_text, 'html.parser')

# # # # #     # Check the domain to apply the appropriate parsing logic
# # # # #     if "amazon.in" in link:
# # # # #         for index, review_section in enumerate(soup.find_all('div', {'data-hook': 'review'}), start=1):
# # # # #             start_rating = review_section.find('i', {'data-hook': 'review-star-rating'})
# # # # #             start_rating_text = start_rating.text.strip() if start_rating else 'No rating'

# # # # #             time_and_place = review_section.find('span', {'data-hook': 'review-date'})
# # # # #             time_and_place_text = time_and_place.text.strip() if time_and_place else 'No date'

# # # # #             review = review_section.find('span', {'data-hook': 'review-body'})
# # # # #             review_text = review.text.strip() if review else 'No review'

# # # # #             all_reviews.append({
# # # # #                 'URL': link,
# # # # #                 'Index': index,
# # # # #                 'Rating': start_rating_text,
# # # # #                 'Time and Place': time_and_place_text,
# # # # #                 'Review': review_text
# # # # #             })
# # # # #             print('Review Number:', index)
# # # # #             print('Rating:', start_rating_text)
# # # # #             print('Time and Place:', time_and_place_text)
# # # # #             print('Review:', review_text)
# # # # #             print()
            
# # # # #     elif "flipkart.com" in link:
# # # # #         for index, review_section in enumerate(soup.find_all('div', {'class': 'cPHDOP col-12-12'}), start=1):
# # # # #             start_rating = review_section.find('div', {'class': 'XQDdHH Ga3i8K'})
# # # # #             start_rating_text = start_rating.text.strip() if start_rating else 'No rating'

# # # # #             time_and_place = review_section.find('p', {'class': '_2NsDsF'})
# # # # #             time_and_place_text = time_and_place.text.strip() if time_and_place else 'No date'

# # # # #             review = review_section.find('div', {'class': 'row'})
# # # # #             review_text = review.div.div.text.strip() if review else 'No review'

# # # # #             all_reviews.append({
# # # # #                 'URL': link,
# # # # #                 'Index': index,
# # # # #                 'Rating': start_rating_text,
# # # # #                 'Time and Place': time_and_place_text,
# # # # #                 'Review': review_text
# # # # #             })
# # # # #             print('Review Number:', index)
# # # # #             print('Rating:', start_rating_text)
# # # # #             print('Time and Place:', time_and_place_text)
# # # # #             print('Review:', review_text)
# # # # #             print()
    
# # # # #     elif "meesho.com" in link:
# # # # #         for index, review_section in enumerate(soup.find_all('div', {'class': 'sc-bqWxrE hupGZf RatingReviewDrawer__StyledCard-sc-y5ksev-1 eyMVSu RatingReviewDrawer__StyledCard-sc-y5ksev-1 eyMVSu'}), start=1):
# # # # #             start_rating = review_section.find('span', {'class': 'sc-iJnaPW fGVEwV'})
# # # # #             start_rating_text = start_rating.text.strip() if start_rating else 'No rating'

# # # # #             time_and_place = review_section.find('span', {'class': 'sc-eDvSVe XndEO'})
# # # # #             time_and_place_text = time_and_place.text.strip() if time_and_place else 'No date'

# # # # #             review = review_section.find('p', {'class': 'sc-eDvSVe gUjMRV Comment__CommentText-sc-1ju5q0e-3 cfdxfJ Comment__CommentText-sc-1ju5q0e-3 cfdxfJ'})
# # # # #             review_text = review.text.strip() if review else 'No review'

# # # # #             all_reviews.append({
# # # # #                 'URL': link,
# # # # #                 'Index': index,
# # # # #                 'Rating': start_rating_text,
# # # # #                 'Time and Place': time_and_place_text,
# # # # #                 'Review': review_text
# # # # #             })
# # # # #             print('Review Number:', index)
# # # # #             print('Rating:', start_rating_text)
# # # # #             print('Time and Place:', time_and_place_text)
# # # # #             print('Review:', review_text)
# # # # #             print()
    
# # # # #     elif "makemytrip.com" in link:
# # # # #         for index, review_section in enumerate(soup.find_all('div', {'class': 'userRvs '}), start=1):
# # # # #             start_rating = review_section.find('span', {'class': 'userRvs__rtng'})
# # # # #             start_rating_text = start_rating.text.strip() if start_rating else 'No rating'

# # # # #             time_and_place = review_section.find('p', {'class': 'userRvs__rvdtlPoints'})
# # # # #             time_and_place_text = time_and_place.text.strip() if time_and_place else 'No date'

# # # # #             review = review_section.find('p', {'class': 'font14 lineHight20'})
# # # # #             review_text = review.text.strip() if review else 'No review'

# # # # #             all_reviews.append({
# # # # #                 'URL': link,
# # # # #                 'Index': index,
# # # # #                 'Rating': start_rating_text,
# # # # #                 'Time and Place': time_and_place_text,
# # # # #                 'Review': review_text
# # # # #             })
# # # # #             print('Review Number:', index)
# # # # #             print('Rating:', start_rating_text)
# # # # #             print('Time and Place:', time_and_place_text)
# # # # #             print('Review:', review_text)
# # # # #             print()

# # # # #     # Implement rate limiting
# # # # #     time.sleep(random.uniform(1, 3))

# # # # # # Convert all_reviews list to a Pandas DataFrame
# # # # # df = pd.DataFrame(all_reviews)

# # # # # # Write DataFrame to Excel file
# # # # # excel_file_path = 'C:\\Users\\chaub\\python files project\\Project1\\reviews.xlsx'
# # # # # df.to_excel(excel_file_path, index=False)

# # # # # print(f'Excel file saved at: {excel_file_path}')

# # # # import requests
# # # # from bs4 import BeautifulSoup
# # # # from oauth2client.service_account import ServiceAccountCredentials
# # # # import gspread
# # # # from datetime import date

# # # # def html_code(url):
# # # #     headers = {
# # # #         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
# # # #     response = requests.get(url, headers=headers)
# # # #     soup = BeautifulSoup(response.content, "html.parser")
# # # #     return soup

# # # # def cus_rev(soup):
# # # #     reviews = []
# # # #     review_blocks = soup.find_all('div', {'class': '_27M-vq'})
# # # #     for block in review_blocks:
# # # #         rating_elem = block.find('div', {'class': '_3LWZlK'})
# # # #         review_elem = block.find('p', {'class': '_2-N8zT'})
# # # #         sum_elem = block.find('div', {'class': 't-ZTKy'})
# # # #         name_elem = block.find_all('p', {'class': '_2sc7ZR'})[0]
# # # #         date_elem = block.find_all('p', {'class': '_2sc7ZR'})[1]
# # # #         location_elem = block.find('p', {'class': '_2mcZGG'})
        
# # # #         if rating_elem and review_elem and name_elem and date_elem:
# # # #             review = {
# # # #                 'Rating': rating_elem.text,
# # # #                 'Review': review_elem.text,
# # # #                 'Name': name_elem.text.strip(),
# # # #                 'Date': date_elem.text.strip(),
# # # #                 'Review Description': sum_elem.text.strip(),
# # # #                 'Location': location_elem.text
# # # #             }
# # # #             reviews.append(review)
# # # #     return reviews

# # # # # URL of the page to scrape
# # # # url = "https://www.flipkart.com/sony-zv-e10l-mirrorless-camera-body-1650-mm-power-zoom-lens-vlog/product-reviews/itmed07cbb694444?pid=DLLG6G8U8P2NGEHG&lid=LSTDLLG6G8U8P2NGEHGGVZNLB&marketplace=FLIPKART"

# # # # reviews = []
# # # # page = 1

# # # # while True:
# # # #     page_url = url + "&page=" + str(page)
# # # #     print(page, "st page is scraping")
# # # #     soup = html_code(page_url)
# # # #     page_reviews = cus_rev(soup)
# # # #     if not page_reviews:
# # # #         break
# # # #     reviews.extend(page_reviews)
# # # #     page += 1


# # # # print(reviews)
# # # # # Define the scope and credentials for Google Sheets API
# # # # scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
# # # # credentials = ServiceAccountCredentials.from_json_keyfile_name(r'C:\Users\faroo\Downloads\youtube0011-391306-e2aaaf87f3f1.json', scope)

# # # # # Authenticate and access the Google Sheets API
# # # # client = gspread.authorize(credentials)

# # # # # Open the existing Google Sheets spreadsheet
# # # # spreadsheet = client.open_by_url('https://docs.google.com/spreadsheets/d/14S7YUe1x24jqoFwjQkej6lh7zJrHMr6ImJ8eDErS3PU/edit#gid=0')

# # # # # Set the sheet name as the current date
# # # # today = date.today()
# # # # new_sheet_name = today.strftime("%d-%m-%Y")

# # # # # Create a new sheet
# # # # new_worksheet = spreadsheet.add_worksheet(title=new_sheet_name, rows="100", cols="20")

# # # # # Select the new sheet
# # # # sheet = spreadsheet.worksheet(new_sheet_name)

# # # # # Create a new list with the header row included
# # # # header_row = ['Rating', 'Review', 'Name', 'Date', 'Review Description', 'Location']
# # # # data_list = [header_row] + [[review[col] for col in header_row] for review in reviews]

# # # # # Clear the existing values in the sheet
# # # # sheet.clear()

# # # # # Append the data list to the Google Sheets
# # # # sheet.append_rows(data_list)

# # # # print("Reviews saved to Google Sheets.")from selenium import webdriver
# # # from selenium.webdriver.chrome.service import Service
# # # from selenium.webdriver.chrome.options import Options

# # # def fetch_url_with_selenium(url):
# # #     options = Options()
# # #     options.add_argument("--proxy-server=http://my-proxy.com")
# # #     options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36")
# # #     options.add_argument("--window-size=1920,1200")
# # #     options.add_argument("--disable-gpu")
# # #     options.add_argument("--no-sandbox")
# # #     options.add_argument("--disable-features=IsolateOrigins,site-per-process")
# # #     options.add_argument("--blink-settings=imagesEnabled=true")

# # #     service = Service(executable_path='C:/Users/chaub/python files project/venv/chromedriver.exe')
    
# # #     driver = webdriver.Chrome(service=service, options=options)
# # #     driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
# # #     driver.get(url)
    
# # #     try:
# # #         WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body")))
# # #         page_source = driver.page_source
# # #     finally:
# # #         driver.quit()

# # #     return page_source
# # from selenium import webdriver
# # from selenium.webdriver.chrome.service import Service as ChromeService
# # from selenium.webdriver.chrome.options import Options
# # from selenium.webdriver.common.by import By
# # from webdriver_manager.chrome import ChromeDriverManager

# # def fetch_url_with_selenium(url):
# #     options = Options()
# #     options.add_argument('--headless')  # Run Chrome in headless mode.
# #     options.add_argument('--no-sandbox')
# #     options.add_argument('--disable-dev-shm-usage')

# #     # Automatically download and use the correct ChromeDriver
# #     service = ChromeService(executable_path=ChromeDriverManager().install())

# #     driver = webdriver.Chrome(service=service, options=options)
# #     driver.get(url)

# #     # Optionally wait for the page to load completely
# #     driver.implicitly_wait(10)  # Wait up to 10 seconds for elements to become available

# #     # Get the page source
# #     page_source = driver.page_source

# #     # Close the browser
# #     driver.quit()
    
# #     return page_source

# # # Example usage
# # url = "https://www.flipkart.com/product-reviews-page-url"  # Replace with the actual URL
# # response_text = fetch_url_with_selenium(url)
# # print(response_text)
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# import time

# def fetch_url_with_selenium(url):
#     options = Options()
#     options.add_argument('--headless')  # Run Chrome in headless mode
#     options.add_argument('--no-sandbox')
#     options.add_argument('--disable-dev-shm-usage')
#     options.add_argument('--disable-blink-features=AutomationControlled')  # Disable automation control
#     options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')  # User agent

#     # Automatically download and use the correct ChromeDriver
#     service = ChromeService(executable_path=ChromeDriverManager().install())

#     driver = webdriver.Chrome(service=service, options=options)
#     driver.get(url)

#     # Optionally wait for the page to load completely
#     driver.implicitly_wait(10)  # Wait up to 10 seconds for elements to become available

#     # Scroll to the bottom to load dynamic content
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(3)  # Wait for content to load

#     # Find and click the "Read all reviews" button if it exists
#     try:
#         read_all_reviews_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Read all reviews')]")
#         read_all_reviews_button.click()
#         time.sleep(3)  # Wait for the reviews page to load
#     except Exception as e:
#         print("Could not find the 'Read all reviews' button. Proceeding with available content.")

#     # Get the page source
#     page_source = driver.page_source

#     # Close the browser
#     driver.quit()
    
#     return page_source

# # Example usage
# url = "https://www.flipkart.com/flipkart-supermart-select-sugar/product-reviews/itmfy2jxm4h87ptd?pid=SUGFY2JXQQKRYFBP"
# response_text = fetch_url_with_selenium(url)
# print(response_text)
import requests
from bs4 import BeautifulSoup

# Define the URL of the Flipkart product reviews page
url = 'https://www.flipkart.com/flipkart-supermart-select-sugar/product-reviews/itmfy2jxm4h87ptd?pid=SUGFY2JXQQKRYFBP'

# Make a request to the URL
response = requests.get(url)
response.raise_for_status()  # Check that the request was successful

# Parse the page content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all review containers
review_containers = soup.find_all('div', class_='col _2wzgFH _1QgsS5')

# Extract data from each review container
reviews = []
for container in review_containers:
    # Extract rating
    rating_tag = container.find('div', class_='row')
    rating = rating_tag.find('div', class_='Rza2QY').text if rating_tag else 'N/A'
    
    # Extract time and place
    time_and_place_tag = container.find('p', class_='_2sc7ZR _2V5EHH')
    time_and_place = time_and_place_tag.text if time_and_place_tag else 'N/A'
    
    # Extract review text
    review_tag = container.find('div', class_='t-ZTKy')
    review = review_tag.div.text if review_tag else 'N/A'
    
    # Append the extracted data to the reviews list
    reviews.append({
        'Rating': rating,
        'Time and Place': time_and_place,
        'Review': review
    })

# Print the extracted reviews
for review in reviews:
    print('Rating:', review['Rating'])
    print('Time and Place:', review['Time and Place'])
    print('Review:', review['Review'])
    print('-' * 40)
