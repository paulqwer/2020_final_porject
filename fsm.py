from transitions.extensions import GraphMachine
import os
import random

from utils import send_text_message
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,TemplateSendMessage,ButtonsTemplate,MessageTemplateAction)
from linebot import LineBotApi, WebhookParser

channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
line_bot_api = LineBotApi(channel_access_token)

#                       1     2      3      4     5      6     7      8     9         10      11      12    13       14     15    16
male_twicher_name = ['6tan','餐哥','鳥屎','國棟','虧皮','館長','爆哥','Rex','KO0416','Toyz','NL(MK)', '老皮','史丹利','花輪','懶貓','UZRA']
male_used = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

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
    # def on_enter_male(self,event):
    #     reply_token = event.reply_token
    #     send_text_message(reply_token, "您已進入男性選擇區 haha")
    
    def on_enter_male(self,event):
        num1 = random.randint(0,15)
        num2 = random.randint(0,15)
        while male_used[num1] != 0:
            num1 = random.randint(0,15)
        while num1 == num2 or male_used[num2] != 0:
            num2 = random.randint(0,15)
        male_used[num1] = -1
        male_used[num2] = -1
        s1 = male_twicher_name[num1]
        s2 = male_twicher_name[num2]
        line_bot_api.reply_message(
            event.reply_token,
            TemplateSendMessage(
                alt_text = 'Button template',
                template = ButtonsTemplate(
                    title = '選擇',
                    text = '請選擇你最喜歡的實況主',
                    actions = [
                        MessageTemplateAction(
                            label = s1,
                            text = s1
                        ),
                        MessageTemplateAction(
                            label = s2,
                            text = s2
                        )
                    ]
                )
            )
        )
   
    def do_f_compete(self,event,times):
        num1 = random.randint(0,15)
        num2 = random.randint(0,15)
        while male_used[num1] != times:
            num1 = random.randint(0,15)
        while num1 == num2 or male_used[num2] != times:
            num2 = random.randint(0,15)
        male_used[num1] = -1
        male_used[num2] = -1
        s1 = male_twicher_name[num1]
        s2 = male_twicher_name[num2]
        line_bot_api.reply_message(
            event.reply_token,
            TemplateSendMessage(
                alt_text = 'Button template',
                template = ButtonsTemplate(
                    title = '選擇',
                    text = '請選擇你最喜歡的實況主',
                    actions = [
                        MessageTemplateAction(
                            label = s1,
                            text = s1
                        ),
                        MessageTemplateAction(
                            label = s2,
                            text = s2
                        )
                    ]
                )
            )
        )
    def do_times_count(self,event,index,times):
        i = 0
        male_used[index] = times
        send_text_message(event.reply_token,male_twicher_name[index])
    # def on_enter_comop1(self,event):
    #     num1 = random.randint(0,15)
    #     num2 = random.randint(0,15)
    #     while male_used[num1] == 0 :
    #         num1 = random.randint(0,15)
    #     while num1 == num2 or male_used[num2] == 0:
    #         num2 = random.randint(0,15)
    # def do_male_compete_1(self,event,times):
    #     num1 = random.randint(0,15)
    #     num2 = random.randint(0,15)
    #     while male_used[num1] != 0:
    #         num1 = random.randint(0,15)
    #     while num1 != num2 and male_used[num2] == 0:
    #         num2 = random.randint(0,15)
    #     male_used[num1] = male_used + 1
    #     male_used[num2] = male_used[num2] + 1
    #     s1 = male_twicher_name[num1]
    #     s2 = male_twicher_name[num2]
    #     line_bot_api.reply_message(
    #         event.reply_token,[
    #             TemplateSendMessage(
    #                 alt_text = 'Button template',
    #                 template = ButtonsTemplate(
    #                     title = '選擇',
    #                     text = '請選擇你最喜歡的實況主',
    #                     actions = [
    #                         MessageTemplateAction(
    #                             label = s1,
    #                             text = s1
    #                         ),
    #                         MessageTemplateAction(
    #                             label = s2,
    #                             text = s2
    #                         )
    #                     ]
    #                 )
    #             )
    #         ]
    #     )
    #     return "第一輪"

        def do_nothing(self,event):
            reply_token = event.reply_token
            send_text_message(reply_token, "nothing")