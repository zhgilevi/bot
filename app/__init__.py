from flask import Flask,request,jsonify
import telebot
import json
token="781229574:AAGC6K39EQ1VNcf2RTOlLpXg_KWoHPAZTI"

app = Flask(__name__)
bot=telebot.TeleBot(token)



@app.route('/',methods=["POST","GET"])
def hello_world():
    if request.method == "POST":
        r=json.loads(request.data)
        chat_id=r['message']['chat']['id']
        bot.send_message(chat_id,'it work')
        return (jsonify(r),200)
    else:
 
        return ('Hi',200,None)
