import json
import pandas as pd

temp_row = {}

#Create output files
l1 = open("google_codespark_list_1_star.txt", 'w', encoding='utf-8')
l2 = open("google_codespark_list_2_star.txt", 'w', encoding='utf-8')
l3 = open("google_codespark_list_3_star.txt", 'w', encoding='utf-8')
l4 = open("google_codespark_list_4_star.txt", 'w', encoding='utf-8')
l5 = open("google_codespark_list_5_star.txt", 'w', encoding='utf-8')

#Open the text file
print("Started reading JSON input file")
with pd.read_json("google_codespark.txt", lines=True, chunksize = 1) as f:

    for chunk in f:

        #Iterate through each row in 1,000 row chunks
        for row in chunk.itertuples():
            temp_row['star_rating']   = str(row.score)
            temp_row['review']        = row.content
            temp_row['date']          = str(row.at)

            if temp_row['star_rating'] == '1':
                l1.write(json.dumps(temp_row))
                l1.write('\n')
            
            elif temp_row['star_rating'] == '2':
                l2.write(json.dumps(temp_row))
                l2.write('\n')

            elif temp_row['star_rating'] == '3':
                l3.write(json.dumps(temp_row))
                l3.write('\n')

            elif temp_row['star_rating'] == '4':
                l4.write(json.dumps(temp_row))
                l4.write('\n')

            elif temp_row['star_rating'] == '5':
                l5.write(json.dumps(temp_row))
                l5.write('\n')