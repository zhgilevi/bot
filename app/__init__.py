from flask import Flask,request,jsonify
import telebot
token="683907622:AAFDIZxPvAQJXqFQNc4zwGgggmvs9EICr8c"

app = Flask(__name__)
bot=telebot.TeleBot(token)
bot.set_webhook(url='https://easybot123.herokuapp.com/')


@app.route('/',methods=["GET","POST"])
def hello_world():
    if request.method=="POST":
        return request.get_json()
    bot.send_message(421590404,"Hello from heroku")
    return ('Hello World!',200,None)
