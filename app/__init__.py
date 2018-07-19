from flask import Flask,request,jsonify
import telebot
token="683907622:AAFDIZxPvAQJXqFQNc4zwGgggmvs9EICr8c"

app = Flask(__name__)
bot=telebot.TeleBot(token)
global count=0


@app.route('/',methods=["POST","GET"])
def hello_world():
    global count
    if request.method == "POST":
        count+=1
        return (request.get_json(),200,None)
    else:
        bot.send_message(421590404,"Hello from heroku")
        return (count,200,None)
