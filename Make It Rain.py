from helper import summation

investments = {'piggy': 269000, 'mattress': 216000, 'comic': 138000, 'savings': 84800, 'bitcoin': 144000, 'stock': 752000, 'bookie':845000, 'loan':2110000, 'angel':3250000, 'venture': 760000000, 'pork': 12000000000000000000, 'hedge':128000000000000000000, 'invest': 10100000000000000000, 'insider':61500000000000000000, 'subprime':10900000000000000000, 'pyramid': 4530000000000000000, 'hypercube': 8750000000000000000, 'unholy':4940000000000000000, 'honey': 9720000000000000000, 'flash': 30100000000000000000, 'check': 2450000000000000000000, 'upload': 1890000000000000000000, 'software': 3580000000000000000000, 'multi': 12600000000000000000000}
payouts = {'piggy': .5, 'mattress': 1, 'comic': 3, 'savings': 16, 'bitcoin': 50, 'stock': 200, 'bookie':833, 'loan':3050, 'angel':10500, 'venture': 27700, 'pork': 72200, 'hedge':2250000, 'invest':9720000, 'insider':277000000, 'subprime':13300000000, 'pyramid': 55500000000, 'hypercube': 177000000000, 'unholy': 13000000000000, 'honey': 94400000000000, 'flash': 237000000000000, 'check': 12800000000000000, 'upload': 21600000000000000, 'software': 29200000000000000, 'multi': 70700000000000000}
rate = 1320000000000000000
current = 1150000000000000000000
buy = ('piggy',0)

for new_key in investments:
	for key in investments:
		if not new_key is key:
			number_to_buy = 1

			while summation(investments[new_key], number_to_buy) < investments[key]:
				number_to_buy += 1

			if not number_to_buy <= 1:
				number_to_buy -= 1

			if payouts[new_key] * number_to_buy > payouts[key]:
				

				if payouts[new_key] * number_to_buy > payouts[buy[0]] * buy[1]:
					# print "New_key is {0}, key is {1}, number to buy is {2}, new payouts is {3}, buy[1] is {4}".format(new_key, key, number_to_buy, payouts[new_key] * number_to_buy, buy[1])
					buy = (new_key, number_to_buy)


print "Recommended buy: {0} of {1}".format(buy[1], buy[0])
# in seconds
#time_to_buy_seconds = abs(summation(investments[buy[0]], buy[1]) - current)/rate
time_to_buy_seconds = abs(summation(investments[buy[0]], 1) - current)/rate
print "It will take {0} seconds".format(time_to_buy_seconds)

# in minutes
time_to_buy_minutes = time_to_buy_seconds/60
print "That is {0} minutes".format(time_to_buy_minutes)

#in hours
time_to_buy_hours = time_to_buy_minutes/60
print "That is {0} hours".format(time_to_buy_hours)