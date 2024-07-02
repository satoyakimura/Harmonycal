import os
from dotenv import load_dotenv
from etc.send import Discord

# Tokenの取得
load_dotenv()
discord_token = os.environ.get("DISCORD_TOKEN")
slack_token = os.environ.get("SLACK_TOKEN")
slack_channel = os.environ.get("SLACK_CHANNEL")


if __name__ == "__main__":
    discord_bot = Discord(slack_token, slack_channel)
    # ボットを実行
    discord_bot.bot.run(discord_token)