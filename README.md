# Telegram Bot

This project contains a simple Telegram bot built with [aiogram](https://docs.aiogram.dev). The bot stores text, photo and video messages in a SQLite database. An admin web interface built with Flask allows viewing the stored data in a browser.

## Requirements
Install the dependencies using pip:

```bash
pip install -r requirements.txt
```

## Configuration
The bot uses environment variables for configuration:

- `BOT_TOKEN` – Telegram bot token.
- `DB_PATH` – path to the SQLite database file (default: `bot.db`).
- `ADMIN_PASSWORD` – password for the admin interface (default: `admin`).

## Usage
Run the Telegram bot:

```bash
python -m bot.bot
```

Run the admin panel:

```bash
python -m bot.admin
```

Then open `http://localhost:5000` in your browser and enter the admin password to view stored messages.
