import csv

#내가 이 파일은 읽고 f 라고 부르겠다. 
with open('lunch.csv', 'r', encoding='utf-8') as f:
    items = csv.reader(f)
    for item in items:
        print(item)