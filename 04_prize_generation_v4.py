# edited odds, increased trials and just showed stats.

import random

NUM_TRIALS = 100
winnings = 0

cost = NUM_TRIALS * 5

gold = 5
silver = 2
copper = 1
lead = 0

for item in range(0, NUM_TRIALS):
    # prize = ""
    round_winnings = 0

    for thing in range(0, 3):

        # randint finds number between given endpoints, including both endpoints
        prize_num = random.randint(1, 10)
        # prize += " "
        if prize_num == 1:
            # one in ten chance of getting gold
            # prize += "gold"
            round_winnings += 5
        elif 1 < prize_num <= 3:
            # get silver if it's a 2 or 3
            # prize += "silver"
            round_winnings += 2
        elif 3 < prize_num <= 7:
            # copper if its 4, 5, 6, 7 <40% chance of copper>
            # prize += "copper"
            round_winnings += 1
        '''else:
            round_winnings += lead'''

    winnings += round_winnings

print("Paid in: ${}".format(cost))
print("Pay out ${}".format(winnings))

if winnings > cost:
    print("You came out ${} ahead".format(winnings - cost))
else:
    print("Sorry, you lost ${}".format(cost - winnings))