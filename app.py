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
    states=[ "in", "choose","male","male2","mcomp1","mcomp2"],
    transitions=[
        { "trigger" : "go_back_intro", "source" : "choose", "dest" : "in"},
        { "trigger" : "to_choose", "source" : "in", "dest" : "choose"},
        { "trigger" : "to_male", "source" : "choose", "dest" : "male"},
        { "trigger" : "to_male2","source":"male","dest":"male2"},
        { "trigger" : "to_mcomp1", "source":"male", "dest" : "mcomp1"},
        { "trigger" : "to_mcomp2", "source":"mcomp1","dest" : "mcomp2"},
        {"trigger": "go_back", "source": ["state1", "state2"], "dest": "user"},
    ],
    initial="in",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")
#                       1     2      3      4     5      6     7      8     9         10      11      12    13       14     15    16
male_twicher_name = ['6tan','餐哥','鳥屎','國棟','虧皮','館長','爆哥','Rex','KO0416','Toyz','NL(MK)', '老皮','史丹利','花輪','懶貓','UZRA']
first_round_times = 0
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
            machine.go_back_intro(event)
        if machine.state == "in":
            if event.message.text == "介紹":
                machine.introduce(event)
            if event.message.text == "開始":
                machine.to_choose(event)
        if machine.state == "choose":
            if event.message.text == "男性":
                machine.to_male(event)
        if machine.state == "male":
            if isinstance(event,MessageEvent):
                index = 0
                while index < 16:
                    if male_twicher_name[index] == event.message.text:
                        machine.do_nothing(event)
                        break
                    else :
                        index += 1
                # index = 0
                # while index < 16:
                #     if male_twicher_name[index] == event.message.text:
                #         machine.do_times_count(event,index,first_round_times)
                #         break
                #     else :
                #         index += 1
                # machine.to_male2(event)
                
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
