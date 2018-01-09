# -*- coding: utf-8 -*-
"""
Created on Mon Jan 08 20:00:17 2018
@author: Jimmy
This script test differenct cryptocurrency data API
"""
import requests
import json

# Bitfinex data API
#from CryptoCoinChartsApi import API
#api = API()
#list_ = api.listofpairs()

# CryptoCompare API
exchanges = ['bitfinex', 'bitstamp', 'coinbase', 'kraken', 'bittrex', 'poloniex', 'gemini']
coins = ['ETH', 'BTC',]
currencies = ['USD', 'EUR', 'JPY']
API = {
    "base": "https://min-api.cryptocompare.com/",
    "coinlist": "https://www.cryptocompare.com/api/data/coinlist/",
    "price": "https://min-api.cryptocompare.com/data/price?fsym=%s&tsyms=%s&e=%s",
    "exchange": "https://min-api.cryptocompare.com/data/all/exchanges",
        }
PROXIES = {
        'http': 
        }


def get_coins_list(proxies=None):
    """
    Get all traded coins in the market
    """
    with requests.Session() as session:
        r = session.get(API["coinlist"], proxies=proxies)
        result = json.loads(r.text)
    return result


def get_all_exchanges(proxies=None):
    """
    Get information of all exchanges
    """
    with requests.Session() as session:
        r = session.get(API['exchange'], proxies=proxies)
        result = json.loads(r.txt)
    return result

    
def get_live(fsym, tsyms, exch, proxies=None):
    """
    Get live data for pairs
    """
    to_symbols = ",".join(tsyms) if type(tsyms) == type([]) else tsyms
    url = API["price"] % (fsym.upper(), to_symbols.upper(), exch)
    with requests.Session() as session:
        r = session.get(url, proxies=proxies)
        result = json.loads(r.text)
    return result
