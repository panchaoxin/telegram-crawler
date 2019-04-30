

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
api_hash = 1234562a3e03835d881624e28c6f1d50  # Your api_hash
session_name = 'session_name'
proxy_param = (socks.SOCKS5, 'localhost', 1080)   # Proxy settings, if you need
```

## 1.3. MySQL setup

Execute `telegram.sql`
```sql
-- ----------------------------
-- Table structure for message
-- ----------------------------
DROP TABLE IF EXISTS `message`;
CREATE TABLE `message`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `message_id` bigint(20) DEFAULT NULL,
  `chat_id` bigint(20) DEFAULT NULL,
  `is_out` tinyint(1) DEFAULT NULL,
  `is_mentioned` tinyint(1) DEFAULT NULL,
  `message` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `date` datetime(0) DEFAULT NULL,
  `from_id` bigint(20) DEFAULT NULL,
  `is_reply` tinyint(1) DEFAULT NULL,
  `reply_to_msg_id` bigint(20) DEFAULT NULL,
  `is_channel` tinyint(1) DEFAULT NULL,
  `is_group` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 169697 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;


-- ----------------------------
-- Table structure for channel
-- ----------------------------
DROP TABLE IF EXISTS `channel`;
CREATE TABLE `channel`  (
  `id` bigint(20) NOT NULL,
  `title` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `username` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `is_channel` tinyint(1) DEFAULT NULL,
  `is_group` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;
```

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

```
python main.py
python main.py --take-fresh
```