import discord
import slack_sdk
import datetime

class Discord():
    def __init__(self, slack_token, slack_channel):
        # 初期化
        intents = discord.Intents.default()
        intents.message_content = True
        self.bot = discord.Client(intents=intents)
        self.slack_client = slack_sdk.WebClient(token=slack_token)
        slack_channel = slack_channel

        # ボイチャ通知
        @self.bot.event
        async def on_voice_state_update(member, before, after):
            if before.channel != after.channel:
                time = datetime.datetime.now().strftime("%Y年%m月%d日 %H:%M:%S")
                if before.channel is None:
                    msg = f"{time}{member.nick}が{after.channel.name}に参加しました"
                    # DBに記述
                else:
                    msg = f"{time}{member.nick}が{before.channel.name}から退出しました"
                    # DBに記述
                await self.send_msg_to_slack(msg, slack_channel)
                
    # Slackに送る関数を定義
    async def send_msg_to_slack(self, message, channel):
        response = self.slack_client.chat_postMessage(channel=channel, text=message)
        return response
