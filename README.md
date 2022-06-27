# linebot-movie
最新の映画ランキングとレビューを毎週通知してくれるLinebot

## Demo
<img src="https://user-images.githubusercontent.com/58250083/134469328-aa1ab56d-0eae-41df-ad67-5e2f9c2512ec.jpg" width="50%">

## Features
* LineBot
* You can recieve movie information once every Monday and when you follow this bot.

## Requirement
* Python 3.7.12
* Flask 2.0.1
* line-bot-sdk 1.20.0
* beautifulsoup4 4.10.0

## Usage in Local Environment
1. set token (not including .zshrc in github)
```
source .zshrc
```

2. install necessary libraries
```
pip install requirements.txt
```

3. execute sheduler.py by heroku scheduler
```
python sheduler.py
```

sheduler.pyをherokuで定期実行することで、映画のアクセスランキングを配信。

main.py: メッセージを送信した時に、映画情報を返す。
