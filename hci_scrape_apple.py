from app_store_scraper import AppStore
import json

#Create the output file to write the comments, scores, and subreddits to
f1 = open("apple_codespark.txt", 'w', encoding='utf-8')

cs = AppStore(country="us", app_name="codespark")
cs.review()

for review in cs.reviews:
    f1.write(json.dumps(review, default=str))
    f1.write('\n')
    f1.write('\n')
print(cs.reviews_count)
