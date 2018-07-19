from flask import Flask,request,jsonify
import telebot
token="683907622:AAFDIZxPvAQJXqFQNc4zwGgggmvs9EICr8c"

app = Flask(__name__)
bot=telebot.TeleBot(token)



@app.route('/',methods=["POST","GET"])
def hello_world():
    if request.method == "POST":
        count+=1
        return (request.get_json(),200,None)
    else:
 
        return ('Hi',200,None)
