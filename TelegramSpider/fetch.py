from TelegramSpider.client import client
from TelegramSpider import pipelines
import os

def fetch_user(user):
    try:
        avatar_file = client.download_profile_photo(entity=user, file='avatar/{}.jpg'.format(user.id),
                                                    download_big=False)
        avatar_file = os.path.basename(avatar_file)
    except:
        avatar_file = ''

    item = {
        'id': user.id,
        'username': user.username,
        'photo': avatar_file,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'phone': user.phone,
    }

    print("[DEBUG] [USER] ==> ", item)
    pipelines.process_user(item)