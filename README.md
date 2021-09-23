# linebot-movie
## Implemetation in Local Environment
1. set token (not including .zshrc in github)
```
source .zshrc
```

2. execute sheduler.py by heroku scheduler
python sheduler.py

sheduler.pyをherokuで定期実行することで、映画のアクセスランキングを配信。
（映画情報は、映画.comからスクレイピングすることで取得。）

main.py: メッセージを送信した時に、映画情報を返す。