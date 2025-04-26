import requests
import os
import dotenv
import random
dotenv.load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv("DATABASE_ID")

url = f'https://api.notion.com/v1/databases/{DATABASE_ID}/query'

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json"
}

def fetch_word(lang: str):
    response = requests.post(url, headers=headers)
    if response.status_code != 200:
        print("エラー:", response.status_code, response.text)
        return {}

    data = response.json()
    words = {}

    for result in data["results"]:
        properties = result["properties"]
        if lang in properties and properties[lang]["rich_text"]:
            words[properties["名前"]["title"][0]["plain_text"]] = properties[lang]["rich_text"][0]["plain_text"]

    # ランダムに10個選択
    if len(words) > 10:
        words = dict(random.sample(words.items(), 10))

    return words

if __name__ == "__main__":
    # テスト用
    spanish_words = fetch_word("Spanish")
    print("Spanish Words:", spanish_words)
    korean_words = fetch_word("Korean")
    print("Korean Words:", korean_words)

    print("テスト完了")
