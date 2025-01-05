from creator.message_creator import MessageCreator

class GreetCreator(MessageCreator):
    """
    あいさつ用のクラス

    Attributes:
        _message (str): 受信したメッセージ
    """

    def create_send_message(self):
        """
        メッセージ生成用の具象クラス.
        """
        self.add_message(self._message + '！！')
