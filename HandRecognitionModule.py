import cv2
import mediapipe as mp

class HandRecognition:
    def __init__(self):
        """
        Initializes the hand detection system using MediaPipe.
        """
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands()
        self.mp_draw = mp.solutions.drawing_utils
    
    def detect_hand(self, frame):
        """
        Detects the Index finger position from the camera feed.
        """
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb_frame)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
                return hand_landmarks.landmark[8].y  # Returns y position of index finger
        return None
