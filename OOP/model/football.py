from model.teams import Teams

class Football(Teams):

    number_of_teams = 0
    
    def __init__(self, teams_name, wins, losses, draws = 0, sport = "FootBall"):
        super().__init__(teams_name, wins, losses,sport)
        # Teams.__init__(teams_name, wins, losses,sport)

        self.draws = draws

        Football.number_of_teams +=1
    
    # Class Method - Charge .txt file in main.py
    @classmethod
    def from_file(cls, stats_as_file):
        with open(stats_as_file) as file:
            teams_name, wins, losses, draws, sport = file.readline().strip().split('-')
            return cls(teams_name, int(wins), int(losses), int(draws), sport)

    
    def get_stats(self):
        winner, looser = self.plural() 

        return f"[Team: {self.teams_name}] || {winner}: {self.wins} || {looser}: {self.losses} || || Draws: {self.draws} || [Catgeory: {self.sport}]"