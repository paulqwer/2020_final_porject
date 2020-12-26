import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message

load_dotenv()


machine = TocMachine(
    states=[ "in", "choose","male","male2","male3","male4","female","female2","female3","female4","final"],
    transitions=[
        { "trigger" : "go_back_intro", "source" : ["choose","male", "male2","male3","male4","female","female2","female3","female4","final"], "dest" : "in"},
        { "trigger" : "to_choose", "source" : "in", "dest" : "choose"},
        { "trigger" : "to_male", "source" : "choose", "dest" : "male"},
        { "trigger" : "to_male2","source":"male","dest":"male2"},
        { "trigger" : "to_male3","source":"male2","dest":"male3"},
        { "trigger" : "to_male4","source":"male3","dest":"male4"},
        { "trigger" : "to_female","source":"choose","dest":"female"},
        { "trigger" : "to_female2","source":"female","dest":"female2"},
        { "trigger" : "to_female3","source":"female2","dest":"female3"},
        { "trigger" : "to_female4","source":"female3","dest":"female4"},
        { "trigger" : "to_final","source":["female4,male4"],"dest":"final"},    ],
    initial="in",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")
#                       1     2      3      4     5      6     7      8     9         10      11      12    13       14     15    16
male_twicher_name = ['6tan','餐哥','鳥屎','國棟','虧皮','館長','爆哥','Rex','KO','Toyz','NL(MK)', '老皮','史丹利','花輪','懶貓','UZRA']

f_1_times = 0
f_2_times = 0
f_3_times = 0
f_4_times = 0

ff_1_times = 0
ff_2_times = 0
ff_3_times = 0
ff_4_times = 0

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    global f_1_times,f_2_times,f_3_times,f_4_times,ff_1_times,ff_2_times,ff_3_times,ff_4_times
    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        if event.message.text == "結束":
            f_1_times = 0
            f_2_times = 0
            f_3_times = 0
            f_4_times = 0
            ff_1_times = 0
            ff_2_times = 0
            ff_3_times = 0
            ff_4_times = 0
            machine.do_initia(event)
            machine.go_back_intro(event)
        if machine.state == "in":
            if event.message.text == "介紹":
                machine.introduce(event)
            if event.message.text == "開始":
                f_1_times = 0
                machine.to_choose(event)
        if machine.state == "choose":
            if event.message.text == "男性":
                machine.to_male(event)
            if event.message.text == "女性":
                machine.to_female(event)
        if machine.state == "male":     #t = 1
            if  event.message.text == "6tan" or event.message.text == "餐哥" or event.message.text == "鳥屎" or event.message.text == "國棟" or event.message.text == "虧皮" or event.message.text == "館長" or event.message.text == "爆哥" or event.message.text == "Rex" or event.message.text == "KO" or event.message.text == "Toyz" or event.message.text == "NL(MK)" or event.message.text == "老皮" or event.message.text == "史丹利" or event.message.text =="花輪" or event.message.text == "懶貓" or event.message.text == "UZRA":
                te = event.message.text
                f_1_times = f_1_times +1
                x = f_1_times
                if f_1_times == 8:
                    f_1_times = 0
                    machine.do_something(event,te)
                    machine.to_male2(event)
                else :
                    machine.do_male1_comp(event,te,x)
        elif machine.state == "male2": 
            if  event.message.text == "6tan" or event.message.text == "餐哥" or event.message.text == "鳥屎" or event.message.text == "國棟" or event.message.text == "虧皮" or event.message.text == "館長" or event.message.text == "爆哥" or event.message.text == "Rex" or event.message.text == "KO" or event.message.text == "Toyz" or event.message.text == "NL(MK)" or event.message.text == "老皮" or event.message.text == "史丹利" or event.message.text =="花輪" or event.message.text == "懶貓" or event.message.text == "UZRA":
                # machine.do_print(event)
                tt = event.message.text 
                f_2_times += 1
                xx = f_2_times
                if f_2_times == 4:
                    machine.do_something_ver2(event,tt)
                    machine.to_male3(event)
                else :
                    machine.do_male2_comp(event,tt,xx)
        elif machine.state == "male3":
            if  event.message.text == "6tan" or event.message.text == "餐哥" or event.message.text == "鳥屎" or event.message.text == "國棟" or event.message.text == "虧皮" or event.message.text == "館長" or event.message.text == "爆哥" or event.message.text == "Rex" or event.message.text == "KO" or event.message.text == "Toyz" or event.message.text == "NL(MK)" or event.message.text == "老皮" or event.message.text == "史丹利" or event.message.text =="花輪" or event.message.text == "懶貓" or event.message.text == "UZRA":
                t3 = event.message.text 
                f_3_times += 1
                x3 = f_3_times
                if f_3_times == 2:
                    machine.do_something_ver3(event,t3)
                    # machine.do_nothing(event)
                    machine.to_male4(event)
                else :
                    machine.do_male3_comp(event,t3,x3)
        elif machine.state == "male4":
            if  event.message.text == "6tan" or event.message.text == "餐哥" or event.message.text == "鳥屎" or event.message.text == "國棟" or event.message.text == "虧皮" or event.message.text == "館長" or event.message.text == "爆哥" or event.message.text == "Rex" or event.message.text == "KO" or event.message.text == "Toyz" or event.message.text == "NL(MK)" or event.message.text == "老皮" or event.message.text == "史丹利" or event.message.text =="花輪" or event.message.text == "懶貓" or event.message.text == "UZRA":
                t4 = event.message.text
                f_4_times += 1
                if f_4_times == 1:
                    machine.show_final_result(event,t4)
                else:
                    machine.to_final(event)
        elif machine.state == "female":
            if event.message.text == "Mita" or event.message.text == "小熊" or event.message.text == "湘湘" or event.message.text == "阿倪" or event.message.text == "愷蒂喵" or event.message.text == "妮妮" or event.message.text == "艾比純純" or event.message.text == "ViVi" or event.message.text == "蛋捲" or event.message.text == "優格" or event.message.text == "小雲寶寶" or event.message.text == "諾曼" or event.message.text == "妮婭" or event.message.text =="劉萱" or event.message.text == "阿樂" or event.message.text == "JoJo":
                # machine.do_nothing(event)
                ft1 = event.message.text
                ff_1_times += 1
                fx1 = ff_1_times
                if ff_1_times == 8:
                    ff_1_times = 0
                    machine.fdo_something(event,ft1)
                    machine.to_female2(event)
                else :
                    machine.fdo_female_comp(event,ft1,fx1)
        elif machine.state == "female2":
            if event.message.text == "Mita" or event.message.text == "小熊" or event.message.text == "湘湘" or event.message.text == "阿倪" or event.message.text == "愷蒂喵" or event.message.text == "妮妮" or event.message.text == "艾比純純" or event.message.text == "ViVi" or event.message.text == "蛋捲" or event.message.text == "優格" or event.message.text == "小雲寶寶" or event.message.text == "諾曼" or event.message.text == "妮婭" or event.message.text =="劉萱" or event.message.text == "阿樂" or event.message.text == "JoJo":
                #machine.fdo_print(event)
                ft2 = event.message.text 
                ff_2_times += 1
                xx = ff_2_times
                if ff_2_times == 4:
                    machine.fdo_something_ver2(event,ft2)
                    machine.to_female3(event)
                else :
                    machine.fdo_female_comp2(event,ft2,xx)
        elif machine.state == "female3":
            if event.message.text == "Mita" or event.message.text == "小熊" or event.message.text == "湘湘" or event.message.text == "阿倪" or event.message.text == "愷蒂喵" or event.message.text == "妮妮" or event.message.text == "艾比純純" or event.message.text == "ViVi" or event.message.text == "蛋捲" or event.message.text == "優格" or event.message.text == "小雲寶寶" or event.message.text == "諾曼" or event.message.text == "妮婭" or event.message.text =="劉萱" or event.message.text == "阿樂" or event.message.text == "JoJo":
                ft3 = event.message.text 
                ff_3_times += 1
                x3 = ff_3_times
                if ff_3_times == 2:
                    machine.fdo_something_ver3(event,ft3)
                    # machine.do_nothing(event)
                    machine.to_female4(event)
                else :
                    machine.fdo_female_comp3(event,ft3,x3)
        elif machine.state == "female4":
            if event.message.text == "Mita" or event.message.text == "小熊" or event.message.text == "湘湘" or event.message.text == "阿倪" or event.message.text == "愷蒂喵" or event.message.text == "妮妮" or event.message.text == "艾比純純" or event.message.text == "ViVi" or event.message.text == "蛋捲" or event.message.text == "優格" or event.message.text == "小雲寶寶" or event.message.text == "諾曼" or event.message.text == "妮婭" or event.message.text =="劉萱" or event.message.text == "阿樂" or event.message.text == "JoJo":
                t4 = event.message.text
                ff_4_times += 1
                if ff_4_times == 1:
                    machine.show_final_result(event,t4)
                else :
                    machine.to_final(event)
        # if machine.state == "male2":    #t = 2
        #     if  event.message.text == "6tan" or event.message.text == "餐哥" or event.message.text == "鳥屎" or event.message.text == "國棟" or event.message.text == "虧皮" or event.message.text == "館長" or event.message.text == "爆哥" or event.message.text == "Rex" or event.message.text == "KO" or event.message.text == "Toyz" or event.message.text == "NL(MK)" or event.message.text == "老皮" or event.message.text == "史丹利" or event.message.text =="花輪" or event.message.text == "懶貓" or event.message.text == "UZRA":
        #         index = 0
        #         first_round_times += 1
        #         while index < 16:
        #             if male_twicher_name[index] == event.message.text:
        #                 machine.do_times_count(event,index,first_round_times)
        #                 break
        #             else :
        #                 index += 1
        #         machine.to_male3(event)
        # if machine.state == "male3":
        #     if  event.message.text == "6tan" or event.message.text == "餐哥" or event.message.text == "鳥屎" or event.message.text == "國棟" or event.message.text == "虧皮" or event.message.text == "館長" or event.message.text == "爆哥" or event.message.text == "Rex" or event.message.text == "KO" or event.message.text == "Toyz" or event.message.text == "NL(MK)" or event.message.text == "老皮" or event.message.text == "史丹利" or event.message.text =="花輪" or event.message.text == "懶貓" or event.message.text == "UZRA":
        #         index = 0
        #         first_round_times += 1
        #         while index < 16:
        #             if male_twicher_name[index] == event.message.text:
        #                 machine.do_times_count(event,index,first_round_times)
        #                 break
        #             else :
        #                 index += 1
        #         machine.to_male4(event)    
                
        # if machine.state == "mcomp1":
        #     index = 0   
        #     while index < 16:
        #         if event.message.text == male_twicher_name[index]:
        #             machine.to_mcomp2(event)
        #             break
        #         else :
        #             index = index + 1
            
        




    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
