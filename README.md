# linebot-movie
## Implemetation in Local Environment
1. set token (not including .zshrc in github)
```
source .zshrc
```

2. execution sheduler.py
python sheduler.py

sheduler.pyをherokuで定期実行することで、映画のアクセスランキングを配信。
（映画情報は、映画.comからスクレイピングすることで取得。）