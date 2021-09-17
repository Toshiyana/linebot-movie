import os
from flask import Flask, request, abort

from linebot import {
    LineBotApi, WebhookHandler
}
from linebot.exceptions import {
    InvalidSignatureError
}
from linebot.models import {
    MessageEvent, TextMessage, TextSendMessage
}

app = Flask(__name__)

# 環境変数取得
token = os.environ["LINE_CHANNEL_TOKEN"]
secret = os.environ["LINE_CHANNEL_SECRET"]

line_bot_api = LineBotApi(token)
handler = WebhookHandler(secret)

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers["X-Line-Signature"]

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return "OK"

@handler.add(MessageEvent, messagea=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text)
    )

if __name__ == "__main__":
    port = int(os.getenv("PORT", 200))
    app.run(host="0.0.0.0", port=port)