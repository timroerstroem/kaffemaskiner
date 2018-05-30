"""Simulating the queue at the coffee machine.

The simulation will run over three hours (0700-1000). These hours
should be the busiest in terms of coffee.

Assumptions:
    - Regardless of what is being served, the coffee machine takes
        45 s to make it.
    - People will not go to a different floor to use a coffee machine.
    - Simulation will use timesteps of 15 s (i.e. it takes 3 steps to
        make coffee).
"""

import statistics as stat
import random


# The number of ticks to run the simulation (3 h * 60 min/h * 4 ticks/min)
stop = 3 * 60 * 4
# The queue length at each time interval (start at 0 for time 0)
queue = [0]
people = 96  # number of people on each floor
# How many cups of coffee does the average person drink in the morning?
cups = 3
# Probability of a person getting a cup of coffee at any given tick
pCoffee = cups / stop
timeToCoffee = 0
t = 1


while t < stop:
    if timeToCoffee > 0:
        timeToCoffee -= 1

    if queue[t-1] > 0 and timeToCoffee == 0:
        # Someone was waiting in line and the coffee machine is free
        queue[t] = queue[t-1] - 1
        timeToCoffee = 3

    if len(queue) == t:
        queue[t] = queue[t-1]

    # See if anyone wants coffee
    if random.random() < people * pCoffee:
        # One person has decided to get coffee, check if the machine is free
        if queue[t] == 0 and timeToCoffee == 0:
            timeToCoffee = 3
        else:
            queue[t] += 1

    t += 1
