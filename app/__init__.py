from flask import Flask,request,jsonify
import telebot
token="683907622:AAFDIZxPvAQJXqFQNc4zwGgggmvs9EICr8c"

app = Flask(__name__)
bot=telebot.TeleBot(token)
bot.set_webhook(url='https://easybot123.herokuapp.com/')


@app.route('/',methods=["POST","GET"])
def hello_world():
    if request.method=='POST':
        d=request.get_data()
        r=d.json
        return (jsonify(r),200)
    bot.send_message(421590404,"Hello from heroku")
    return ('Hello World!',200,None)
