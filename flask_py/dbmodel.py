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
from flask_login import UserMixin
from sqlalchemy.orm import validates

from flask_py import db


class Exfacer(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    exfac_id = db.Column(db.String(14), unique=True, nullable=False)
    first_name = db.Column(db.String(100), nullable=False)


    def __repr__(self):
        return f"Exfacer(Exfac ID: '{self.exfac_id}')"


    @classmethod
    def get_by_email_address(cls, email_address):
        return (
            ExfacerBasicInfo.query
                .filter_by(email_address=email_address)
                .first()
        )
        
        
    @classmethod
    def get_by_exfac_id(cls, exfac_id):
        return cls.query.filter_by(exfac_id=exfac_id).first()
    
    
    @validates("email_address")
    def validate_email(self, email_address):
        assert "@" in email_address, "Invalid email address"
        
        return email_address
    
    
    def add(self):
        db.session.add(self)
        db.session.commit()
        
        
    def update(self, firstname):
        self.firstname = firstname
        
        db.session.commit()
        
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()


    # relationships logic
    basic_info = db.relationship(
        "ExfacerBasicInfo", backref="_basic_info", uselist=False
    )


# rest api boilerplate
class ExfacerBasicInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    exfac_id = db.Column(
        db.String(14), db.ForeignKey("exfacer.exfac_id"), unique=True,
        nullable=False,
    )
    username = db.Column(db.String(100), unique=True)
    profile_picture = db.Column(
        db.String(20), default="default.png", nullable=False
    )
    email_address = db.Column(db.String(500), unique=True, nullable=False)
    
    
    def add(self):
        db.session.add(self)
        db.session.commit()
        
        
    def update(self, username, profile_picture, email_address):
        self.username = username
        self.profile_picture = profile_picture
        self.email_address = email_address
        
        db.session.commit()
    
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()


# circular import modules
from flask_py.utils import *
