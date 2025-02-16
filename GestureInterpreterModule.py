class GestureInterpreter:
    def __init__(self):
        """
        Initializes gesture interpretation parameters.
        """
        self.threshold = 0.5
    
    def interpret_gesture(self, hand_position):
        """
        Interprets the detected hand position and decides whether to flap.
        """
        if hand_position < self.threshold:
            return "FLAP"
        return "NO ACTION"
