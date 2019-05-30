from telethon.sync import TelegramClient
from telethon import functions, types
import socks
import random
from TelegramSpider import fetch

from TelegramSpider.client import client

def crawl_contact():
    contact_result = client(functions.contacts.GetContactsRequest(hash=0))
    user_list = contact_result.users
    for user in user_list:
        fetch.fetch_user(user)

def run():
    crawl_contact()

if __name__ == '__main__':
    crawl_contact()
