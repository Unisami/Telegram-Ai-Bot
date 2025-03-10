# Telegram Bot with Gemini AI Integration

A demo project that shows how multiple APIs can be integrated. 

## Prerequisites

-   Python 3.10+
-   Telegram Bot Token
-   Gemini API Key

## Installation

1.  Clone the repository:

    ```bash
    git clone https://github.com/Unisami/Telegram-Ai-Bot
    cd Telegram-Ai-Bot
    ```

2.  Install the required packages:

    ```bash
    pip install pyTelegramBotAPI google-generativeai python-dotenv
    ```

3.  Set up environment variables:
    -   Add your API keys to the `.env` file.

## Usage

1.  Run the bot:

    ```bash
    python tbot.py
    ```

2.  Interact with the bot on Telegram. Send `/start` or `/help` to initiate a conversation.  The bot will respond to other messages using Gemini AI.

## Environment Variables

-   `TELEGRAM_BOT_TOKEN`:  The token for your Telegram bot, obtained from BotFather.
-   `GEMINI_API_KEY`: The API key for accessing the Gemini AI model.
