# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 16:13:08 2018

@author: junbai

This script retrieve data from database
"""

import os
import sqlite3
import pandas as pd
import json

from config import (
        DBDIR,
        DB,
        EXCHANGE_TABLE,
        COIN_TABLE,
        )


def get_exchange(exchange):
    """
    Get all traded pairs of an exchange
    :return: a pandas DataFrame
    """
    with sqlite3.connect(os.path.join(DBDIR, DB)) as conn:
        df = pd.read_sql_query("select * from %s where exchange = '%s'" % (EXCHANGE_TABLE, exchange.lower()),
                          conn)
    return df


def get_exchanges(*exchanges):
    """
    Get all traded pairs for multiple exchanges
    :return: a dictionary of pandas DataFrame
    """
    result = dict()
    for exchange in exchanges:
        result[result] = get_exchange(exchange)
    return result


def get_coin(coin):
    """
    Get information of a coin from database
    :param coin: abbreviation of a cryptocurrency
    :return: DataFrame
    """
    with sqlite3.connect(os.path.join(DBDIR, DB)) as conn:
        df = pd.read_sql_query("select * from %s where [index] = '%s'" % (COIN_TABLE, coin.upper()), conn)
    return df

