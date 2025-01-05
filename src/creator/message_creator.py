from abc import ABC, abstractmethod
from linebot.models import TextSendMessage

class MessageCreator(ABC):
    """
    ユーザーへの返答メッセージ用の基底クラス

    Attributes:
        _message (str): 受信したメッセージ
        _message_list (TextSendMessage[]): 返答メッセージ
    """

    def __init__(self, msg: str):
        """
        イニシャライザ.

        Args:
            msg (str): 受信したメッセージ
        """
        self._message = msg
        self._message_list = []

    @abstractmethod
    def create_send_message(self):
        """
        返答メッセージ生成用の抽象クラス.
        サブクラスでオーバーライドして生成したメッセージを返すこと.

        :return: 返答メッセージ
        """
        pass

    def add_message(self, msg: str):
        """
        返答メッセージを追加する

        :param msg (str): 追加したい返答メッセージ
        """
        self._message_list.append(TextSendMessage(msg))

    @property
    def message_list(self):
        """返答メッセージ取得用プロパティ"""
        return self._message_list
