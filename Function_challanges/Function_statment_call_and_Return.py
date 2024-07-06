# from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()
from db.mongo_db import create_connection, insert_many, insert_one
from scrapers import nykaa_scraper, pepejeans_scraper, Levis_scraper, ajio_scraper, tata_cliq_scraper, forever21,pull_and_bear
import json
import schedule
import time
import os
from repositories.scraping_session import ScrapeSessionBuilder, add_scraping_session, mark_job_completed, mark_session_completed
import uuid

# URL pattern of the page to scrape
# List of dictionaries containing URLs, scraper functions, and store functions
NUMBER_PRODUCTS_TO_SCRAPE = 100
jobs = [
   {
       "job_id":str(uuid.uuid4()),
       "entity_name":'men-shirts',
       "max_count":NUMBER_PRODUCTS_TO_SCRAPE,
       "url": "https://levi.in/collections/men-shirts",
       "scrape": Levis_scraper.scrape_product_details,
       "store": insert_many,
       "collection":create_connection(collection="ScrapedProducts"),
   }
   ,
   {
       "job_id":str(uuid.uuid4()),
       "entity_name":'casual-shirt',
       "max_count":NUMBER_PRODUCTS_TO_SCRAPE,
       "url": "https://www.nykaafashion.com/men/topwear/casual-shirts/c/6826?root=nav_3&ptype=listing%2Cmen%2Ctopwear%2Ccasual-shirts%2C5%2Ccasual-shirts",
       "scrape": nykaa_scraper.scrape_products,
       "store": insert_many,
       "collection":create_connection(collection="ScrapedProducts"),
   }
   ,
   {
       "job_id":str(uuid.uuid4()),
       "entity_name":'shirts',
       "max_count":NUMBER_PRODUCTS_TO_SCRAPE,
       "url": "https://www.pepejeans.in/men/clothing/shirts",
       "scrape": pepejeans_scraper.scrape_pepejeans_products,
       "store": insert_many,
       "collection":create_connection(collection="ScrapedProducts"),
   }
   ,
   {
       "job_id":str(uuid.uuid4()),
       "entity_name":'men-shirts',
       "max_count":NUMBER_PRODUCTS_TO_SCRAPE,
       "url": "https://www.ajio.com/men-shirts/c/830216013",
       "scrape": ajio_scraper.scrape_product_details,
       "store": insert_many,
       "collection":create_connection(collection="ScrapedProducts"),
   },
   {
       "job_id":str(uuid.uuid4()),
       "entity_name":'men-shirts',
       "max_count":NUMBER_PRODUCTS_TO_SCRAPE,
       "url": "https://forever21.abfrl.in/c/men-checked-shirts",
       "scrape": forever21.scrape_forever21_products,
       "store": insert_many,
       "collection":create_connection(collection="ScrapedProducts"),
   },
   {
       "job_id":str(uuid.uuid4()),
       "entity_name":'men-shirts',
       "max_count":NUMBER_PRODUCTS_TO_SCRAPE,
       "url": "https://www.pullandbear.com/es/hombre/ropa/camisetas-n6323",
       "scrape": pull_and_bear.scrape_pull_and_bear_products,
       "store": insert_many,
       "collection":create_connection(collection="ScrapedProducts"),
   }
   # ,
   # {
   #     "job_id":str(uuid.uuid4()),
   #     "entity_name":'men-shirts',
   #     "max_count":NUMBER_PRODUCTS_TO_SCRAPE,
   #     "url": "https://www.tatacliq.com/search/?searchCategory=all&text=shirts%20for%20men",
   #     "scrape": tata_cliq_scraper.scrape_product_details,
   #     "store": insert_many,
   #     "collection":create_connection(collection="ScrapedProducts"),
   # }
   # Add more tasks as needed
]


def job1():
   for i in range(1, 10):
       print(f"{i} cron ki testing kr rha hoon bhai!")
      

def job():
   print("job kr rah hoon bhai!")
   builder = ScrapeSessionBuilder()
    
   for job in jobs:
    builder.add_job({
        "job_id": job["job_id"],
        "entity_name": job["entity_name"],
        "max_count": job["max_count"],
        "url": job["url"],
    })
   scraping_session = builder.build();

#    print(f"{json.dumps(scraping_session,indent=4)}")
   session_ki_db_id = add_scraping_session(scraping_session_data=scraping_session)
   scrape_Session_id = scraping_session["label"]
   scraping_session["_id"] = session_ki_db_id
   
   for scraping_job in jobs:
        if scraping_job["collection"] is not None:
           data = scraping_job["scrape"](url=scraping_job["url"], max_count=scraping_job["max_count"],job_id=scraping_job.get("job_id"))
           for _ in data:
            _['scrape_session_id'] = scrape_Session_id
           print(f"({scraping_job["job_id"]})[{data[0]["source"]["website_name"] if len(data)>0 else ""}-{scraping_job["entity_name"]}]: {json.dumps(len(data), indent=4)}")
           
           if len(data) > 0:
            scraping_job["store"](collection=scraping_job["collection"], data=data);
           
           if len(data) == scraping_job["max_count"]:
            result = mark_job_completed(scrape_session_id=session_ki_db_id, job_id=scraping_job["job_id"])
   
   mark_session_completed(scrape_session_id=session_ki_db_id)


# Main function
def main():

    SCRAPE_SCHEDULE = os.environ.get('SCRAPE_SCHEDULE', '10:30')
    SCRAPE_SCHEDULE1 = os.environ.get('SCRAPE_SCHEDULE1', 30)
    print(f"{SCRAPE_SCHEDULE} == {SCRAPE_SCHEDULE1}")

    schedule.every().day.at(SCRAPE_SCHEDULE).do(job)
    
    # schedule.every(2).seconds.do(job)
    schedule.every(int(SCRAPE_SCHEDULE1)).seconds.do(job1)

    while True:
        schedule.run_pending()
        time.sleep(1)


