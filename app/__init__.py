from flask import Flask,request,jsonify
import telebot
token="683907622:AAFDIZxPvAQJXqFQNc4zwGgggmvs9EICr8c"

app = Flask(__name__)
bot=telebot.TeleBot(token)



@app.route('/',methods=["POST","GET"])
def hello_world():
    if request.method == "POST":
        r=request.get_json()
        chat_id=r['message']['chat']['id']
        bot.send_message(chat_id,'it work')
        return (jsonify(r),200)
    else:
 
        return ('Hi',200,None)
