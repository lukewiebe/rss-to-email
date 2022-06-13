# time_check.py
# Input: a time in Python time notation
# Output: True if less than a day old, false otherwise

import time

# Grab the time and convert to Unix time
current_time = time.localtime()
current_time = time.mktime(current_time)

def is_this_less_than_a_day_old(published_time):
	# Reformat to Unix time
	published_time = time.mktime(published_time)
	
	elapsed_time = current_time - published_time

	if elapsed_time >= 86400:
		return False
	else:
		return True
