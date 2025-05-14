# AWS Lambdaで作るLINE bot

## アーキテクチャ

![名称未設定ファイル drawio](https://github.com/user-attachments/assets/b6f79693-11dc-456c-95d7-68bd29d269b5)

## Messaging API周りの設定方法

[私のブログ記事](https://hollage.net/archives/836)を参照ください。  
  

# 使い方

## 基本的な使い方

1. creator/messsage_creator.pyを継承したクリエータークラスを作成  
2. message_factoryに応答するメッセージを追加し、1で作成したクラスのimport文を追記  
3. 1で作成したクラスはcreate_send_messageをオーバーロードしてメッセージを作成する  
4. creator#self.add_messageを書いた数だけbotが返答を投げます  

## ファイルの説明

### template.xml

CloudFormationやSAMを使ったことないのでよく分かっていません。  
Lambdaレイヤーを使っていることを示すためだけに置いてあります。  
  

### lambda_function.py

ハンドラです。  
MessageFactoryが肝なので流し見すればOKです。  
  

### line_bot_client.py

send_messageメソッドにTextSendMessageのリストを渡せばいい感じにメッセージを送信してくれます。  
  

### message_factory.py

受信メッセージを解析して完全一致または部分一致した場合に、  
該当のメッセージクリエータークラスを返すファクトリクラスです。  
拡張する場合はこちらをよく触ることになると思います。  
  

### util.py

can_get_msgはif~elifで一定の確率で返答メッセージを生成しようと思って作ったものですが、どこからも使われていません。  
is_in_rangeを使ったmatch文が割と可読性低いんですよねえ。  
  

### creator/messsage_creator.py

基底クラスです。  
大したことはしていませんが、add_messageメソッドだけ軽く読んでおいてください。  
  

### creator/default_creator.py

MessageFactoryで指定したメッセージと一致しなかった場合のデフォルトクラスです。  
元気キャラbotを作るなら `+ '！！！'` とすればいいし、お店のアカウントならpassすればいいと思います。  
  

### creator/その他のcreatorファイル

create_send_messageをオーバーロードして後は好きに書いてください。  
self.add_messageの数だけメッセージを送信します。
