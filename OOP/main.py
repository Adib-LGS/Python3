from gc import get_stats
from os.path import split
import os

from model.football import Football
from model.basketball import BasketBall
from model.teams import Teams

Teams.set_fine_amount(25000)
BasketBall.set_fine_amount(20)


# Principal Class
ekip2 = Teams("LA", 1, 8, "Soccer")
print(ekip2.get_stats() )


# BasketBall sub-class
ekip1 = BasketBall("Toronto-Raptors", 9, 5)
print(ekip1.get_stats())

ekip4 = BasketBall("Sixers", 3, 2)
print(ekip4.get_stats())

ekip5 = BasketBall("Pistons", 5, 6)
print(ekip5.get_stats())
ekip5.get_fined()


# Football sub-class 
ekip7 = Football('Chief', 7, 1, 2)
print(ekip7.get_stats())


# Fine amount for some teams
ekip3 = Teams("Montreal", 14, 2, "Hockey")
print(ekip3.get_stats())
ekip3.get_fined()


# Add Teams Using .txt file
ekip6 = Teams.from_file('OOP/teams.txt')
print(ekip6.get_stats())

# Count Number of created Teams Global and Specific ones
print("[Total of All Teams Created]: ",Teams.number_of_teams)
print("[Total of BasketBall Teams Created]: ",BasketBall.number_of_teams)
print("[Total of Football Teams Created]: ",Football.number_of_teams)