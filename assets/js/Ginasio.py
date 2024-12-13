import gym
from gym import spaces
import numpy as np
import random

class SimpleGridEnv(gym.Env):
    """
    Um ambiente simples de tabuleiro 2D com obstáculos, objetivo e agente.
    """
    def __init__(self):
        super(SimpleGridEnv, self).__init__()
        self.grid_size = 5  # Tamanho do tabuleiro (5x5)
        self.state = None  # Estado atual (posição do agente)

        # Ações: 0 = cima, 1 = baixo, 2 = esquerda, 3 = direita
        self.action_space = spaces.Discrete(4)

        # Observação: posição do agente no tabuleiro
        self.observation_space = spaces.Box(low=0, high=self.grid_size - 1, shape=(2,), dtype=np.int32)

        # Posições do objetivo e obstáculos
        self.goal_position = np.array([4, 4])
        self.obstacles = [
            np.array([2, 2]),
            np.array([3, 2]),
            np.array([1, 3]),
        ]

    def reset(self):
        """Reinicia o ambiente e retorna o estado inicial."""
        self.state = np.array([0, 0])  # Posição inicial
        return self.state

    def step(self, action):
        """Executa uma ação e retorna (novo estado, recompensa, terminado, info)."""
        if action == 0:  # Cima
            self.state[0] = max(self.state[0] - 1, 0)
        elif action == 1:  # Baixo
            self.state[0] = min(self.state[0] + 1, self.grid_size - 1)
        elif action == 2:  # Esquerda
            self.state[1] = max(self.state[1] - 1, 0)
        elif action == 3:  # Direita
            self.state[1] = min(self.state[1] + 1, self.grid_size - 1)

        # Verifica se atingiu o objetivo
        if np.array_equal(self.state, self.goal_position):
            return self.state, 10.0, True, {}

        # Verifica se atingiu um obstáculo
        for obstacle in self.obstacles:
            if np.array_equal(self.state, obstacle):
                return self.state, -10.0, True, {}

        # Caso contrário, nenhuma recompensa significativa
        return self.state, -1.0, False, {}

    def render(self):
        """Renderiza o ambiente no console."""
        grid = np.zeros((self.grid_size, self.grid_size), dtype=str)
        grid[:] = '.'
        for obstacle in self.obstacles:
            grid[tuple(obstacle)] = 'X'
        grid[tuple(self.goal_position)] = 'G'
        grid[tuple(self.state)] = 'A'
        for row in grid:
            print(' '.join(row))
        print()

# Testando o ambiente
if __name__ == "__main__":
    env = SimpleGridEnv()
    state = env.reset()
    env.render()

    done = False
    while not done:
        action = env.action_space.sample()  # Escolha de ação aleatória
        state, reward, done, info = env.step(action)
        env.render()
        print(f"Ação: {action}, Recompensa: {reward}, Terminado: {done}")
