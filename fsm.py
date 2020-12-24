from transitions.extensions import GraphMachine
import os

from utils import send_text_message
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,TemplateSendMessage,ButtonsTemplate,MessageTemplateAction)
from linebot import LineBotApi, WebhookParser

channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
line_bot_api = LineBotApi(channel_access_token)

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_state1(self, event):
        text = event.message.text
        return text.lower() == "go to state1"

    def is_going_to_state2(self, event):
        text = event.message.text
        return text.lower() == "go to state2"

    def on_enter_state1(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state1")
        self.go_back()

    def on_exit_state1(self):
        print("Leaving state1")

    def on_enter_state2(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state2")
        self.go_back()

    def on_exit_state2(self):
        print("Leaving state2")

    def introduce(self,event):
        reply_token = event.reply_token
        send_text_message(reply_token,"===歡迎來到台灣實況主二選一===\n===輸入{開始}即可進入===\n===輸入{結束}可以重新開始===")
    
    def on_enter_in(self,event):
        reply_token = event.reply_token
        send_text_message(reply_token,"===歡迎來到台灣實況主二選一===\n===輸入{開始}即可進入===\n===輸入{結束}可以重新開始===")

    def  on_enter_choose(self,event):
        line_bot_api.reply_message(
            event.reply_token,
            TemplateSendMessage(
                alt_text = 'Button template',
                template = ButtonsTemplate(
                    title = '選擇',
                    text = '請選擇實況主的性別',
                    actions = [
                        MessageTemplateAction(
                            label = '男性',
                            text = '男性'
                        ),
                        MessageTemplateAction(
                            label = '女性',
                            text = '女性'
                        )
                    ]
                )
            )
        )