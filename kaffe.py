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


# The queue length at each time interval (start at 0 for time 0)
queue = [0]
people = 96  # number of people on each floor
# How many cups of coffee does the average person drink in the morning?
cups = 4
