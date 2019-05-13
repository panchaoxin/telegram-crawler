from telethon.sync import TelegramClient
from telethon import functions, types
import socks
import random
from TelegramSpider import pipelines, database as db
from TelegramSpider.client import client

cursor = db.connection.cursor()

def download_photo_by_user_id(client, user_id):
    """
    client.download_profile_photo
        参考文档
            https://docs.telethon.dev/en/latest/modules/client.html#telethon.client.downloads.DownloadMethods.download_profile_photo
        参数
            entity: 群组或者用户
            file: 自定义下载文件名，
            download_big: 是否下载大头像
        返回值
            下载得到的文件名，None代表没有头像

        entity找不到，则抛出异常
    """

    try:
        filename = client.download_profile_photo(entity=user_id, file='avatar/{}.jpg'.format(user_id), download_big=False)
    except:
        filename = None
    # print("[DEBUG] {} has photo: {}".format(user_id, filename))
    return filename


def crawl_user_info(client, userid_list):
    for userid in userid_list:
        item = {
            'id': userid,
            'username': '',
            'photo': '',
            'first_name': '',
            'last_name': '',
            'phone': '',
        }

        try:
            user = client.get_entity(userid)
        except:
            user = None

        if user:
            item['username'] = user.username
            item['photo'] = download_photo_by_user_id(client, userid)
            item['first_name'] = user.first_name
            item['last_name'] = user.last_name
            item['phone'] = user.phone

        print("[DEBUG] [user] ==> ", item)
        pipelines.process_user(item)

def run():
    sql = """
        SELECT DISTINCT(from_id) AS id FROM message
        WHERE from_id NOT IN (SELECT DISTINCT(id) FROM user)
    """
    cursor.execute(sql)
    item_list = cursor.fetchall()
    userid_list = [item['id'] for item in item_list]
    crawl_user_info(client, userid_list)
