# import json
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

# with open('C:\\Users\\chaub\\python files project\\Project1\\HandsonProject1.json', 'r') as file:
#     urls = json.load(file)['url']

# headers = {
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
# }


# all_reviews = []


# for url in urls:
#     print(f'Scraping reviews from: {url}\n')
#     reviews = []

#     response = requests.get(url, headers=headers)
#     response.raise_for_status()
#     soup = BeautifulSoup(response.text, 'html.parser')

#     if "amazon.in" in url:
#         for index, review_section in enumerate(soup.find_all('div', {'data-hook': 'review'}), start=1):
#             rating_tag = review_section.find('i', {'data-hook': 'review-star-rating'})
#             rating_text = rating_tag.text.strip() if rating_tag else 'No rating'

#             date_tag = review_section.find('span', {'data-hook': 'review-date'})
#             date_text = date_tag.text.strip() if date_tag else 'No date'

#             review_text_tag = review_section.find('span', {'data-hook': 'review-body'})
#             review_text = review_text_tag.text.strip() if review_text_tag else 'No review'

#             all_reviews.append({
#                 'URL': url,
#                 'Index': index,
#                 'Rating': rating_text,
#                 'Time and Place': date_text,
#                 'Review': review_text
#             })

#             print('Review Number:', index)
#             print('Rating:', rating_text)
#             print('Time and Place:', date_text)
#             print('Review:', review_text)
#             print()
#     elif "makemytrip.com" in url:
        
#         for index, review_section in enumerate(soup.find_all('div', {'class': 'userRvs__item'}), start=1):
#             rating_text = review_section.find('span', {'class': 'userRvs__rtng'}).text
            

#             date_text1 = review_section.find('div', {'class': 'userRvs__rvdtl'})
#             date_text = ''
#             for date_text1 in date_text1 : 
#                 if 'titText' not in date_text1.get('class', []) and 'grayDot' not in date_text1.get('class', []):
#                     date_text = date_text1.text
#                     break
            

#             review_text= review_section.find('p', {'class': 'font14 lineHight20'}).text
            

#             all_reviews.append({
#                         'URL': url,
#                         'Index': index,
#                         'Rating': rating_text,
#                         'Time and Place': date_text,
#                         'Review': review_text
#                     })

#             print('Review Number:', index)
#             print('Rating:', rating_text)
#             print('Time and Place:', date_text)
#             print('Review:', review_text)
#             print()


# df = pd.DataFrame(all_reviews)
# df.to_csv('reviews_data.csv', index=False)
# print('Data saved to reviews_data.csv')
# print('\nDataFrame with all reviews:')
# print(df)
#-------------Below this flipkart link progarm which only Run seprately ------------------------------------------

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.flipkart.com/flipkart-supermart-select-sugar/product-reviews/itmfy2jxm4h87ptd?pid=SUGFY2JXQQKRYFBP'

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.content, 'html.parser')

all_reviews = []

for index, review_section in enumerate(soup.find_all('div', {'class': 'cPHDOP col-12-12'}), start=1):
    rating_tag = review_section.find('div', {'class': 'XQDdHH Ga3i8K'})
    rating_text = rating_tag.text.strip() if rating_tag else 'No rating'

    date_elements = review_section.find_all('p', {'class': '_2NsDsF'})
    time_and_place = None
    for date_element in date_elements:
        if 'AwS1CA' not in date_element.get('class', []):
            time_and_place = date_element.text.strip()
            break
    if not time_and_place:
        time_and_place = 'No date'

    review_text_tag = review_section.find('div', {'class': 'row'})
    if review_text_tag:
        review_text = review_text_tag.text.strip()
    else:
        review_text = 'No review text'

    all_reviews.append({
        'URL': url,
        'Index': index,
        'Rating': rating_text,
        'Time and Place': time_and_place,
        'Review': review_text
    })

    print('Review Number:', index)
    print('Rating:', rating_text)
    print('Time and Place:', time_and_place)
    print('Review:', review_text)
    print()


# new_reviews_df = pd.DataFrame(all_reviews)
# existing_reviews_df = pd.read_csv('reviews_data.csv')
# combined_df = pd.concat([existing_reviews_df, new_reviews_df], ignore_index=True)
# combined_df.to_csv('reviews_data.csv', index=False)
# print('New reviews added to reviews_data.csv')
# print('\nUpdated DataFrame with all reviews:')



# print(combined_df)
