from transitions.extensions import GraphMachine
import os
import random

from utils import send_text_message
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,TemplateSendMessage,ButtonsTemplate,MessageTemplateAction,ImageSendMessage,ImageCarouselTemplate,ImageCarouselColumn,PostbackTemplateAction )
from linebot import LineBotApi, WebhookParser

channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
line_bot_api = LineBotApi(channel_access_token)

#                       1     2      3      4     5      6     7      8     9     10      11      12    13       14     15    16
male_twicher_name = ['6tan','餐哥','鳥屎','國棟','虧皮','館長','爆哥','Rex','KO','Toyz','NL(MK)', '老皮','史丹利','花輪','懶貓','UZRA']
male_used = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
male_url = ['https://img.piku.co.kr/w/uploads/1EzjZH/19094e876afc18befb686aa4bdfcd69d.jpg','https://img.piku.co.kr/w/uploads/1EzjZH/9a86fadea62c342986f940a1f8a4cbf7.jpg','https://img.piku.co.kr/w/uploads/1EzjZH/10c6e257e25b3950f86e0bcd8292161a.jpg',
'https://img.piku.co.kr/w/uploads/1EzjZH/14bea65518c72195df7bc0591c4a8836.jpg','https://img.piku.co.kr/w/uploads/1EzjZH/bd8b7017e68f39197d7d6d2e32b3f18b.jpg','https://img.piku.co.kr/w/uploads/1EzjZH/06117a47bf17e62bb191b5373031cf49.jpg',
'https://img.piku.co.kr/w/uploads/1EzjZH/0fc7bdfec9a9aebe8ea6be472079ef03.jpg','https://img.piku.co.kr/w/uploads/1EzjZH/bd4cd92c994b5ef13a96d30002f63e49.jpg','https://img.piku.co.kr/w/uploads/1EzjZH/2eb5d91905274783a523219b14f6754d.jpg',
'https://img.piku.co.kr/w/uploads/1EzjZH/c82fdf7085cf5f24212790019c97069f.jpg','https://img.piku.co.kr/w/uploads/1EzjZH/79de8d7b5ea9bdafc51a71257e23dade.jpg','https://img.piku.co.kr/w/uploads/1EzjZH/c98fd925d3e87d125815b9a69187c112.jpg',
'https://img.piku.co.kr/w/uploads/1EzjZH/801d6720f2615d90cd6de432df033f7d.jpg','https://img.piku.co.kr/w/uploads/1EzjZH/dee9c8e7555f26923ae4c14c67d00ae2.jpg','https://img.piku.co.kr/w/uploads/1EzjZH/1a028760ad1d5313c60f7333700a266e.jpg',
'https://img.piku.co.kr/w/uploads/1EzjZH/19ff9750e7811d014a76351dd5d82387.jpg']
#                          1      2      3     4      5       6       7      8      9     10       11      12     13     14     15      16
female_twitcher_name = ['Mita','小熊','湘湘','凱琪','愷蒂喵','妮妮','企鵝妹','ViVi','蛋捲','優格','小雲寶寶','諾曼','妮婭','劉萱','阿樂','天菜娘娘']
female_uese = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

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
    
    def on_enter_male(self,event):
        num1 = random.randint(0,15)
        num2 = random.randint(0,15)
        while num1 == num2:
            num2 = random.randint(0,15)
        male_used[num1] = -1
        male_used[num2] = -1
        s1 = male_twicher_name[num1]
        s2 = male_twicher_name[num2]
        u1 = male_url[num1]
        u2 = male_url[num2]
        line_bot_api.reply_message(
            event.reply_token,
            TemplateSendMessage(
                alt_text = 'ImageCarousel template',
                template = ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url = u1,
                            action = PostbackTemplateAction(
                                label='postback1',
                                text=s1,
                            )
                        ),
                        ImageCarouselColumn(
                            image_url=u2,
                            action=PostbackTemplateAction(
                                label='postback2',
                                text=s2,
                            )
                        )
                    ]
                )
            )
        )
    def do_male1_comp(self,event,te,x):
        index = 0
        while index < 16:
            if male_twicher_name[index] == te:
                male_used[index] = 2
                break
            else :
                index += 1
        num1 = random.randint(0,15)
        num2 = random.randint(0,15)
        while male_used[num1] == -1 or male_used[num1] == 2:
            num1 = random.randint(0,15)
        while num1 == num2  or male_used[num2] == -1 or male_used[num2] == 2:
            num2 = random.randint(0,15)
        male_used[num1] = -1
        male_used[num2] = -1
        s1 = male_twicher_name[num1]
        s2 = male_twicher_name[num2]
        line_bot_api.reply_message(
            event.reply_token,[
            TemplateSendMessage(
                alt_text = 'ImageCarousel template',
                template = ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(
                            image_url = 'https://img.piku.co.kr/w/uploads/1EzjZH/19094e876afc18befb686aa4bdfcd69d.jpg',
                            action = PostbackTemplateAction(
                                label='postback1',
                                text='postback text1',
                                data='action=buy&itemid=1'
                            )
                        ),
                        ImageCarouselColumn(
                            image_url='https://img.piku.co.kr/w/uploads/1EzjZH/19094e876afc18befb686aa4bdfcd69d.jpg',
                            action=PostbackTemplateAction(
                                label='postback2',
                                text='postback text2',
                                data='action=buy&itemid=2'
                            )
                        )
                    ]
                )
            )
            ]
        )
    def on_enter_male2(self,event):
        num1 = random.randint(0,15)
        num2 = random.randint(0,15)
        while male_used[num1] != 2:
            num1 = random.randint(0,15)
        while num1 == num2 or male_used[num2] == -1:
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
                    title = '1/4選擇',
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
    def do_male2_comp(self,event,tt,xx):
        # reply_token = event.reply_token
        # send_text_message(reply_token, x2)
        ind = 0
        while ind < 16:
            if male_twicher_name[ind] == tt:
                male_used[ind] = 3
                break
            else :
                ind += 1
        num1 = random.randint(0,15)
        num2 = random.randint(0,15)
        while male_used[num1] == -1 or male_used[num1] == 3:
            num1 = random.randint(0,15)
        while num1 == num2  or male_used[num2] == -1 or male_used[num2] == 3:
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
                    title = str(xx+1) + "/4選擇",
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
    def do_something(self,event,tex):
        ind = 0
        while ind < 16:
            if male_twicher_name[ind] == tex:
                male_used[ind] = 2
                break
            else :
                ind += 1
    def do_something_ver2(self,event,t3):
        ind = 0
        while ind < 16:
            if male_twicher_name[ind] == t3:
                male_used[ind] = 3
                break
            else :
                ind += 1
    def do_something_ver3(self,event,t4):
        ind = 0
        while ind < 16:
            if male_twicher_name[ind] == t4:
                male_used[ind] = 4
                break
            else :
                ind += 1
    def on_enter_male3(self,event):
        num1 = random.randint(0,15)
        num2 = random.randint(0,15)
        while male_used[num1] != 3:
            num1 = random.randint(0,15)
        while num1 == num2 or male_used[num2] == -1:
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
                    title = '1/2選擇',
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
    def do_male3_comp(self,event,t3,x3):
        ind = 0
        while ind < 16:
            if male_twicher_name[ind] == t3:
                male_used[ind] = 4
                break
            else :
                ind += 1
        num1 = random.randint(0,15)
        num2 = random.randint(0,15)
        while male_used[num1] == -1 or male_used[num1] == 4:
            num1 = random.randint(0,15)
        while num1 == num2  or male_used[num2] == -1 or male_used[num2] == 4:
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
                    title = str(x3+1) + "/2選擇",
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
    def on_enter_male4(self,event):
        num1 = random.randint(0,15)
        num2 = random.randint(0,15)
        while male_used[num1] != 4:
            num1 = random.randint(0,15)
        while num1 == num2 or male_used[num2] == -1:
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
                    title = '1/1選擇',
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

    def fdo_something(self,event,tx):
        # reply_token = event.reply_token
        # send_text_message(reply_token, "nothing")
        ind = 0
        while ind < 16:
            if female_twitcher_name[ind] == tx:
                female_uese[ind] = 2
                break
            else :
                ind += 1
    def fdo_something_ver2(self,event,tx):
        global female_uese
        ind = 0
        while ind < 16:
            if female_twitcher_name[ind] == tx:
                female_uese[ind] = 3
                break
            else :
                ind += 1
    def fdo_something_ver3(self,event,t3):
        global female_uese
        ind = 0
        while ind < 16:
            if female_twitcher_name[ind] == t3:
                female_uese[ind] = 4
                break
            else :
                ind += 1   
    def fdo_female_comp(self,event,te,x):
        global female_uese
        index = 0
        while index < 16:
            if female_twitcher_name[index] == te:
                female_uese[index] = 2
                break
            else :
                index += 1
        num1 = random.randint(0,15)
        num2 = random.randint(0,15)
        while female_uese[num1] != 0:
            num1 = random.randint(0,15)
        while num1 == num2  or female_uese[num2] != 0:
            num2 = random.randint(0,15)
        female_uese[num1] = -1
        female_uese[num2] = -1
        s1 = female_twitcher_name[num1]
        s2 = female_twitcher_name[num2] 
        line_bot_api.reply_message(
            event.reply_token,
            TemplateSendMessage(
                alt_text = 'Button template',
                template = ButtonsTemplate(
                    title = str(x+1) + "/8選擇",
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
    def fdo_female_comp2(self,event,ft2,xx):
        global female_uese
        # reply_token = event.reply_token
        # send_text_message(reply_token, x2)
        ind = 0
        while ind < 16:
            if female_twitcher_name[ind] == ft2:
                female_uese[ind] = 3
                break
            else :
                ind += 1
        num1 = random.randint(0,15)
        num2 = random.randint(0,15)
        while female_uese[num1] != 2:
            num1 = random.randint(0,15)
        while num1 == num2  or female_uese[num2] == -1 or female_uese[num2] == 3:
            num2 = random.randint(0,15)
        female_uese[num1] = -1
        female_uese[num2] = -1
        s1 = female_twitcher_name[num1]
        s2 = female_twitcher_name[num2]
        line_bot_api.reply_message(
            event.reply_token,
            TemplateSendMessage(
                alt_text = 'Button template',
                template = ButtonsTemplate(
                    title = str(xx+1) + "/4選擇",
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
    def fdo_female_comp3(self,event,t3,x3):
        global female_uese
        ind = 0
        while ind < 16:
            if female_twitcher_name[ind] == t3:
                female_uese[ind] = 4
                break
            else :
                ind += 1
        num1 = random.randint(0,15)
        num2 = random.randint(0,15)
        while female_uese[num1] == -1 or female_uese[num1] == 4:
            num1 = random.randint(0,15)
        while num1 == num2  or female_uese[num2] == -1 or female_uese[num2] == 4:
            num2 = random.randint(0,15)
        female_uese[num1] = -1
        female_uese[num2] = -1
        s1 = female_twitcher_name[num1]
        s2 = female_twitcher_name[num2]
        line_bot_api.reply_message(
            event.reply_token,
            TemplateSendMessage(
                alt_text = 'Button template',
                template = ButtonsTemplate(
                    title = str(x3+1) + "/2選擇",
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

    def on_enter_female(self,event):
        global female_uese
        num1 = random.randint(0,15)
        num2 = random.randint(0,15)
        while num1 == num2:
            num2 = random.randint(0,15)
        female_uese[num1] = -1
        female_uese[num2] = -1
        s1 = female_twitcher_name[num1]
        s2 = female_twitcher_name[num2]
        line_bot_api.reply_message(
            event.reply_token,
            TemplateSendMessage(
                alt_text = 'Button template',
                template = ButtonsTemplate(
                    title = '1/8選擇',
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
    def on_enter_female2(self,event):
        # index = 0
        # s = ""
        # while index < 16:
        #     s += str(female_uese[index]) + " "
        #     index += 1
        # reply_token = event.reply_token
        # send_text_message(reply_token,s)
        num1 = random.randint(0,15)
        num2 = random.randint(0,15)
        while female_uese[num1] != 2:
            num1 = random.randint(0,15)
        while num1 == num2 or female_uese[num2] == -1:
            num2 = random.randint(0,15)
        female_uese[num1] = -1
        female_uese[num2] = -1
        s1 = female_twitcher_name[num1]
        s2 = female_twitcher_name[num2]
        line_bot_api.reply_message(
            event.reply_token,
            TemplateSendMessage(
                alt_text = 'Button template',
                template = ButtonsTemplate(
                    title = '1/4選擇',
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
    def on_enter_female3(self,event):
        num1 = random.randint(0,15)
        num2 = random.randint(0,15)
        while female_uese[num1] != 3:
            num1 = random.randint(0,15)
        while num1 == num2 or female_uese[num2] != 3:
            num2 = random.randint(0,15)
        female_uese[num1] = -1
        female_uese[num2] = -1
        s1 = female_twitcher_name[num1]
        s2 = female_twitcher_name[num2]
        line_bot_api.reply_message(
            event.reply_token,
            TemplateSendMessage(
                alt_text = 'Button template',
                template = ButtonsTemplate(
                    title = '1/2選擇',
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
    def on_enter_female4(self,event):
        global female_uese
        num1 = random.randint(0,15)
        num2 = random.randint(0,15)
        while female_uese[num1] != 4:
            num1 = random.randint(0,15)
        while num1 == num2 or female_uese[num2] == -1:
            num2 = random.randint(0,15)
        female_uese[num1] = -1
        female_uese[num2] = -1
        s1 = female_twitcher_name[num1]
        s2 = female_twitcher_name[num2]
        line_bot_api.reply_message(
            event.reply_token,
            TemplateSendMessage(
                alt_text = 'Button template',
                template = ButtonsTemplate(
                    title = '1/1選擇',
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

    def do_initia(self,event):
        global male_used,female_uese
        index = 0
        while index <16:
            male_used[index] = 0
            female_uese[index] = 0
            index += 1

    def do_print(self,event):
        index = 0
        s = ""
        while index < 16:
            s += str(male_used[index]) + " "
            index += 1
        reply_token = event.reply_token
        send_text_message(reply_token,s)
    def fdo_print(self,event):
        index = 0
        s = ""
        while index < 16:
            s += str(female_uese[index]) + " "
            index += 1
        reply_token = event.reply_token
        send_text_message(reply_token,s)

    def show_final_result(self,event,t4):
        sss = "感謝您，使用此功能\n您最後的選擇是\n====  "+ t4 +"  ===="
        reply_token = event.reply_token
        send_text_message(reply_token, sss)
    
    def do_nothing(self,event):
        reply_token = event.reply_token
        send_text_message(reply_token, "nothing")
   
    