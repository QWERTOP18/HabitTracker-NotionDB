from NotionDB.WordSender import fetch_word
from Discord.webhook import send_to_discord
import os

if __name__ == "__main__":
    # 各言語用のWebhook URLを取得
    spanish_webhook = os.getenv("DISCORD_SPANISH_WEBHOOK")
    korean_webhook = os.getenv("DISCORD_KOREAN_WEBHOOK")

    # SpanishとKoreanのデータを取得
    spanish_words = fetch_word("Spanish")
    korean_words = fetch_word("Korean")

    # Discordに送信
    if not spanish_words and not korean_words:
        if spanish_webhook:
            send_to_discord("⚠️ データが見つかりませんでした。", spanish_webhook)
        if korean_webhook:
            send_to_discord("⚠️ データが見つかりませんでした。", korean_webhook)
    else:
        # Spanishのデータを送信
        if spanish_words and spanish_webhook:
            for key, value in spanish_words.items():
                message = f"- **{key}**: ||{value}||"
                send_to_discord(message, spanish_webhook)

        # Koreanのデータを送信
        if korean_words and korean_webhook:
            for key, value in korean_words.items():
                message = f"- **{key}**: ||{value}||"
                send_to_discord(message, korean_webhook)
