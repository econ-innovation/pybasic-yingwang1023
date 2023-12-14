##1.使用高德API获取985大学地理信息
import requests
import csv
# 读取csv文件
universities = []
with open('university.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        universities.append(row)
# 定义请求URL和参数
url = 'https://restapi.amap.com/v3/geocode/geo'
params = {'key': '45aff143c80be095aa0b05b0bb7b606a', 'address': '', 'city': ''}
# 遍历每个大学，获取地理编码信息
for university in universities:
    address = university['name']
    params['address'] = address
    response = requests.get(url, params=params)
    result = response.json()
    if result['status'] == '1':
        geocode = result['geocodes'][0]
        university['location'] = geocode['location']
        university['formatted_country'] = geocode['formatted_address'].replace(' ', '')
        university['country'] = geocode['country']
        university['province'] = geocode['province']
        university['city'] = geocode['city']
        university['district'] = geocode['district']
        university['street'] = geocode['street']
        university['number'] = geocode['number']
    else:
        print(f"获取{address}的地理编码信息失败：{result['info']}")
# 将结果保存到'university_geocode.csv'文件
header = universities[0].keys()
with open('university_geocode.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=header)
    writer.writeheader()
    writer.writerows(universities)

## 2.拆分google专利文件
import json
with open("./google100.txt", "r") as f:
    with open('./patent_dates.txt', 'a') as fs:
        fs.write("Filing Date|Publication Date|Grant Date|Priority Date\n")
        for pt in f.readlines():
            patent = json.loads(pt)
            filing_date = patent.get("filing_date", "")
            publication_date = patent.get("publication_date", "")
            grant_date = patent.get("grant_date", "")
            priority_date = patent.get("priority_date", "")

            fs.write(f"{filing_date}|{publication_date}|{grant_date}|{priority_date}\n")

#在命令行运行?
import patent_dates
python3 patent_dates google100.txt
