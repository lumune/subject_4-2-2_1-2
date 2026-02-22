# Google ドキュメント API - 課題1-2

提出用課題
4-2-2 API連携実践課題
1-2. Google ドキュメント API


Google Docs API 課題1-2
## 📌 概要

Google Docs API を使用し、新しいドキュメントを作成し、
指定したテキストを自動で挿入するプログラムを作成しました。

### 作成されるドキュメント
#### 1. ドキュメント名

課題1-2

#### 2.挿入テキスト

名前：もなか

猫種：マンチカン


## 🚀 実装した機能

1. Google Docs APIを用いた新規ドキュメント作成

2. 作成したドキュメントIDの取得

3. 指定したテキストの自動挿入


## 🛠 使用技術

・Python

・Google Docs API

・Google Drive API

・OAuth 2.0 認証


## 🔑 事前準備
① Google Cloud ConsoleでAPIを有効化

1. プロジェクトを作成

2. Google Docs API を有効化

3. Google Drive API を有効化

4. OAuth クライアントIDを作成

5. credentials.json をダウンロード


## ⚠️ 注意

セキュリティ上の理由から、
credentials.json は本リポジトリには含めていません。

実行する場合は、各自でGoogle Cloud Consoleより取得し、
プロジェクトのルートディレクトリに配置してください。

## ▶ 実行方法

`pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib`

`python create_document.py`

## 実行すると：

・新しいGoogleドキュメントが作成されます

・指定テキストが自動で挿入されます


