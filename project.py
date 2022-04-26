import os, telegram, openpyxl, pandas as pd


##HTTP API from telegrambot - BotFather
chat_id = 'chat-id' ##Add the chat ID where you want to receive the messages
api_key = 'bot-key' ##Add the Bot-Key from BotFather on telegram

data = pd.read_excel('data.xlsx') ##Create and excel file with the IP addresses to monitor and some description on the second column as "customer"
ip_list = list(data['IP'])
name = list(data['Customer'])

## Function to send messages to telegram
def bot(msg):
  bot = telegram.Bot(token=api_key)
  bot.send_message(chat_id=chat_id, text=str(msg))

def run():
  i = 0
  for ip in ip_list:
    response = os.popen(f"ping {ip}").read()
    if "recibidos = 4" in response:
      msg = "UP " + str(ip) + " - " + str(name[i]) + " - ping successful" ##You can delete this line if you dont want to receive a message for each UP IP address
      print(msg)
    else:
      if 'recibidos = 0' in response:
        msg = "Down " + str(ip) + " - " + str(name[i]) + " - Ping unsuccessful"
        print(msg)
        bot(msg)
      else:
        msg = 'Packet Loss ' + str(ip) + " - " + str(name[i]) + ' - Ping Error'
        print(msg)
        bot(msg)
    i += 1

if __name__ == '__main__':
  run()
