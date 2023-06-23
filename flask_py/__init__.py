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
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restx import Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_session import Session
from flask_login import LoginManager
from flask_mail import Mail
from flask_moment import Moment
import pymysql


db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
sess = Session()
login_manager = LoginManager()
mail = Mail()
moment = Moment()

login_manager.login_view = "auth.sign_in"
login_manager.login_message_category = "info"

pymysql.install_as_MySQLdb()

# rest api boilerplate
jwt_manager = JWTManager()
cors = CORS()
api = Api(
    title="FLASK.py API",
    version="1.0",
    description="My Flask.py Boilerplate",
    doc="/",
)


def create_flask_py_app(config):
    flask_py_app = Flask(__name__)

    flask_py_app.config.from_object(config)
    flask_py_app.config["SESSION_SQLALCHEMY"] = db  # session config

    # initialize extensions
    db.init_app(flask_py_app)
    migrate.init_app(
        flask_py_app, db, render_as_batch=True, compare_type=True
    )
    bcrypt.init_app(flask_py_app)
    sess.init_app(flask_py_app)
    login_manager.init_app(flask_py_app)
    mail.init_app(flask_py_app)
    moment.init_app(flask_py_app)
    
    
    # import blueprints
    from flask_py.auth.routes import auth


    # register blueprints
    flask_py_app.register_blueprint(auth)
    
    # rest api boilerplate
    api.init_app(flask_py_app)
    jwt_manager.init_app(flask_py_app)
    cors.init_app(flask_py_app)


    # import namespaces
    from flask_py.auth.routes import auth


    # register namespaces
    api.add_namespace(auth)

    return flask_py_app
