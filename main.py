from get_movie import get_movies, get_txt_info

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

# app.route("/"): appに対して / というURLに対応するアクションを登録
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    ## Lineから送られたメッセージかどうかを確認するための著名を取得 =
    ## X-Line-Signatureリクエストヘッダに含まれる著名を検証して、
    ## リクエストがLineプラットフォームから送信されたことを確認
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)# postされたデータをそのまま取得（HTTPリクエストメッセージボディ）
    app.logger.info("Request body: " + body)# ログ処理（記録）

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:# signatureエラー（Lineから送られたメッセージでない場合）
        abort(400)# abort(): flaskの関数で、httpステータスとメッセージを指定可能
        # ステータスコード400: Bad request. クライアント側のエラーにより、サーバ側がリクエストを処理できない時に使用。
    return 'OK'


# handler.add(): 引数にlinebotのリクエストのイベントを指定
@handler.add(MessageEvent, message=TextMessage)
def response_message(event):# event: LineMessagingAPIで定義されるリクエストボディ
    movie_info = get_movies()

    name = movie_info[0]
    review = movie_info[1]
    date = movie_info[2]
    img = movie_info[3]
    url = movie_info[4]


    notes = [
        CarouselColumn(
            thumbnail_image_url = img[0],
            title = name[0],
            text = review[0],
            actions = [{"type": "message", "label": "詳しく見る", "text": url[0]}]),
        CarouselColumn(
            thumbnail_image_url = img[1],
            title = name[1],
            text = review[1],
            actions = [{"type": "message", "label": "詳しく見る", "text": url[1]}]),
        CarouselColumn(
            thumbnail_image_url = img[2],
            title = name[2],
            text = review[2],
            actions = [{"type": "message", "label": "詳しく見る", "text": url[2]}]),
    ]

    messages = TemplateSendMessage(
        alt_text = 'template',
        template = CarouselTemplate(columns=notes),
    )

    line_bot_api.reply_message(
        event.reply_token,# イベントの応答に用いるトークン
        messages=messages)
# 多分、event = {MessageEvent, message}になっている

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    # Flaskが持っている開発ようサーバーの起動
    app.run(host="0.0.0.0", port=port)