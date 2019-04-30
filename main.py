import sys
import os
import getopt
from TelegramSpider.crawler import message_crawler
import settings

project_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_dir)

def print_usage():
    print(
"""
USAGE: 
    python main.py
    python main.py --take-fresh""")

if len(sys.argv) > 1:
    try:
        options, args = getopt.getopt(sys.argv[1:], "", ["take-fresh"])
        for name, value in options:
            if name in ("--take-fresh"):
                settings.TAKE_FRESH_MESSAGE = True
            else:
                raise RuntimeError()
    except:
        print_usage()
        exit(1)

message_crawler.run()
