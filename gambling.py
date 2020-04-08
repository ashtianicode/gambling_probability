from decimal import Decimal 
import math
from  statistics import mean
import matplotlib.pyplot as plt

fig,ax = plt.subplots()


def nCr(n,r):
	f = math.factorial 
	return f(n)/ (f(r)*f(n-r))

def gamble_odds(prediction,investing_value=1000.0000,number_of_bets=1000):    
		bet_value = investing_value / number_of_bets
		win_odds = ((100 - prediction) -1)/100.0000
		win_multiply = round((1.0000/win_odds) * 0.99, 2)
		win_reward_value = (win_multiply*bet_value) 
		
		required_wins = int(investing_value // win_reward_value)  #=>  for $100 and 100 bets: $100 / (1.5X * $0.01)
		max_profit = (number_of_bets * win_reward_value )/ investing_value

		cumulative_batter_than_break_even_prob =  0
		break_even_prob = nCr(number_of_bets,required_wins) * (win_odds**required_wins)*((1-win_odds)**(number_of_bets-required_wins))
		
		# returns_of_scenarios = []
		num_wins_scenarios = [w for w in range(0,number_of_bets )]
		# the range was starating from required_wins before. but lets have the whole thing
		for wins in num_wins_scenarios:
				win_num_prob = nCr(number_of_bets,wins) * (win_odds**wins)*((1-win_odds)**(number_of_bets-wins))
				# return_of_this_num_of_WINS = (wins* win_reward_value ) # we have $50 for 10 bets. reward is 1.5X => "$5*1.5 = $7.5 on winning bet"  from [6 min required wins from 10 ] we're at 8 for example. now: 8 wins * probability of winning 8 times * reward value => ex: 8wins * %42 * $7.5 = $25.2 return
				# return_of_this_num_of_WINS_with_prob = return_of_this_num_of_WINS * win_num_prob 
				# returns_of_scenarios.append(	return_of_this_num_of_WINS_with_prob)
				if wins > required_wins:
					cumulative_batter_than_break_even_prob += win_num_prob
		
		
		# bionomila E[X] = np  =>   expected value of wins = number_of_bets * win_odds
		expected_value_of_wins = number_of_bets * win_odds
		return_of_bet_package  = expected_value_of_wins * win_reward_value
		#APPT => average profitability per trade package 
		APPT = return_of_bet_package - investing_value   

		if APPT > 0:
			print(" predition: ",prediction,'max_profit: $',max_profit*investing_value," -- win_odds: %",win_odds*100," -- win_multiply: X",win_multiply)
			print("cumulative_better_than_break_even: ",cumulative_batter_than_break_even_prob)
			print("Expected Profit: $",APPT)
			print('\n\n')
		

			

		return cumulative_batter_than_break_even_prob , break_even_prob
   

# number_of_bets = [ b for b in range(0,10,2)][1:]
number_of_bets = [ 1 , 10, 100, 1000]
investing_value = [ v*1.0000 for v in range(1,10)]


for b in number_of_bets:
	preditions = []
	odds = []
	for p in range(1,98):
		preditions.append(p)    
		cumulative_batter_than_break_even_prob , break_even_prob = gamble_odds(p,number_of_bets=b)
		odds.append(cumulative_batter_than_break_even_prob)
	ax.scatter(preditions,odds, label = b)

ax.legend()
plt.show()
