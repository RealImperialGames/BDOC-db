# -*- coding: utf-8 -*-
"""package bdocdb.configs
    Created on 01 march 2018
    @author: Netzulo
    @website: https://www.netzulo.com
"""


from bdocdb.configs import settings


SETTINGS = {
   "db_root_pwd": settings.DB_ROOT_PWD,
   "db_root_usr": settings.DB_ROOT_USR,
   "db_service_port": settings.DB_SERVICE_PORT,
   "db_uri_port": settings.DB_URI_PORT,
   "dbs_cfg": settings.DBS_CFG,
   "docker_host": settings.DOCKER_HOST
}


__all__ = ['settings', 'SETTINGS']
