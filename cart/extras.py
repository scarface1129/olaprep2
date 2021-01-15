import random
import string
from datetime import date
import datetime

def genetrate_order_id():
	date_str = date.today().strftime('%y%m%d')[2:]+str(datetime.datetime.now)
	rand_str = ''.join([random.choice(string.digits)for count in range(3)])
	return date_str+rand_str