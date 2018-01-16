# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 16:14:56 2018

@author: junbai

Config file
"""

import os

# directories
BASEDIR = os.path.dirname(os.path.abspath(__file__))
DBDIR = os.path.join(BASEDIR, 'data')

# database name
DB = 'data.db'
DB_FULL_PATH = os.path.join(DBDIR, DB)

# table names
EXCHANGE_TABLE = 'exchanges'
COIN_TABLE = 'coins'

# proxies
PROXIES = {
        'http': 'http://j291414:TerranForce1!@10.252.22.102:4200',
        'https': 'https://j291414:TerranForce1!@10.252.22.102:4200',
        }
