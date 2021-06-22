from model.teams import Teams

class BasketBall(Teams):
    
    number_of_teams = 0

    def __init__(self, teams_name, wins, losses, sport = "Basketball"):
        super().__init__(teams_name, wins, losses, sport)

        BasketBall.number_of_teams +=1