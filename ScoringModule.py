class ScoringSystem:
    def __init__(self):
        # Initialize scoring parameters (if needed)
        self.scoring_params = {
            "matching_fingers_threshold": 5,
            "points_per_matching_finger": 10,
            "base_points_for_common_fingers": 5
        }

    def calculate_score(self, player1_gesture, player2_gesture):
        
        matching_fingers = sum(f1 == f2 for f1, f2 in zip(player1_gesture, player2_gesture))

        if matching_fingers == 5:
            return 100  # If all fingers are the same, 100 points
        else:
            points_per_matching_finger = 10

            if matching_fingers > 0:
                # Calculate total score for matching fingers
                score = matching_fingers * points_per_matching_finger
            else:
                # Calculate total score for different fingers
                score = 5  # Base points for common fingers

        return score

    def advance_level(self, player1_score, player2_score):
    
        max_score = max(player1_score, player2_score)

        # Reduce the number of iterations by 2
        self.iterations //= 2

        # Ensure the resulting number is odd
        self.iterations = self.iterations + 1 if self.iterations % 2 == 0 else self.iterations

        if max_score >= 100:
            if max_score == player1_score:
                print(f"Player 1 Advanced to the Next Level with {self.iterations} iterations")
                self.current_round = 1  # Reset round counter after advancing
                self.play_game()  # Play the game at the new level
            else:
                print(f"Player 2 Advanced to the Next Level with {self.iterations} iterations")
                self.current_round = 1  # Reset round counter after advancing
                self.play_game()  # Play the game at the new level
        else:
            print(f"Try Again to Advance with {self.iterations} iterations")
            self.restart_game()
