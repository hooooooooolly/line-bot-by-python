from creator.fortune_creator     import FortuneCreator
from creator.default_creator     import DefaultCreator
from creator.greet_creator       import GreetCreator

class MessageFactory:
    """
    受信したメッセージに応じて専用クラスを返すファクトリクラス.
    """

    #完全一致の場合に返すクラス
    _keywords_to_classes_exact = {
        'やあ': GreetCreator
        , 'こんにちは': GreetCreator
        , 'こんばんは': GreetCreator
    }

    #部分一致の場合に返すクラス
    _keywords_to_classes_partial = {
        '占い': FortuneCreator
        , '占って': FortuneCreator
        , 'おはよう': GreetCreator
    }

    @staticmethod
    def create_message_creator(message: str):
        #完全一致
        if message in MessageFactory._keywords_to_classes_exact:
            return MessageFactory._keywords_to_classes_exact[message](message)
        #部分一致
        else:
            for keyword, message_class in MessageFactory._keywords_to_classes_partial.items():
                if keyword in message:
                    return message_class(message)
        #一致なし
        return DefaultCreator(message)
