
def send_to_discord(content: str, url: str = None):
    if not url:
        raise ValueError("DISCORD_urlが.envに設定されていません。")

    data = {
        "content": content
    }

    response = requests.post(url, json=data)
    if response.status_code != 204:
        print("送信失敗:", response.status_code, response.text)
    else:
        print("✅ Discordに送信しました")



import requests
import os
import dotenv
dotenv.load_dotenv()
DISCORD_URL = os.getenv("DISCORD_WEBHOOK_URL")
if __name__ == "__main__":
    # テスト用のメッセージを送信
    test_message = "これはテストメッセージです。"
    send_to_discord(test_message, DISCORD_URL)
