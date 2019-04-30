# -*- coding: utf-8 -*-

from telethon import TelegramClient, sync
from TelegramSpider import pipelines, database as db
from TelegramSpider.client import client
import telethon
import settings

cursor = db.connection.cursor()

def fetch_one_message(msg):
    """
    Process and fetch a message
    :param msg:
    :return:
    """

    # Empty messages are not accepted
    if not msg.message:
        return

    item = {
        "message_id": msg.id,    # Message id of current chat
        "chat_id": msg.chat.id,  # ID of current chat
        "is_out": msg.out,      # Whether the message is outgoing (i.e. you sent it from another session) or incoming (i.e. someone else sent it).
        "is_mentioned": msg.mentioned,   # Whether you were mentioned in this message or not. Note that replies to your own messages also count as mentions
        "message": msg.message,    # message content
        "date": msg.date,
        "from_id": msg.from_id,    # The ID of the user who sent this message
        "is_reply": msg.is_reply,           # True if the message is a reply to some other
        "reply_to_msg_id": msg.reply_to_msg_id,    # The ID to which this message is replying to, if any
        "is_channel": msg.is_channel,
        "is_group": msg.is_group,
    }

    print("(DEBUG) GET MESSAGE: ", item)
    pipelines.process_message(item)




def fetch_all_user_message(client):
    sql = """
        SELECT * FROM user
    """
    cursor.execute(sql)
    user_list = cursor.fetchall()

    for user in user_list:
        for msg in client.iter_messages(user["id"]):
            fetch_one_message(msg)


def fetch_channel(entity, is_group):
    """
    Process and fetch a channel
    :param msg:
    :return:
    """
    item = {
        "id": entity.id,
        "title": entity.title,
        "username": entity.username,
        "is_group": is_group
    }
    print("(DEBUG) GET CHANNEL: ", item)
    pipelines.process_channel(item)


def fetch_all_group_message(client):
    dialog_list = client.get_dialogs()
    for dialog in dialog_list:
        entity = client.get_entity(dialog.title)
        if isinstance(entity, telethon.tl.types.Channel) and dialog.is_group:
            fetch_channel(entity, dialog.is_group)

            if settings.TAKE_FRESH_MESSAGE:
                max_message_id = pipelines.get_max_message_id_of_chat(entity.id) or 0
            else:
                max_message_id = 0
            print("(DEBUG) max_message_id of %s = %s" % (entity.title, max_message_id))
            for msg in client.iter_messages(entity.id, min_id=max_message_id):
                fetch_one_message(msg)

def run():
    fetch_all_group_message(client)
