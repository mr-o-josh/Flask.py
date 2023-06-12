#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Bite Express App


__author__ = "PhoenixITng"
__copyright__ = "Copyright 2023 - datetime.utcnow().year, {}".format(__author__)
__credits__ = ["Mr. O"]
__version__ = "os.environ.get('BITE_EXPRESS_VERSION')"
__maintainer__ = __author__
__email__ = "support@bitexpress.ng"
__status__ = "os.environ.get('BITE_EXPRESS_ENVIRONMENT_STATUS')"


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
