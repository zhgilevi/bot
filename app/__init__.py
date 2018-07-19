from flask import Flask,request,jsonify
import telebot
token="683907622:AAFDIZxPvAQJXqFQNc4zwGgggmvs9EICr8c"

app = Flask(__name__)
bot=telebot.TeleBot(token)



@app.route('/')
def hello_world():
    bot.send_message(421590404,"Hello from heroku")
    return ('Hello World!',200,None)
