import util
from linebot.models import TextSendMessage
from linebot import (
    LineBotApi,
)

class LineBotClient:
    """
    メッセージ送信用クライアント

    Attributes:
        _line_bot_api (LineBotApi): LINE公式の提供するAPI
        _reply_token (str): 受け取ったメッセージのリプライトークンと一致する必要がある.
    """
    def __init__(self, reply_token):
        line_channel_access_token = util.get_access_token()
        self._line_bot_api = LineBotApi(line_channel_access_token)
        self._reply_token = reply_token

    def send_message(self, message_list):
        """
        ユーザーにメッセージを送信する

        :param message_list (TextSendMessage): ユーザーに送信するメッセージ
        """
        self._line_bot_api.reply_message(self._reply_token, message_list)
