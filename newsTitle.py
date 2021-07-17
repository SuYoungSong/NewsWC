import requests
from bs4 import BeautifulSoup

# [0]society [1]politics [2]economin [3]culture [4]sport [5]digital
def newsTitleCollection(type, pageNumber):
    category = [ "society", "politics", "economic", "culture", "sport", "digital"]
    daumNewsUrl = "https://news.daum.net/breakingnews/" + category[type] + "?page="
    newsTitlePrecleaning = []

    # category[tyoe]유형의 기사를 pageNumber페이지 까지 뉴스 제목 크롤링
    for num in range(1, pageNumber+1 ):
        req = requests.get( daumNewsUrl + str(num))
        soup = BeautifulSoup(req.text, 'html.parser')

        newsTitle = soup.select("#mArticle > div.box_etc > ul > li > div > strong > a")

        for i in range(len(newsTitle)):
            newsTitlePrecleaning.append(newsTitle[i].text) 


    print(newsTitlePrecleaning)