from utils import Utils
import csv
import json
import yfinance as yf
import pandas as pd
import numpy as np


obj = Utils()
DATA_FILE = 'data.json'


def get_share_data(sname):
	data = yf.download(tickers=sname, period="1d", interval="1m")
	return data


def read_data (path= DATA_FILE):
	'''This function read data from given csv file'''
	with open(path) as f:
		data = json.load(f)
		return data

def calculate_dividend():
	data = read_data()

	result = []
	if not data:
		return ("\n Data does not exists in given file!!! \n")

	for d in data:
		if d.get('type') == 'COMMON':
			common_div = obj.common_dividend(d.get('lastDividend'),d.get('marketPrice'))
			d['dividend'] = common_div
			result.append(d)
			
		if d.get('type') == 'PREFERRED':
			pref_div = obj.preferred_dividend(d.get('fixedDividend'),d.get('parValue'), d.get('marketPrice'))
			d['dividend'] = pref_div
			result.append(d)

	return (result)

def calculate_pe_ratio():
	result = []

	data = calculate_dividend()
	for d in data:
		pe = obj.pe_ratio(d.get('marketPrice'), d.get('dividend'))
		# obj.pe_ratio()
		d['peRatio'] = pe
		result.append(d)

	return result


def geo_metric_mean():
	data = calculate_pe_ratio()
	result = []
	market_price = []
	for d in data:
		market_price.append(d.get('marketPrice'))
	geo_metric = obj.geometric_mean(market_price)
	data.append({'GeometricMean': geo_metric})

	with open('result.json', 'w') as fp:
		json.dump(data, fp, indent=4)

def vwsp(scrit_code = 'AAPL'):	
	df = get_share_data(scrit_code)
	
	df['price'] = (df.Open+df.High + df.Close)/3
	df['vwap'] = (np.cumsum(df.Volume * df.price) / np.cumsum(df.Volume))
	print(df.to_markdown())


if __name__ == '__main__':
	geo_metric_mean()
	print ('\n ******Calculate Volume Weighted Stock Price based on trades ********\n')
	vwsp()
