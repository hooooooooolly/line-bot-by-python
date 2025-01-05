import json
import os
import random

def get_received_text(event):
    """
    受信したメッセージ本文を取得

    :param event: イベント
    :return: メッセージ本文
    """
    body = json.loads(event['body'])
    return body['events'][0]['message']['text']

def get_reply_token(event):
    """
    受信したメッセージのリプライトークンを取得

    :param event: イベント
    :return: リプライトークン
    """
    body = json.loads(event['body'])
    return body['events'][0]['replyToken']

def get_access_token():
    """
    アクセストークンを取得

    :return: 環境変数から取得したアクセストークン
    """
    return os.environ['LINE_CHANNEL_ACCESS_TOKEN']

def is_in_range(start, end, number):
    """
    指定された範囲内に含まれているかどうかを判断する
    
    :param start: 最小値（含む）
    :param end: 最大値（含む）
    :param number: 対象値
    """
    return start <= number <= end

def can_get_msg(probability):
    """
    指定した割合で乱数が取得できたかどうか
    
    :param probability: 成功率（百分率）
    :return 成功の場合true
    """
    rnd_num = random.randint(1, 100)
    return rnd_num <= probability
