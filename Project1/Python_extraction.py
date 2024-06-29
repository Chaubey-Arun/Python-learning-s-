import json
import requests
from bs4 import BeautifulSoup

# Load URLs from the JSON file
with open('C:\\Users\\chaub\\python files project\\Project1\\HandsonProject1.json', 'r') as file:
    web_url = json.loads(file.read())

# Extract the list of URLs
urls = web_url['url']

# User-agent header
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
}

# Loop through each URL and scrape reviews
for link in  (urls):
    reviews = []
    response = requests.get(link, headers=header)
    response_text = response.text
    soup = BeautifulSoup(response_text, 'lxml')

    # Iterate over each review section using enumerate
    for index, review_section in enumerate(soup.find_all('div', {'data-hook': 'review'}), start=1):
        # Extract the star rating
        start_rating = review_section.find('i', {'data-hook': 'review-star-rating'})
        start_rating_text = start_rating.text if start_rating else 'No rating'

        # Extract the date and place of the review
        time_and_place = review_section.find('span', {'data-hook': 'review-date'})
        time_and_place_text = time_and_place.text if time_and_place else 'No date'

        # Extract the review text
        review = review_section.find('span', {'data-hook': 'review-body'})
        review_text = review.text.strip() if review else 'No review'

        # Append a dictionary with the extracted information to the reviews list
        reviews.append({ 
          
            'index': index,
            'rating': start_rating_text,
            'time_and_place': time_and_place_text,
            'review': review_text
        })

    # Print all reviews
    for review in reviews:
        print('Review Number :-    ', review['index'])
        print('Rating :-           ', review['rating'])
        print('Time and Place :-   ', review['time_and_place'])
        print('Review :-           ', review['review'])

        
