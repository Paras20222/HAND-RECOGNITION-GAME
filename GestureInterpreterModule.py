class GestureInterpreter:
    def __init__(self):
        # Initialize gesture interpretation parameters
        self.gesture_params = {
            "matching_fingers_threshold": 5,
            "points_per_matching_finger": 10,
            "points_for_common_fingers": 5,
            "points_for_different_fingers": 0
        }

    def map_gesture_to_action(self, player1_gesture, player2_gesture):
        
        #Map detected hand gestures to in-game actions.
        matching_fingers = sum(f1 == f2 for f1, f2 in zip(player1_gesture, player2_gesture))

        if matching_fingers == 5:
            return "Same Fingers: 100 points"
        else:
            points_per_matching_finger = 10

            if matching_fingers > 0:
                return f"Matching Fingers: {matching_fingers * points_per_matching_finger} points"
            else:
                return "Different Fingers: 5 points for common fingers, 0 points for different fingers"
