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

from data import (
    get_live,
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


def get_exchanges_by_pair(fsym, tsym):
    """
    Find out all exchanges trading the pair
    :return: list of exchanges
    """
    fsym = fsym.upper()
    tsym = tsym.upper()
    with sqlite3.connect(os.path.join(DBDIR, DB)) as conn:
        df = pd.read_sql_query("select exchange, pair from %s where _pair='%s'" % (EXCHANGE_TABLE, "/".join(sorted([fsym, tsym]))),
                               conn)
    if not df.empty:
        return df
    else:
        return None


def get_pair_prices(fsym, tsym, proxies=None):
    """
    Get all prices of a pair across exchanges
    :return: DataFrame of prices of a pair across exchanges
    """
    df = get_exchanges_by_pair(fsym, tsym)
    prices = list()
    for i in range(len(df)):
        frm, to = df['pair'][i].split('/')
        exch = df['exchange'][i]
        prices.append(get_live(str(frm), str(to), str(exch), proxies))
    df['last'] = prices
    return df


def get_coin_info(coin):
    """
    Get information of a coin from database
    :param coin: abbreviation of a cryptocurrency
    :return: DataFrame
    """
    with sqlite3.connect(os.path.join(DBDIR, DB)) as conn:
        df = pd.read_sql_query("select * from %s where [index] = '%s'" % (COIN_TABLE, coin.upper()), conn)
    return df




