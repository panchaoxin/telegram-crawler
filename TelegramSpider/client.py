# -*- coding: utf-8 -*-

from telethon import TelegramClient, sync
import socks

# Telegram config
api_id = 123456  # Your api_id
api_hash = 1234562a3e03835d881624e28c6f1d50  # Your api_hash
session_name = 'session_name'
proxy_param = (socks.SOCKS5, 'localhost', 1080)   # Proxy settings, if you need

# Create connection
client = TelegramClient(session_name, api_id, api_hash,
                            proxy=proxy_param).start()
