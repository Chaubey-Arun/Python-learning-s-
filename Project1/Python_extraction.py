# import json
# import requests 
# from bs4 import BeautifulSoup
# import pandas as pd 


# with open('C:\\Users\\chaub\\python files project\\Project1\\HandsonProject1.json', 'r') as file:
#     web_url = json.load(file)


# links = web_url['url']


# header = {
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
# }

# for link in links:
#     print(f"Scraping reviews from: {link}\n")

#     reviews = []

  
#     response = requests.get(link, headers=header)
#     response_text = response.text

#     soup = BeautifulSoup(response_text, 'html.parser')

#     for index, review_section in enumerate(soup.find_all('div', {'data-hook': 'review'}), start=1):
      
#         start_rating = review_section.find('i', {'data-hook': 'review-star-rating'})
#         start_rating_text = start_rating.text.strip() 

#         time_and_place = review_section.find('span', {'data-hook': 'review-date'})
#         time_and_place_text = time_and_place.text.strip()

#         review = review_section.find('span', {'data-hook': 'review-body'})
#         review_text = review.text.strip() 

    
#         reviews.append({
#             'index': index,
#             'rating': start_rating_text,
#             'time_and_place': time_and_place_text,
#             'review': review_text
#         })


#         print('Review Number:', index)
#         print('Rating:', start_rating_text)
#         print('Time and Place:', time_and_place_text)
#         print('Review:', review_text)
#         print()

# print(f'Here are the links: {links}')

# df = pd.DataFrame(review)
# print(df)
import json
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Load URLs from JSON file
with open('C:\\Users\\chaub\\python files project\\Project1\\HandsonProject1.json', 'r') as file:
    web_urls = json.load(file)['url']

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}

# List to store all reviews from all URLs
all_reviews = []

# Iterate through each URL and scrape reviews
for url in web_urls:
    print(f'Scraping reviews from: {url}\n')
    reviews = []

    response = requests.get(url, headers=header)
    response_text = response.text
    soup = BeautifulSoup(response_text, 'html.parser')

    if "amazon.in" in url:
        for index, review_section in enumerate(soup.find_all('div', {'data-hook': 'review'}), start=1):
            start_rating = review_section.find('i', {'data-hook': 'review-star-rating'})
            start_rating_text = start_rating.text.strip() if start_rating else 'No rating'

            time_and_place = review_section.find('span', {'data-hook': 'review-date'})
            time_and_place_text = time_and_place.text.strip() if time_and_place else 'No date'

            review = review_section.find('span', {'data-hook': 'review-body'})
            review_text = review.text.strip() if review else 'No review'

            all_reviews.append({
                'URL': url,
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

    elif "flipkart.com" in url:
        for index, review_section in enumerate(soup.find_all('div', {'class': 'cPHDOP col-12-12'}), start=1):
            start_rating = review_section.find('div', {'class': 'XQDdHH Ga3i8K'})
            start_rating_text = start_rating.text.strip() if start_rating else 'No rating'

            time_and_place = review_section.find('p', {'class': '_2NsDsF'})
            time_and_place_text = time_and_place.text.strip() if time_and_place else 'No date'

            review = review_section.find('div', {'class': 'row'})
            review_text = review.div.div.text.strip() if review else 'No review'

            all_reviews.append({
                'URL': url,
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

    elif "meesho.com" in url:
        for index, review_section in enumerate(soup.find_all('div', {'class': 'sc-bqWxrE hupGZf RatingReviewDrawer__StyledCard-sc-y5ksev-1 eyMVSu RatingReviewDrawer__StyledCard-sc-y5ksev-1 eyMVSu'}), start=1):
            start_rating = review_section.find('span', {'class': 'sc-iJnaPW fGVEwV'})
            start_rating_text = start_rating.text.strip() if start_rating else 'No rating'

            time_and_place = review_section.find('span', {'class': 'sc-eDvSVe XndEO'})
            time_and_place_text = time_and_place.text.strip() if time_and_place else 'No date'

            review = review_section.find('p', {'class': 'sc-eDvSVe gUjMRV Comment__CommentText-sc-1ju5q0e-3 cfdxfJ Comment__CommentText-sc-1ju5q0e-3 cfdxfJ'})
            review_text = review.text.strip() if review else 'No review'

            all_reviews.append({
                'URL': url,
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

    elif "makemytrip.com" in url:
        for index, review_section in enumerate(soup.find_all('div', {'class': 'col-xs-12 reviewUnit'}), start=1):
            start_rating = review_section.find('span', {'class': 'sprite rating_fill'})
            start_rating_text = start_rating.text.strip() if start_rating else 'No rating'

            time_and_place = review_section.find('span', {'class': 'dateAndTime'})
            time_and_place_text = time_and_place.text.strip() if time_and_place else 'No date'

            review = review_section.find('p', {'class': 'userRvs__reviewDescription'})
            review_text = review.text.strip() if review else 'No review'

            all_reviews.append({
                'URL': url,
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

# Convert all_reviews list to DataFrame
df = pd.DataFrame(all_reviews)

# Write DataFrame to CSV file
df.to_csv('reviews_data.csv', index=False)
print('Data saved to reviews_data.csv')

# Display DataFrame
print('\nDataFrame with all reviews:')
print(df)

