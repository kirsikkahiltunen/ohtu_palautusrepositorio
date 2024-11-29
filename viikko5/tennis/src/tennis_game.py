class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.score_player1 = 0
        self.score_player2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.score_player1 += 1
        else:
            self.score_player2 += 1

    def get_score(self):
        score_calls = {0:"Love", 1:"Fifteen", 2:"Thirty", 3:"Forty"}

        def score_call_equal(self, score_calls):
            if self.score_player1 >= 3:
                score_call = "Deuce"
            else:
                score_call = f"{score_calls[self.score_player1]}-All"
            return score_call
        
        def score_call_advantage(self):
            point_difference = self.score_player1 - self.score_player2

            if point_difference == 1:
                score_call = "Advantage player1"
            elif point_difference == -1:
                score_call = "Advantage player2"
            elif point_difference >= 2:
                score_call = "Win for player1"
            else:
                score_call = "Win for player2"
            return score_call

        if self.score_player1 == self.score_player2:
            score=score_call_equal(self, score_calls)
            
        elif self.score_player1 >= 4 or self.score_player2 >= 4:
            score = score_call_advantage(self)

        else:
            score = f"{score_calls[self.score_player1]}-{score_calls[self.score_player2]}"
        
        return score