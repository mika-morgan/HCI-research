import random
input = open("google_scratchjr_list_5_star.txt", 'r', encoding='utf-8')
list = []

for line in input:
    list.append(line)

ten_random = random.choices(list, k= 10)
print(ten_random)