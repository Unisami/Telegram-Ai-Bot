import telebot
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
if not TELEGRAM_BOT_TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN is not set in the environment variables")

client = genai.Client(api_key=GEMINI_API_KEY)
def ask_gemini(prompt):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"You are a telegram bot, reply with short answer to the following prompt, use natural language, respond like a human would, maybe even make spelling mistakes, but not too much:\n{prompt}")
    return response.text


bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN, parse_mode="markdown")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, ask_gemini(message.text))


print("starting bot...")
bot.infinity_polling()