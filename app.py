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

from flask_py import create_flask_py_app, db
from flask_py.dbmodel import *
from flask_py.config import *


# Set the appropriate config based on the environment settings
configs = {
    'development': DevConfig,
    'testing': TestConfig,
    'production': ProdConfig,
}
env = config("FLASK_PY_ENVIRONMENT_STATUS", cast=str).lower()
use_config = configs[env]
flask_py_app = create_flask_py_app(use_config)


@flask_py_app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
    }


if __name__ == "__main__":
    flask_py_app.run(debug=False)
