
# -*- coding: utf-8 -*-
"""SETTINGS for module scripts

python bdodb.py --help

"""


MSG_UNKOWN_COMMAND = "Unknown command : {}"

DOCKER_HOST = "tcp://192.168.99.100:2376"
DB_IP = "192.168.99.100"
DB_SERVICE_PORT = 2376
DB_URI_PORT = 27018
DB_ROOT_USR = "root"
DB_ROOT_PWD = "1bdo@admin.2"
DBS_CFG = [
    {
        "database_name": "loginserver",
        "database_usr": "admin",
        "database_pwd": "1bdo@admin.2"
    },
    {
        "database_name": "gameserver",
        "database_usr": "admin",
        "database_pwd": "1bdo@admin.2"
    }
]
