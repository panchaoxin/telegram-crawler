# -*- coding: utf-8 -*-

import TelegramSpider.database as db
import datetime
import pytz
tz = pytz.timezone('Asia/Shanghai')


cursor = db.connection.cursor()

"""
    common
"""
def get_max_message_id_of_chat(chat_id):
    sql = """
        SELECT MAX(message_id) AS m FROM message WHERE chat_id = %s
    """ % chat_id
    cursor.execute(sql)
    r = cursor.fetchone()
    return r["m"]


def process_value(value):
    if isinstance(value, bool):
        ## return 1 if value else 0
        return value

    if isinstance(value, str):
        if value == "None":
            return ""
        else:
            return value.strip()

    if isinstance(value, datetime.datetime):
        # utc转东8区时间
        value = (value + datetime.timedelta(hours=8))
        return value

    return value


def get_save_sql(item, table_name):
    keys = item.keys()
    fields = ','.join(keys)
    placeholders = ','.join(['%s'] * len(keys))
    sql = 'INSERT INTO %s (%s) VALUES (%s)' % (table_name, fields, placeholders)
    return sql


"""
    user
"""


def get_user(item):
    sql = 'SELECT id FROM user WHERE id=%s' % item['id']
    cursor.execute(sql)
    return cursor.fetchone()


def save_user(item):
    sql = get_save_sql(item, "user")
    values = tuple(item.values())
    cursor.execute(sql, tuple(process_value(i) for i in values))
    return db.connection.commit()


def process_user(item):
    exist = get_user(item)
    if not exist:
        try:
            save_user(item)
        except Exception as e:
            print(item)
            print(e)


"""
    channel
"""


def get_channel(item):
    sql = 'SELECT id FROM channel WHERE id=%s' % item['id']
    cursor.execute(sql)
    return cursor.fetchone()


def save_channel(item):
    sql = get_save_sql(item, "channel")
    values = tuple(item.values())
    cursor.execute(sql, tuple(process_value(i) for i in values))
    return db.connection.commit()

def update_channel(item):
    item_id = item.pop('id')
    keys = item.keys()
    values = list(item.values())
    values.append(item_id)
    fields = ['%s=' % i + '%s' for i in keys]
    sql = 'UPDATE channel SET %s WHERE id=%s' % (','.join(fields), '%s')
    cursor.execute(sql, values)
    return db.connection.commit()

def process_channel(item):
    exist = get_channel(item)
    if not exist:
        try:
            save_channel(item)
        except Exception as e:
            print(item)
            print(e)
    else:
        update_channel(item)

"""
    message
"""


def get_message(item):
    sql = 'SELECT id FROM message WHERE message_id=%s AND chat_id=%s' % (item['message_id'], item['chat_id'])
    cursor.execute(sql)
    return cursor.fetchone()


def save_message(item):
    sql = get_save_sql(item, "message")
    values = tuple(item.values())
    cursor.execute(sql, tuple(process_value(i) for i in values))
    return db.connection.commit()

def update_message(item):
    message_id, chat_id = item.pop('message_id'), item.pop('chat_id')
    keys = item.keys()
    values = list(item.values())

    values.append(message_id)
    values.append(chat_id)

    fields = ['%s=' % i + '%s' for i in keys]
    sql = 'UPDATE message SET %s WHERE message_id=%s AND chat_id=%s' % (','.join(fields), "%s", "%s")
    cursor.execute(sql, values)
    return db.connection.commit()

def process_message(item):
    exist = get_message(item)
    if not exist:
        try:
            save_message(item)
        except Exception as e:
            print(item)
            print(e)
    else:
        update_message(item)