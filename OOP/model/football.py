from model.teams import Teams

class Football(Teams):

    number_of_teams = 0
    
    def __init__(self, teams_name, wins, losses, sport = "FootBall"):
        super().__init__(teams_name, wins, losses, sport)

        Football.number_of_teams +=1