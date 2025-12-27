# Telegram Bot

A simple Telegram bot build with **aiogram**.

## Features
- Respons to '/start' command
- Echoes user text messages

# Tech Stack
- Python
- aiogram (v3)

# How to run
1.Create a virtual environment

2.Install dependencies:
```bash
pip install -r requirement.txt
```
3.Create a .env file in the project root and add your Telegram bot token
```bash
BOT_TOKEN=yourBotToken
```
4.Run the bot
```bash
python main.py
```
⚠️ Make sure a system-wide VPN is enabled, otherwise the bot may not be able to connect to Telegram servers.

# Project structure
```bash
Bot/
├── main.py
├── config.py
├── requirements.txt
├── handlers/
│   ├── start.py
│   └── echo.py
```
