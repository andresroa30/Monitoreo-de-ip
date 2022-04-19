import os, requests, telegram
from telegram.ext import Updater

##HTTP API:
ip_list = ['8.8.8.8', '8.8.4.4'] ##Set a list of the IP addresses or range IP you want to monitor
user_id = 'userid' ##set the user ID from your telegram bot
api_key = 'apikey' ##Set API Key

## function to send the messge to telegram
def bot(msg):
  bot = telegram.Bot(token=api_key)
  bot.send_message(chat_id=user_id, text=str(msg))

## Function to monitor the IP list set before
def run():
  for ip in ip_list:
    response = os.popen(f"ping {ip}").read()
    if "recibidos = 4" in response:
      msg = "UP " + str(ip) + " ping successful"
      print(msg)
      response = bot(msg)
    else:
      msg = "Down " + str(ip) + " Ping unsuccessful"
      print(msg)
      response = bot(msg)

if __name__ == '__main__':
  run()
