class HandRecognition:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.players = {"Player 1": 0, "Player 2": 0}
        self.duration_per_player = 10
        self.rounds = 9

        # Initialize variables for player switching
        self.current_player = "Player 1"
        self.start_time = time.time()

        # Initialize Mediapipe Hand module
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands()
        self.mp_drawing = mp.solutions.drawing_utils

    def detect_hand(self, frame):
        # Check if it's time to switch to the next player
        elapsed_time = time.time() - self.start_time
        if elapsed_time >= self.duration_per_player:
            self.start_time = time.time()  # Reset the timer
            self.switch_player()  # Switch to the next player

        # Convert the frame to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame with Mediapipe Hand module
        results = self.hands.process(rgb_frame)

        # Check if hand is detected
        if results.multi_hand_landmarks:
            # Get the landmarks of the current player's hand
            hand_landmarks = results.multi_hand_landmarks[0]  # only one hand must be shown at a time

            # Update the player's hand landmarks in the dictionary
            self.players[self.current_player] = hand_landmarks

            return hand_landmarks
        else:
            return None

    def switch_player(self):
        # Switch to the next player
        if self.current_player == "Player 1":
            self.current_player = "Player 2"
        else:
            self.current_player = "Player 1"
