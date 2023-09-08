import requests
from bs4 import BeautifulSoup
import csv

url = "https://movie.douban.com/top250"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
}
response = requests.get(url=url, headers=headers)
print(response.status_code)
soup = BeautifulSoup(response.text, "html.parser")

movies = soup.find_all("div", class_="item")
# print(movies)
data = []
for movie in movies:
    title = movie.find("span", class_="title").text
    # rating = movie.find("span", class_="rating_num").text
    # inq = movie.find("span", class_="inq").text
    bd = (
        movie.find("div", class_="bd")
        .text.replace(" ", "")
        .replace("\n\n\n", "\n")
        .replace("\n\n\n", "\n")
        .split("\n")
    )
    bd = [x for x in bd if x != ""]
    bd = [x for y in bd for x in y.split("   ", 1)]
    data.append([title] + bd)

with open(r"download\movies.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)
    writer.writerow(["电影名", "导演", "主演", "时间/地区/类型", "评分", "评价人数", "一句话评价"])
    writer.writerows(data)

print("数据爬取完成并存储到movies.csv文件中。")

