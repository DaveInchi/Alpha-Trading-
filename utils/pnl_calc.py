import json
import requests
from utils.hystory_data_loader import get_hystory_data

def calc_pnl(stock_data_day, ent_p, num_of_shares):
    pnl = (stock_data_day - ent_p) * num_of_shares

    return pnl

