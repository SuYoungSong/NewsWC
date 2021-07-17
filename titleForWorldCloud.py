from newsTitle import newsTitleCollection
import numpy as np
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# [0]society [1]politics [2]economin [3]culture [4]sport [5]digital
# 첫번째 매개변수 : 카테고리 선택(↑), 두번째 매개변수 : 크롤링할 페이지 수
newsTitleTxt = newsTitleCollection(2,10)

font_path = 'C:\Windows\Fonts\malgun.ttf'   # 폰트 적용
 
wc = WordCloud(font_path=font_path, background_color="white")
wc.generate(newsTitleTxt)

plt.figure(figsize=(10,10))     # wordcloud 사이즈 설정
plt.axis("off")                 # 축 숫자 제거
plt.imshow(wc)
plt.show()

