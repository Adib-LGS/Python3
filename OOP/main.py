from gc import get_stats
from os.path import split
import os

from model.basketball import BasketBall
from model.teams import Teams

Teams.set_fine_amount(25000)
BasketBall.set_fine_amount(20)

ekip1 = BasketBall("Toronto-Raptors", 9, 5)
print(ekip1.get_stats())

ekip4 = BasketBall("Sixers", 3, 2)
print(ekip4.get_stats())

ekip2 = Teams("LA", 1, 8, "Soccer")
print(ekip2.get_stats() )

# Fine amount for some teams
ekip3 = Teams("Montreal", 14, 2, "Hockey")
print(ekip3.get_stats())
ekip3.get_fined()


ekip5 = BasketBall("Pistons", 5, 6)
print(ekip5.get_stats())
ekip5.get_fined()

# Add Teams Using .txt file
ekip6 = Teams.from_file('OOP/teams.txt')
print(ekip6.get_stats())
