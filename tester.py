# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 17:22:55 2018

@author: j291414

A tester
"""
import sys
sys.path.append("C:/Users/j291414/my algorithms/learning")

import cryptocurrency as cc
import os
sys.modules[cc] = None
reload(cc)

proxies = cc.PROXIES
path = os.path.join(cc.DBDIR, cc.DB)

