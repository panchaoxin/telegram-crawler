

# 1. Setup

## 1.1. Installing

```
pip install PyMySQL
pip install telethon
pip install -U requests[socks]
pip install -U pytz
```

## 1.2. Create your Telegram apps

URL：https://my.telegram.org/

Edit `client.py`
```python
# Telegram config
api_id = 123456  # Your api_id
api_hash = '1234562a3e03835d881624e28c6f1d50'  # Your api_hash
session_name = 'session_name'
proxy_param = (socks.SOCKS5, 'localhost', 1080)   # Proxy settings, if you need
```

## 1.3. MySQL setup

Execute `telegram.sql`

Edit `database.py`
```python
# Your MySQL configuration
MYSQL_HOST = 'localhost'
MYSQL_DB = 'telegram'
MYSQL_USER = 'root'
MYSQL_PASS = '123456'

connection = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER,
                             password=MYSQL_PASS, db=MYSQL_DB,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
```

# 2. Run

```bash
# Crawl message
python start_crawl_message.py
python start_crawl_message.py --take-mode=NEW
python start_crawl_message.py --take-mode=OLD
# Crawl user
python start_crawl_user.py
# Crawl contact user
python start_crawl_contact_user.py
```