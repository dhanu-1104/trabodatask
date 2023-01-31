import random
import telebot

bot = telebot.TeleBot("5850408746:AAF_pYfrtlC0mll4OerdEuZ7sfOEQLH0yQQ", parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Hello there! I am a bot that will play rock paper scissors with you. Send me "rock", "paper", or "scissors" to play.')
   
@bot.message_handler(commands=['stop', 'bye'])
def goodbye(message):
    bot.reply_to(message, 'Bye! Have a good time')
    
@bot.message_handler(content_types=['text'])
def play_rps(message):
    choices = ['rock', 'paper', 'scissors']
    user_action = message.text.strip().lower()
    if user_action not in choices:
        bot.send_message(chat_id=message.chat.id, text="Invalid choice. Please choose rock, paper, or scissors.")
        return
    computer_action = random.choice(choices)
    bot.send_message(chat_id=message.chat.id, text=f"You chose {user_action}, computer chose {computer_action}.")

    if user_action == computer_action:
        bot.send_message(chat_id=message.chat.id, text="It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            bot.send_message(chat_id=message.chat.id, text="Rock blunts scissors! You win!")
    elif user_action == "scissors":
        if computer_action == "rock":
            bot.send_message(chat_id=message.chat.id, text="Rock blunts scissors! I win!")
    elif user_action == "paper":
        if computer_action == "rock":
            bot.send_message(chat_id=message.chat.id, text="Paper covers rock! You win.")
    elif user_action == "rock":
        if computer_action == "paper":
            bot.send_message(chat_id=message.chat.id, text="Paper covers rock! I win.")
    elif user_action == "scissors":
        if computer_action == "paper":
            bot.send_message(chat_id=message.chat.id, text="scissors cut paper! You win.")
    elif user_action == "paper":
        if computer_action == "scissors":
            bot.send_message(chat_id=message.chat.id, text="scissors cut paper! I win.")
        else:
            bot.send_message(chat_id=message.chat.id, text="try again")
    
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)
bot.polling()
