import cv2
from GameEnvironmentModule import GameEnvironment
from GestureInterpreterModule import GestureInterpreter
from HandRecognitionModule import HandRecognition
from ScoringModule import ScoringSystem

# Initialize game components
game_env = GameEnvironment()
gesture_interpreter = GestureInterpreter()
hand_recognition = HandRecognition()
scoring_system = ScoringSystem()

# Start video capture
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Detect hand and interpret gesture
    hand_position = hand_recognition.detect_hand(frame)
    action = gesture_interpreter.interpret_gesture(hand_position) if hand_position else "NO ACTION"
    
    if action == "FLAP":
        game_env.velocity = game_env.flap_strength
    
    # Update game state
game_env.update_bird()
game_env.update_pipes()
scoring_system.update_score(game_env.pipes)

    # Check for collision
    if game_env.check_collision():
        print("Game Over! Score:", scoring_system.get_score())
        break

    # Display game window
    cv2.imshow("Hand Controlled Flappy Bird", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
