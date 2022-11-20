import random
import torch
import numpy as np
from abc import ABC, abstractmethod


class Agent:
    def __init__(self):
        pass

    @abstractmethod
    def get_action(self, state):
        pass


class Player:
    def __init__(self, policy, dice_count):
        self.lives = 2
        self.dice_count = dice_count
        self.policy = policy


class Snyd:
    def __init__(self, agents, dice_count):
        self.agents = agents
        self.dice_count = dice_count

    def play_game(self):
        players = []
        for agent in self.agents:
            players.append(Player(agent, self.dice_count))

        start_index = random.randint(0, len(players))
        game_over = False
        state = np.zeros([6, len(players) * self.dice_count])
        print(state)

        while not game_over:
            for i in range(len(players)):
                current_player = players[(i + start_index) % len(players)]
                if current_player.dice_count > 0:
                    current_player.policy.get_action(state, len(players))


game = Snyd([Agent(), Agent()], 4)
game.play_game()
