# -*- coding: utf-8 -*-

import pymysql

MYSQL_HOST = 'localhost'
MYSQL_DB = 'telegram'
MYSQL_USER = 'root'
MYSQL_PASS = '123456'

connection = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER,
                             password=MYSQL_PASS, db=MYSQL_DB,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
