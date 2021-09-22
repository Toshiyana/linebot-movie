from get_movie import get_movies

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
# linebot.modelsから処理したいイベントをimport
from linebot.models import (
    MessageEvent, TextMessage, TemplateSendMessage, TextSendMessage, CarouselTemplate, CarouselColumn
)
import os

# Flaskクラスのインスタンスを生成
## __name__: 自動的に定義される変数で、現在のファイルのモジュール名が入る。
## ファイルをスクリプトとして実行した場合、__name__ は __main__ となる。
app = Flask(__name__)

# 環境変数取得
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

# インスタンス生成
line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

def push_message():
    week, movie_info = get_movies()

    name = movie_info[0]
    review = movie_info[1]
    date = movie_info[2]
    img = movie_info[3]
    url = movie_info[4]

    notes = [
        CarouselColumn(
            thumbnail_image_url = img[0],
            title = "1位：" + name[0],
            text = "評価：" + review[0] + "\n" + date[0],
            actions = [{"type": "uri", "label": "詳しく見る", "uri": url[0]}]),
        CarouselColumn(
            thumbnail_image_url = img[1],
            title = "2位：" + name[1],
            text = "評価：" + review[1] + "\n" + date[1],
            actions = [{"type": "uri", "label": "詳しく見る", "uri": url[1]}]),
        CarouselColumn(
            thumbnail_image_url = img[2],
            title = "3位：" + name[2],
            text = "評価：" + review[2] + "\n" + date[2],
            actions = [{"type": "uri", "label": "詳しく見る", "uri": url[2]}]),
        CarouselColumn(
            thumbnail_image_url = img[3],
            title = "4位：" + name[3],
            text = "評価：" + review[3] + "\n" + date[3],
            actions = [{"type": "uri", "label": "詳しく見る", "uri": url[3]}]),
        CarouselColumn(
            thumbnail_image_url = img[4],
            title = "5位：" + name[4],
            text = "評価：" + review[4] + "\n" + date[4],
            actions = [{"type": "uri", "label": "詳しく見る", "uri": url[4]}]),
        CarouselColumn(
            thumbnail_image_url = img[5],
            title = "6位：" + name[5],
            text = "評価：" + review[5] + "\n" + date[5],
            actions = [{"type": "uri", "label": "詳しく見る", "uri": url[5]}]),
        CarouselColumn(
            thumbnail_image_url = img[6],
            title = "7位：" + name[6],
            text = "評価：" + review[6] + "\n" + date[6],
            actions = [{"type": "uri", "label": "詳しく見る", "uri": url[6]}]),
        CarouselColumn(
            thumbnail_image_url = img[7],
            title = "8位：" + name[7],
            text = "評価：" + review[7] + "\n" + date[7],
            actions = [{"type": "uri", "label": "詳しく見る", "uri": url[7]}]),
        CarouselColumn(
            thumbnail_image_url = img[8],
            title = "9位：" + name[8],
            text = "評価：" + review[8] + "\n" + date[8],
            actions = [{"type": "uri", "label": "詳しく見る", "uri": url[8]}]),
        CarouselColumn(
            thumbnail_image_url = img[9],
            title = "10位：" + name[9],
            text = "評価：" + review[9] + "\n" + date[9],
            actions = [{"type": "uri", "label": "詳しく見る", "uri": url[9]}]),
    ]

    messages = TemplateSendMessage(
        alt_text = '映画情報',
        template = CarouselTemplate(columns=notes),
    )

    line_bot_api.broadcast([
        TextSendMessage(text=week),
        messages
    ])


if __name__ == "__main__":
    push_message()