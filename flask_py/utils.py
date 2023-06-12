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
from flask_restx import fields

from flask_py import login_manager
from flask_py.dbmodel import Exfacer


# exfacer loader
@login_manager.user_loader
def load_smartest(exfac_id):
    return Exfacer.query.get(str(exfac_id))


# rest api boilerplate
class NullableString(fields.String):
    __schema_type__ = ["string", "null"]
