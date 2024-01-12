# Hand-Controlled Flappy Bird Game

A fun and interactive version of Flappy Bird, controlled through hand gestures using MediaPipe's hand tracking. The game uses Python, OpenCV, and MediaPipe to detect hand gestures and interact with the game environment.

## Project Overview

This project implements the classic **Flappy Bird** game, where the user controls the bird's flapping motion by raising their hand. The gesture recognition system is powered by **MediaPipe**, which processes real-time camera frames to detect the position of the user's hand. The bird moves based on the detected gesture, and the goal is to pass through pipes without colliding.

## Features:
- **Hand Gesture Control**: Uses **MediaPipe** for real-time hand tracking and interprets hand gestures to control the bird.
- **Game Mechanics**: Includes gravity, bird flap motion, pipe spawning, and score tracking.
- **Scoring System**: The score is based on the number of pipes the bird successfully passes.
- **Real-Time Gameplay**: OpenCV is used for rendering the game window and capturing the Webcam feed.

## Technical Details

### Core Components:
1. **Game Environment**: 
   - Handles the game's environment, bird movement, pipe spawning, and collision detection.
   - The `GameEnvironment` class manages game logic, including gravity, pipe movement, and scoring.
   
2. **Gesture Interpreter**:
   - Interprets hand gestures and translates them into game actions. For example, the hand position (above or below a threshold) is mapped to the "FLAP" action.
   
3. **Hand Recognition**:
   - Uses **MediaPipe**'s hand tracking model to detect the position of the index finger from the webcam feed. This position is then used to interpret gestures.
   
4. **Scoring System**:
   - Tracks the player's score based on how many pipes the bird passes.

### How It Works:
1. **Game Initialization**:
   - The game window is created using OpenCV, and modules are initialized for game logic, gesture interpretation, hand recognition, and scoring.
   
2. **Hand Gesture Detection**:
   - The camera captures frames, and MediaPipe processes these frames to detect the index finger's position.
   
3. **Gesture Interpretation**:
   - Based on the detected hand position, the `GestureInterpreter` decides whether the player is making the "FLAP" gesture or "NO ACTION".
   
4. **Game Loop**:
   - The game runs in a loop, where each frame updates the bird's position, moves the pipes, checks for collisions, and updates the score.
   
5. **Collision Detection**:
   - The game checks if the bird collides with pipes or the ground using the `check_collision` function.
   
6. **Scoring**:
   - The score is updated based on the number of pipes the bird passes.

### Libraries Used:
- **OpenCV**: For handling the video capture, rendering the game window, and processing the frames.
- **MediaPipe**: For real-time hand tracking to detect hand gestures.
- **NumPy**: For handling arrays and mathematical operations in the game logic.

### Dependencies:

```txt
mediapipe==0.8.6
opencv-python==4.5.3.56
numpy==1.21.0
