Hand Gesture Recognition Game
Overview
This project implements a simple hand gesture recognition game using Python and the Mediapipe library. The game involves two players who take turns making hand gestures, and the gestures are interpreted to determine the score. The game has multiple rounds, and players can advance to higher levels based on their scores.

Prerequisites
Before running the code, make sure you have the following installed:

Python (3.6 or later)
OpenCV (pip install opencv-python)
Mediapipe (pip install mediapipe)
File Structure
The project is organized into the following modules:

HandRecognition.py: Manages hand detection using the Mediapipe library. It captures video from the camera, detects hand landmarks, and switches between players.

GestureInterpreter.py: Interprets hand gestures and maps them to in-game actions. It calculates scores based on the similarity of hand gestures between players.

GameEnvironment.py: Controls the game environment, including displaying the game interface, updating game elements, playing the game, restarting the game, and handling game over scenarios.

ScoringSystem.py: Implements the scoring logic. It calculates scores based on the similarity of hand gestures and defines the rules for advancing to higher levels.

main.py: The main script that orchestrates the interaction between the modules. It initializes instances of the classes defined in the other modules and runs the main game loop.

How to Run
Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/your-username/hand-gesture-game.git
Navigate to the project directory:

bash
Copy code
cd hand-gesture-game
Run the main script:

bash
Copy code
python main.py
Ensure that your camera is properly connected and accessible.

Gameplay
The game initializes with two players (Player 1 and Player 2).

Players take turns making hand gestures in front of the camera.

Hand gestures are detected and interpreted by the system.

Scores are calculated based on the similarity of hand gestures.

The game progresses through multiple rounds, and players can advance to higher levels.

The game ends when a player reaches a predefined score threshold or after a specified number of rounds.

Customization
You can customize the game interface by modifying the display_interface method in GameEnvironment.py.

Adjust scoring parameters and game logic in the ScoringSystem.py file.

Experiment with different hand gestures and their interpretations in the GestureInterpreter.py file.

Troubleshooting
If the camera is not working, check that it is properly connected and not in use by another application.

If there are issues with hand detection, ensure proper lighting conditions and experiment with hand positioning.

Check for any error messages in the console for additional troubleshooting.

Contribution
Feel free to contribute to the project by opening issues, proposing new features, or submitting pull requests.

Happy gaming!


