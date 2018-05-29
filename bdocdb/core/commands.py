# -*- coding: utf-8 -*-
"""package bdocdb.core.commands
    Created on 01 march 2018
    @author: Netzulo
    @website: https://www.netzulo.com
"""


import os
import telnetlib
import pymongo
from bdoccore.commands import Command
from bdocdb.configs import SETTINGS


class CommandModule(Command):

    def install(self):
        """Installation process
        1. Start at background the file docker-compose.yml
        2. Connect to mongoDB, create users from SETTINGS
        3. Verify connection for each DB_USER created
        4. You can stop container with: 'docker stop ID_CONTAINER'
        """
        self.logger.info('Installing BDOC-db: ...')
        # 1. Start at background the file docker-compose.yml
        self.start(is_shell=False)
        # 2. Connect to mongoDB, create users from SETTINGS
        for db_config in SETTINGS.DBS_CFG:
            conn = self.db_connection(
                SETTINGS.DB_IP,
                SETTINGS.DB_URI_PORT,
                SETTINGS.DB_ROOT_USR,
                SETTINGS.DB_ROOT_PWD
            )
            self.db_create_user(conn, **db_config)
        # TODO: 3. Verify connection for each DB_USER created
        # TODO: 4. You can stop container with: 'docker stop ID_CONTAINER'
        self.logger.info('Installing BDOC-db: DONE')

    def start(self, is_shell=True):
        """Start process
        1. Start at background the file docker-compose.yml
            'docker-compose -f bdocdb/data/docker/docker-compose.yml up'
        """
        self.check_prerequisites()
        self.execute([
            "docker-compose",
            "-f",
            "bdocdb/data/docker/docker-compose.yml",
            "up",
            "-d"
        ], shell=is_shell)

    def check_prerequisites(self):
        """Check if environment variable it's setted for DOCKER_HOST
            name at system PATH environ variable
        """
        self.logger.info('check_prerequisites BDOC-db: ...')
        docker_host = os.environ.get('DOCKER_HOST')
        self.logger.debug("  os.environ['DOCKER_HOST']={}".format(docker_host))
        if not docker_host:
            raise Exception("Environment var not found for name : DOCKER_HOST")
        if docker_host != SETTINGS.DOCKER_HOST:
            raise Exception(
                ("Environment var found value it's invalid, "
                 "try to change DOCKER_HOST value to: "
                 "{}".format(SETTINGS.DOCKER_HOST)
                 )
            )
        self.logger.debug("  DOCKER_HOST, using default value={}".format(
            SETTINGS.DOCKER_HOST))
        self.docker_host = docker_host
        self.logger.info('check_prerequisites BDOC-db: DONE')
        # 2. hacer telnet a DOCKER_HOST:PORT para ver si esta encendido
        telnet_response = telnetlib.Telnet(
            host=SETTINGS.DB_IP, port=SETTINGS.DB_SERVICE_PORT)
        if not isinstance(telnet_response, telnetlib.Telnet):
            raise Exception(
                ("Telnet fails at try to connec to: "
                 ""
                 "DB_IP={} DB_SERVICE_PORT={}").format(
                     SETTINGS.DB_IP,
                     SETTINGS.DB_SERVICE_PORT)
            )
        self.logger.info("Telnet it's ok")

    def db_connection(self, host, port, usr, pwd, database_name=None):
        self.logger.info('db_connection BDOC-db: ...')
        if not database_name:
            database_name = 'admin'
        conn = pymongo.MongoClient(
            host=host,
            port=port,
            username=usr,
            password=pwd,
            authSource=database_name)
        self.logger.info('db_connection BDOC-db: DONE')
        return conn

    def db_create_user(self, connection, **kwargs):
        self.logger.info('db_create_user BDOC-db: ...')
        if not kwargs.get('database_name'):
            raise Exception("Bad optional param: kwargs.database_name")
        db_name = kwargs.get('database_name')
        if not kwargs.get('database_usr'):
            raise Exception("Bad optional param: kwargs.database_usr")
        db_usr = kwargs.get('database_usr')
        if not kwargs.get('database_pwd'):
            raise Exception("Bad optional param: kwargs.database_pwd")
        db_pwd = kwargs.get('database_pwd')
        # start
        db = connection[db_name]
        default_roles = ["readWrite"]
        self.logger.debug('    command=createUser')
        self.logger.debug('    db_usr={}'.format(db_usr))
        self.logger.debug('    db_pwd={}'.format(db_pwd))
        self.logger.debug('    db_roles={}'.format(str(default_roles)))
        try:
            db.command(
                "createUser",
                db_usr,
                pwd=db_pwd,
                roles=default_roles)
        except pymongo.errors.DuplicateKeyError as err:
            self.logger.warning('Mongodb message={}'.format(str(err)))
        self.logger.info('db_create_user BDOC-db: DONE')
