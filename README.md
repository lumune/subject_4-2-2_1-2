# Google ドキュメント API - 課題1-2

## 必要なパッケージのインストール

```bash
pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

または、requirements.txt を使用する場合：

```bash
pip install -r requirements.txt
```

## 使い方

1. `credentials.json` を Google Cloud Console で取得し、このディレクトリに配置してください
2. Google Cloud Console で Google Docs API を有効化してください
3. 以下のコマンドでプログラムを実行します：

```bash
python create_document.py
```

4. 初回実行時、ブラウザが開き OAuth2 認証を行います
5. 認証後、認証情報は `token.pickle` に保存され、次回以降は再利用されます
