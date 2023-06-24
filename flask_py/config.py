#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Flask.py Boilerplate


__author__ = "OTechCup"
__copyright__ = f"Copyright 2023 - datetime.utcnow().year, {__author__}"
__credits__ = ["Mr. O"]
__version__ = "config('FLASK_PY_VERSION', cast=float)"
__maintainer__ = __author__
__email__ = "support@exfac.info"
__status__ = "config('FLASK_PY_ENVIRONMENT_STATUS', cast=str)"


# import modules
from decouple import config
import sshtunnel

from datetime import timedelta


class Config:
    # secret key
    SECRET_KEY = config("FLASK_PY_SECRET_KEY", cast=str)

    # jwt setting
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=15)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
    PROPAGATE_EXCEPTIONS = True
    
    # mail
    MAIL_SERVER = "smtp.mail.yahoo.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "noreply@exfac.info"
    MAIL_PASSWORD = config("EXFAC_NOREPLY_EMAIL_PASSWORD", cast=str)
    
    # only accept requests that are up to 1MB in size
    MAX_CONTENT_LENGTH = 1 * 1024 * 1024

    # session
    SESSION_TYPE = "sqlalchemy"
    SESSION_USE_SIGNER = True
    SESSION_SQLALCHEMY_TABLE = "ExfacProductSession"
    SESSION_PERMANENT = True


class DevConfig(Config):
    def db_uri(connection_type: str) -> str:
        if connection_type == "ssh_tunnel":
            # remote db server (rds) ssh tunnel
            rds_ssh_tunnel = sshtunnel.SSHTunnelForwarder(
                ssh_hostname=("ssh.pythonanywhere.com"),
                ssh_username="exfac_inc",
                ssh_password=config("HOST_ACCOUNT_PASSWORD", cast=str),
                remote_bind_address=(
                    "exfac_inc.mysql.pythonanywhere-services.com", 3306
                ),
            )
            
            uri = (
                "{dialect}+{driver}://{username}:{password}@{hostname}:{port}/{dbname}".format(
                    dialect="mysql",
                    driver="pymysql",
                    username="exfac_inc",
                    password=config("FLASK_PY_DATABASE_PASSWORD", cast=str),
                    hostname="127.0.0.1",
                    port=rds_ssh_tunnel.local_bind_port,
                    dbname="exfac_inc$ExfacDataStore",
                )
            )
        else:
            uri = "{dialect}:///{file_path}/{dbname}.db?{query}".format(
                dialect="sqlite",
                file_path="db",
                dbname="ExfacDataStore",
                query="charset=utf8mb4",
            )
        
        return uri
    
        
    DEBUG = True
    
    # db
    SQLALCHEMY_DATABASE_URI = db_uri("sqlite")
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True


class ProdConfig(Config):
    DEBUG = False
    
    # db
    SQLALCHEMY_DATABASE_URI = (
        "{dialect}+{driver}://{username}:{password}@{hostname}:{port}/{dbname}?{query}".format(
            dialect="mysql",
            driver="pymysql",
            username="exfac_inc_api",
            password=config("FLASK_PY_DATABASE_PASSWORD", cast=str),
            hostname="mysql1004.mochahost.com",
            port="3306",
            dbname="exfac_inc_ExfacDataStore",
            query="charset=utf8mb4",
        )
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'connect_args': {
            'connect_timeout': 60,
        },
        'pool_pre_ping': True,
        'pool_size' : 100,
        'pool_recycle': 3600,  # 1 hour 300
    }


class TestConfig(Config):
    DEBUG = True
    TESTING = True
    