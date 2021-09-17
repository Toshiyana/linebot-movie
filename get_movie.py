import time
import urllib.request
from bs4 import BeautifulSoup

# サーバにアクセス毎にプログラムが停止する時間（秒）
DELTA = 3

# htmlを取得する関数
def get_html(url):
    html = urllib.request.urlopen(url).read()
    time.sleep(DELTA)
    return html

# 映画情報（ランキング、映画名、評価、公開日）を返す関数
def get_movies():
    url = 'https://eiga.com/ranking/'
    html = get_html(url)

    # BeautifulSoup
    soup = BeautifulSoup(html, features='lxml')
    # urlタグのBeautifulSoupインスタンスを取得
    info = soup.find('table', {'class': 'ranking-table'})
    info = soup.find('tbody')
    # 映画名、評価、公開日のリスト
    names = []
    reviews = []
    dates = []

    for group in info.find_all('tr'): # find_all: 合致する全てのタグのインスタンスをreturn

        name = group.find('h2', {'class': 'title'})
        date = group.find('small', {'class': 'time'})

        # reviewのvalの値はreviewによって異なる。OR検索し、リストで返す。
        review = group.find_all('p', class_=[
            'rating-star small val10'
            'rating-star small val15'
            'rating-star small val20',
            'rating-star small val25',
            'rating-star small val30',
            'rating-star small val35',
            'rating-star small val40',
            'rating-star small val45',
            'rating-star small val50'])

        name = name.find('a').get_text()
        names.append(name)

        review = review[0].get_text()
        reviews.append(review)

        date = date.get_text()
        dates.append(date)

    return 0


if __name__ == '__main__':
    # print(get_movies())
    get_movies()