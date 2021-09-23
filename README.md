# linebot-movie
## Implemetation in Local Environment
1. set token (not including .zshrc in github)
```
source .zshrc
```

2. execute sheduler.py by heroku scheduler
```
python sheduler.py
```

sheduler.pyをherokuで定期実行することで、映画のアクセスランキングを配信。

main.py: メッセージを送信した時に、映画情報を返す。

## demo
<img src="https://user-images.githubusercontent.com/58250083/134469328-aa1ab56d-0eae-41df-ad67-5e2f9c2512ec.jpg" width="50%">