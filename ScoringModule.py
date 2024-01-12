class ScoringSystem:
    def __init__(self):
        """
        Initializes the scoring system.
        """
        self.score = 0
    
    def update_score(self, pipes):
        """
        Updates the score based on the number of successfully passed pipes.
        """
        self.score = len(pipes)
    
    def get_score(self):
        """
        Return the current score.
        """
        return self.score
