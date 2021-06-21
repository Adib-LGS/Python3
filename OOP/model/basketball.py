from model.teams import Teams

class BasketBall(Teams):

    def __init__(self, teams_name, wins, losses, sport = "Basketball"):
        super().__init__(teams_name, wins, losses, sport)