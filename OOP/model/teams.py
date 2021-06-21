import os

class Teams:
    
    fine_amount = 10_000

    def __init__(self, teams_name, wins, losses, sport):
        self.teams_name = teams_name
        self.wins = wins
        self.losses = losses
        self.sport = sport
        self.total_fines = 0
    
    # Class Method - Charge .txt file in main.py
    @classmethod
    def from_file(cls, stats_as_file):
        with open(stats_as_file) as file:
            teams_name, wins, losses, sport = file.readline().strip().split('-')
            return cls(teams_name, wins, losses, sport)


    # Class Method - Change fine amount directly in main.py
    @classmethod
    def set_fine_amount(cls, amount):
        cls.fine_amount = amount
    

    def get_stats(self):
        return f"Team: {self.teams_name} || Wins: {self.wins} || Losses: {self.losses} || Catgeory: {self.sport}"

    # Add fine to teams
    def get_fined(self):
        self.total_fines += self.fine_amount
        print("Fines amount of: ",self.total_fines,"$")
