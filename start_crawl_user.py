import sys
import os
import getopt
from TelegramSpider.crawler import user_crawler
import settings

project_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_dir)

user_crawler.run()