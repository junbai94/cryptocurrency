# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 16:13:08 2018

@author: junbai

This script retrieve data from database
"""

import pandas as pd
import json
import sqlite3
import os

from data_api import (
    get_live,
)

from config import (
        DBDIR,
        DB,
        DB,
        EXCHANGE_TABLE,
        COIN_TABLE,
        )

def is_traded(fsym, tsym, exch):
    """
    Check if a pair is traded on a given exchange
    :return: Boolean
    """
    list1, list2 = list(), list()
    with sqlite3.connect(os.path.join(DBDIR, DB)) as conn:
        df1 = pd.read_sql_query("select * from %s where exchange='%s' and fsym='%s'" % (EXCHANGE_TABLE, exch.lower(), fsym.upper()),
                               conn)
        df2 = pd.read_sql_query("select * from %s where exchange='%s' and fsym='%s'" % (EXCHANGE_TABLE, exch.lower(), tsym.upper()),
                               conn)
    if not df1.empty:
        list1 = json.loads(df1['tsyms'][0])
    if not df2.empty:
        list2 = json.loads(df2['tsyms'][0])

    return (tsym in list1) or (fsym in list2)


def _two_exchange_pair(fsym, tsym, fex, tex):
    """
    Detect arbitrage opportunity for one pair across two exchanges
    :param fsym: from this crypto
    :param tsym: to this crypto
    :param fex: from this exchange
    :param tex: to this exchange
    :return: Tuple. (Boolean, arbitrage)
    """
    # check if pair is traded on both exchanges
    if not is_traded(fsym, tsym, fex) or not is_traded(fsym, tsym, tex):
        return False, 0


