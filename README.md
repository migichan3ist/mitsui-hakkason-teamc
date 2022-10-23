# セットアップ

## fastapiのインストール
```
pip install fastapi
```

## ロードする

```
uvicorn main:app --reload
```

＊常に上記は実行されている状態で作業する。以下のような表示がコマンドに出てくればよい

```
INFO:     Will watch for changes in these directories: ['C:\\Users\\migic\\Documents\\mitsui2022']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [16076] using statreload
INFO:     Started server process [6800]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

＊実験として、下記URLが立ち上がればOK

URL : http://127.0.0.1:8000

```
{"message":"Hello World"}
```

## database使用するために、下記をインストール

```
pip install sqlalchemy
pip install pysqlite3
```

## 注意点

### 一番最初に必ず以下のURLをブラウザで打ち込む

http://127.0.0.1:8000/hour_table

