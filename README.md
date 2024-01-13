                                                                          **Hand Gesture Recognition Game**
Overview
This project implements a simple hand gesture recognition game using Python and the Mediapipe library. The game involves two players who take turns making hand gestures, and the gestures are interpreted to determine the score. The game has multiple rounds, and players can advance to higher levels based on their scores.

Prerequisites
Before running the code, make sure you have the following installed:

1.Python (3.6 or later)
2.OpenCV (pip install opencv-python)
3.Mediapipe (pip install mediapipe)


File Structure
The project is organized into the following modules:

HandRecognition.py: Manages hand detection using the Mediapipe library. It captures video from the camera, detects hand landmarks, and switches between players.

GestureInterpreter.py: Interprets hand gestures and maps them to in-game actions. It calculates scores based on the similarity of hand gestures between players.

GameEnvironment.py: Controls the game environment, including displaying the game interface, updating game elements, playing the game, restarting the game, and handling game over scenarios.

ScoringSystem.py: Implements the scoring logic. It calculates scores based on the similarity of hand gestures and defines the rules for advancing to higher levels.

main.py: The main script that orchestrates the interaction between the modules. It initializes instances of the classes defined in the other modules and runs the main game loop.

How to Run
1.Clone the repository to your local machine:
2.Navigate to the project directory:
3.Run the main script:
4.Ensure that your camera is properly connected and accessible.

Gameplay
1.The game initializes with two players (Player 1 and Player 2).
2.Players take turns making hand gestures in front of the camera.
3.Hand gestures are detected and interpreted by the system.
4.Scores are calculated based on the similarity of hand gestures.
5.The game progresses through multiple rounds, and players can advance to higher levels.
6.The game ends when a player reaches a predefined score threshold or after a specified number of rounds.

Customization
1.You can customize the game interface by modifying the display_interface method in GameEnvironment.py.
2.Adjust scoring parameters and game logic in the ScoringSystem.py file.
3.Experiment with different hand gestures and their interpretations in the GestureInterpreter.py file.

Contribution
Feel free to contribute to the project by opening issues, proposing new features, or submitting pull requests.

Happy gaming!





