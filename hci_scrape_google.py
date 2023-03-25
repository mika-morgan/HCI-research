import json

#Create the output file to write the comments, scores, and subreddits to
f1 = open("google_codespark.txt", 'w', encoding='utf-8')

from google_play_scraper import Sort, reviews

result, continuation_token = reviews(
    'org.codespark.thefoos',
    #count=3, # defaults to 100
)

# If you pass `continuation_token` as an argument to the reviews function at this point,
# it will crawl the items after 3 review items.

result, _ = reviews(
    'org.codespark.thefoos',
    continuation_token=continuation_token # defaults to None(load from the beginning)
)

for review in result:
    f1.write(json.dumps(review, default=str))
    f1.write('\n')
    f1.write('\n')