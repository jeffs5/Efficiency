
def summation(start_value, number_to_buy):

	control = 1
	final_value = start_value
	last_value = start_value

	while number_to_buy > control:
		final_value += last_value * 1.3
		last_value = last_value * 1.3
		control += 1

	return final_value