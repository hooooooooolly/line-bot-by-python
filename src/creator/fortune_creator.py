import random
import util
from creator.message_creator import MessageCreator

class FortuneCreator(MessageCreator):
    """
    受信メッセージが'占い'と部分一致する場合の専用クラス

    Attributes:
        message (str): 受信したメッセージ
    """
    def create_send_message(self):
        """
        メッセージ生成用の具象クラス.
        """
        self.add_message('占うよ！')
        self.add_message(self.create_random_message())

    def create_random_message(self):
        """
        占いのメイン処理

        :return: 占い結果
        """
        rnd_num = random.randint(1, 100)
        print('占い結果： ' + str(rnd_num))
        match rnd_num:
            case _ if util.is_in_range(1, 20, rnd_num):
                #20%
                return '悪くない吉！\nおすすめアイテムは森羅万象！\n全てを身に着けろ！'
            case _ if util.is_in_range(21, 65, rnd_num):
                #45%
                return 'そこそこ吉！\nおすすめアイテムはキーマカレー！\n食い尽くせ！'
            case _ if util.is_in_range(66, 95, rnd_num):
                #30%
                return '良い吉！\nおすすめアイテムはカルトン！\n手触りがいいね！'
            case _ if util.is_in_range(96, 100, rnd_num):
                #5%
                return '大吉！\nおすすめアイテムは平等院鳳凰堂！\n祈れ！'
            case _:
                return 'Error in FortuneCreator!'
