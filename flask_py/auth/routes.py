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
from flask_restx import Namespace
from flask import Blueprint


auth = Blueprint("auth", __name__)


# rest api boilerplate
auth = Namespace(
    name="auth",
    description="Exfacer authentication namespace",
    path="/v1/auth",
)


# circular import modules
from .sign_in import *
