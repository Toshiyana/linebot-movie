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
    images = []
    detailed_urls = []

    for group in info.find_all('tr'): # find_all: 合致する全てのタグのインスタンスをreturn

        name = group.find('h2', {'class': 'title'})
        date = group.find('small', {'class': 'time'})
        img = group.find('img').get(('data-src'))# 画像urlを取得
        url = name.find('a').get(('href'))
        url = "https://eiga.com" + url
        print(url)

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

        images.append(img)

        detailed_urls.append(url)



    movie_info = [names, reviews, dates, images, detailed_urls]

    return movie_info

def get_txt_info(movie_info):
    name = movie_info[0]
    review = movie_info[1]
    date = movie_info[2]

    txt_info = \
    "1.\n" + \
    "タイトル： " + name[0] + "\n" + \
    "評価： " + review[0] + "\n" + \
    date[0] + "\n\n" + \
    "2.\n" + \
    "タイトル： " + name[1] + "\n" + \
    "評価： " + review[1] + "\n" + \
    date[1] + "\n\n" + \
    "3.\n" + \
    "タイトル： " + name[2] + "\n" + \
    "評価： " + review[2] + "\n" + \
    date[2] + "\n\n" + \
    "4.\n" + \
    "タイトル： " + name[3] + "\n" + \
    "評価： " + review[3] + "\n" + \
    date[3] + "\n\n" + \
    "5.\n" + \
    "タイトル： " + name[4] + "\n" + \
    "評価： " + review[4] + "\n" + \
    date[4] + "\n\n" + \
    "6.\n" + \
    "タイトル： " + name[5] + "\n" + \
    "評価： " + review[5] + "\n" + \
    date[5] + "\n\n" + \
    "7.\n" + \
    "タイトル： " + name[6] + "\n" + \
    "評価： " + review[6] + "\n" + \
    date[6] + "\n\n" + \
    "8.\n" + \
    "タイトル： " + name[7] + "\n" + \
    "評価： " + review[7] + "\n" + \
    date[7] + "\n\n" + \
    "9.\n" + \
    "タイトル： " + name[8] + "\n" + \
    "評価： " + review[8] + "\n" + \
    date[8] + "\n\n" + \
    "10.\n" + \
    "タイトル： " + name[9] + "\n" + \
    "評価： " + review[9] + "\n" + \
    date[9]

    return txt_info

if __name__ == '__main__':
    movie_info = get_movies()
    txt_movie = get_txt_info(movie_info)

    # print(txt_movie)