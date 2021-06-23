import os

class Teams:
    
    number_of_teams = 0
    fine_amount = 10_000

    def __init__(self, teams_name, wins, losses, sport):
        self.teams_name = teams_name
        self.wins = wins
        self.losses = losses
        self.sport = sport
        self.total_fines = 0

        if Teams:
            Teams.number_of_teams += 1
            
        if isinstance(self,__class__):
            self.number_of_teams +=1
    
    # Class Method - Charge .txt file in main.py
    @classmethod
    def from_file(cls, stats_as_file):
        try:
            with open(stats_as_file) as file:
                try:
                    teams_name, wins, losses, sport = file.readline().strip().split('-')
                except ValueError:
                    raise ValueError("You must use '-' between the different values")
                    
                return cls(teams_name, int(wins), int(losses), sport)
        except:
            raise FileNotFoundError(f"file [{stats_as_file}] not found")


    # Class Method - Change fine amount directly in main.py
    @classmethod
    def set_fine_amount(cls, amount):
        cls.fine_amount = amount
    

    def get_stats(self):
        winner, looser = self.plural() 

        return f"[Team: {self.teams_name}] || {winner}: {self.wins} || {looser}: {self.losses} || [Catgeory: {self.sport}]"


    # Add fine to teams
    def get_fined(self):
        self.total_fines += self.fine_amount
        print("Fines amount of: ",self.total_fines,"$")

    
    # Pluralize function depending number of wins/losses
    def plural(self):
        winner = 'Win' 
        if self.wins > 1 :
            winner = "Wins"
        looser = "Defeat"
        if self.losses > 1 :
            looser = "Defeats"
        
        return winner,looser
