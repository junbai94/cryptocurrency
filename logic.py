# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 16:13:08 2018

@author: junbai

This script retrieve data from database
"""

import pandas as pd
import json
import sqlite3


from config import (
        DB_FULL_PATH,
        EXCHANGE_TABLE,
        )


def is_traded(fsym, tsym, exch):
    """
    Check if a pair is traded on an given exchange
    :return: the a string of traded pair or None
    """
    fsym = fsym.upper()
    tsym = tsym.upper()
    with sqlite3.connect(DB_FULL_PATH) as conn:
        df = pd.read_sql_query("select * from %s where exchange='%s' and _pair='%s'"%(EXCHANGE_TABLE, exch.lower(), "/".join(sorted([fsym, tsym]))), conn)

    if not df.empty:
        return df['pair'][0]
    else:
        return None





