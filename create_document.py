"""
Google Docs API を使用してOAuth2認証を行い、
タイトル「課題1-2」の新しいGoogleドキュメントを作成し、
本文の先頭にテキストを挿入するプログラム
"""

import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import pickle

# Google Docs API のスコープ
SCOPES = ['https://www.googleapis.com/auth/documents', 'https://www.googleapis.com/auth/drive.file']

# credentials.json のパス（同一ディレクトリ）
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CREDENTIALS_PATH = os.path.join(SCRIPT_DIR, 'credentials.json')
TOKEN_PATH = os.path.join(SCRIPT_DIR, 'token.pickle')


def get_credentials():
    """
    OAuth2認証を行い、資格情報を取得する
    token.pickle があれば再利用し、なければ credentials.json から新規認証
    """
    creds = None
    if os.path.exists(TOKEN_PATH):
        with open(TOKEN_PATH, 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_PATH, 'wb') as token:
            pickle.dump(creds, token)

    return creds


def create_and_populate_document():
    """
    新しいGoogleドキュメントを作成し、本文の先頭にテキストを挿入する
    """
    creds = get_credentials()

    try:
        # Google Docs API クライアントを構築
        docs_service = build('docs', 'v1', credentials=creds)

        # 新しいドキュメントを作成（タイトル: 課題1-2）
        document = docs_service.documents().create(
            body={'title': '課題1-2'}
        ).execute()

        document_id = document.get('documentId')
        print(f'ドキュメントを作成しました: {document.get("title")}')
        print(f'ドキュメントID: {document_id}')
        print(f'URL: https://docs.google.com/document/d/{document_id}/edit')

        # 挿入するテキスト
        insert_text = '名前：もなか\n猫種：マンチカン\n'

        # 本文の先頭（index 1）にテキストを挿入
        requests = [
            {
                'insertText': {
                    'location': {'index': 1},
                    'text': insert_text
                }
            }
        ]

        docs_service.documents().batchUpdate(
            documentId=document_id,
            body={'requests': requests}
        ).execute()

        print('テキストを挿入しました。')

    except HttpError as error:
        print(f'エラーが発生しました: {error}')
        raise


if __name__ == '__main__':
    create_and_populate_document()
