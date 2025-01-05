import util
from message_factory import MessageFactory
from line_bot_client import LineBotClient

def lambda_handler(event, context):
    #処理開始
    text = util.get_received_text(event)
    print('【処理開始】受信メッセージ：' + text)

    #応答メッセージを作成
    creator = MessageFactory.create_message_creator(text)
    creator.create_send_message()

    #応答メッセージを送信
    reply_token = util.get_reply_token(event)
    client = LineBotClient(reply_token)
    client.send_message(creator.message_list)

    #処理終了
    print('【処理終了】送信メッセージ：')
    for message in creator.message_list:
        print(message)
