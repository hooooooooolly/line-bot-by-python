import random
from creator.message_creator import MessageCreator

class DefaultCreator(MessageCreator):
    """
    受信したメッセージが専用クラスに該当しない場合のデフォルトクラス

    Attributes:
        _message (str): 受信したメッセージ
    """

    def create_send_message(self):
        """
        メッセージ生成用の具象クラス.
        基本的にはおうむ返し
        """
        rnd_num = random.randint(1, 100)
        print('お返事結果： ' + str(rnd_num))
        self.add_message(self._message)
