import cv2
from GameEnvironmentModule import GameEnvironment
from GestureInterpreterModule import GestureInterpreter
from HandRecognitionModule import HandRecognition
from ScoringModule import ScoringSystem

# Initialize all modules
game_env = GameEnvironment()
gesture_interpreter = GestureInterpreter()
hand_recognition = HandRecognition()
scoring_system = ScoringSystem()

# Open the webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  # Exit if no frame is captured

    # Detect hand position
    hand_position = hand_recognition.detect_hand(frame)

    # Interpret the gesture (FLAP or NO ACTION)
    action = gesture_interpreter.interpret_gesture(hand_position) if hand_position else "NO ACTION"

    # If the hand gesture is detected as FLAP, apply the flap strength
    if action == "FLAP":
        game_env.velocity = game_env.flap_strength

    # Update game elements
    game_env.update_bird()
    game_env.update_pipes()
    scoring_system.update_score(game_env.pipes)

    # Check if the bird collides with pipes or ground
    if game_env.check_collision():
        print("Game Over! Score:", scoring_system.get_score())
        break  # Exit the game loop

    # Show the game window
    cv2.imshow("Hand Controlled Flappy Bird", frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources after exiting
cap.release()
cv2.destroyAllWindows()
