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
    MessageEvent, TextMessage, TextSendMessage,
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
@handler.add(MessageEvent)
def handle_message(event):# event: LineMessagingAPIで定義されるリクエストボディ
    movie_info = get_movies()
    name = movie_info[0]
    review = movie_info[1]
    date = movie_info[2]

    movie_txt = \
    "1.\n" + \
    "タイトル： " + name[0] + "\n" + \
    "評価： " + review[0] + "\n" + \
    "公開日： " + date[0] + "\n\n" + \
    "2.\n" + \
    "タイトル： " + name[1] + "\n" + \
    "評価： " + review[1] + "\n" + \
    "公開日： " + date[1] + "\n\n" + \
    "3.\n" + \
    "タイトル： " + name[2] + "\n" + \
    "評価： " + review[2] + "\n" + \
    "公開日： " + date[2] + "\n\n" + \
    "4.\n" + \
    "タイトル： " + name[3] + "\n" + \
    "評価： " + review[3] + "\n" + \
    "公開日： " + date[3] + "\n\n" + \
    "5.\n" + \
    "タイトル： " + name[4] + "\n" + \
    "評価： " + review[4] + "\n" + \
    "公開日： " + date[4] + "\n\n" + \
    "6.\n" + \
    "タイトル： " + name[5] + "\n" + \
    "評価： " + review[5] + "\n" + \
    "公開日： " + date[5] + "\n\n" + \
    "7.\n" + \
    "タイトル： " + name[6] + "\n" + \
    "評価： " + review[6] + "\n" + \
    "公開日： " + date[6] + "\n\n" + \
    "8.\n" + \
    "タイトル： " + name[7] + "\n" + \
    "評価： " + review[7] + "\n" + \
    "公開日： " + date[7] + "\n\n" + \
    "9.\n" + \
    "タイトル： " + name[8] + "\n" + \
    "評価： " + review[8] + "\n" + \
    "公開日： " + date[8] + "\n\n" + \
    "10.\n" + \
    "タイトル： " + name[9] + "\n" + \
    "評価： " + review[9] + "\n" + \
    "公開日： " + date[9]

    line_bot_api.reply_message(
        event.reply_token,# イベントの応答に用いるトークン
        TextSendMessage(text=movie_txt))
# 多分、event = {MessageEvent, message}になっている

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    # Flaskが持っている開発ようサーバーの起動
    app.run(host="0.0.0.0", port=port)