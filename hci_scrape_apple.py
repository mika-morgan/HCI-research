from app_store_scraper import AppStore
import json

#Create the output file to write the comments, scores, and subreddits to
f1 = open("apple_codespark.txt", 'w', encoding='utf-8')

minecraft = AppStore(country="us", app_name="codespark")
minecraft.review()

for review in minecraft.reviews:
    f1.write(json.dumps(review, default=str))
    f1.write('\n')
    f1.write('\n')
print(minecraft.reviews_count)