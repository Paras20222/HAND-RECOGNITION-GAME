import cv2
import numpy as np
import random

class GameEnvironment:
    def __init__(self):
        """
        Initializes the game environment, including window size, bird properties, gravity, pipes, and scoring.
        """
        self.width = 800
        self.height = 600
        self.bird_y = self.height // 2
        self.velocity = 0
        self.gravity = 1
        self.flap_strength = -15
        self.pipes = []
        self.pipe_width = 80
        self.pipe_gap = 200
        self.pipe_speed = 5
        self.score = 0
        self.spawn_pipe()
    
    def spawn_pipe(self):
        """
        Spawns a new pipe at a random height.
        """
        pipe_height = random.randint(100, 400)
        self.pipes.append([self.width, pipe_height])

    def update_pipes(self):
        """
        Moves pipes to the left and removes off-screen pipes while updating the score.
        """
        for pipe in self.pipes:
            pipe[0] -= self.pipe_speed
        if self.pipes and self.pipes[0][0] < -self.pipe_width:
            self.pipes.pop(0)
            self.spawn_pipe()
            self.score += 1

    def update_bird(self):
        """
        Updates the bird's position based on gravity and velocity.
        """
        self.velocity += self.gravity
        self.bird_y += self.velocity
        if self.bird_y < 0:
            self.bird_y = 0
            self.velocity = 0

    def check_collision(self):
        """
        Checks if the bird has collided with the ground or pipes.
        """
        if self.bird_y > self.height:
            return True
        for pipe in self.pipes:
            if pipe[0] < 100 < pipe[0] + self.pipe_width:
                if self.bird_y < pipe[1] or self.bird_y > pipe[1] + self.pipe_gap:
                    return True
        return False

