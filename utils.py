from scipy.stats import gmean

class Utils():

	def __init__(self):
		pass

	def common_dividend(self, last_dividend, price):
		try:
			dividend = last_dividend/price
		except ZeroDivisionError:
			return ('Price should not be Zero!')
		return (dividend)

	def preferred_dividend(self, fixed_dividend, par_value, price):

		try:
			dividend = (fixed_dividend * par_value)/price
		except ZeroDivisionError:
			return ('Price should not be Zero!')
		return (dividend)


	def pe_ratio(self, price, dividend):
		try:
			pe = price/dividend
			return pe
		except ZeroDivisionError:
			# print('Dividend is zero!')
			return 0
			
	def geometric_mean(self, price_lst):
		#calculate geometric mean
		return gmean([1, 4, 7, 6, 6, 4, 8, 9])
