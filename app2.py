# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 01:00:17 2018

@author: linzino
"""


from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('x5105S4R2QkrZ2PsEJixiGmqn3xDxU6LVeEqm8HpqoRKPVvfhBx0sJm7lsH//haHGUAAKsWP+3mNELhuWNUm8YrqAETJ8iBpVsM6JqoXQbpo5WXHUpvkF648m0w8yoTLmYRMfkPFdOn6GMCx/76JbQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('d970b1a7c8c265e7885551211f161b92')



@app.route("/callback", methods=['POST'])
def callback():

    
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="愛惠惠！愛鈞婷！愛竣博"))
 

if __name__ == '__main__':
    app.run(debug=True)