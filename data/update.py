# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 15:14:36 2018

@author: junbai

This script store functions that modify database
"""

import os
import pandas as pd
import sqlite3
import json
from ..config import (
        DBDIR,
        DB,
        EXCHANGE_TABLE,
        COIN_TABLE,
        PROXIES,
        )
from web_api import (
        get_all_exchanges,
        get_coins_list,
        )


def update_exchanges(proxies=None):
    """
    Pairs are sorted with lower value at front. then they are combined to a single
    string
    """
    exchanges = get_all_exchanges(PROXIES)
       
    with sqlite3.connect(os.path.join(DBDIR, DB)) as conn:
        # wipe clean first and rewrite everything
        conn.execute("delete from %s" % EXCHANGE_TABLE)
        for exchange, pairs in exchanges.iteritems():
            for fsym, tsyms in pairs.iteritems():
                for tsym in tsyms:
                    conn.execute("insert into %s values (?, ?, ?)" % EXCHANGE_TABLE,
                                 (exchange.lower(), "/".join(sorted([fsym, tsym])), "/".join([fsym, tsym])))
            conn.commit()
    return True

def update_coins(proxies=None):
    coins = get_coins_list(proxies=proxies)['Data']
    assert isinstance(coins, dict)
    df = pd.DataFrame.from_dict(coins, 'index')

    with sqlite3.connect(os.path.join(DBDIR, DB)) as conn:
        df.to_sql(COIN_TABLE, conn, 'sqlite', if_exists='replace')
    return True