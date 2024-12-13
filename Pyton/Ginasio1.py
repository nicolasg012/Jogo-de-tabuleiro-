import gymnasium as gym
from gymnasium import spaces
import numpy as np

class TabuleiroEnv(gym.Env):
    def __init__(self):
        super(TabuleiroEnv, self).__init__()
        self.grid_size = 5  # Tabuleiro de 5x5
        self.start = (0, 0)
        self.goal = (4, 4)
        self.position = self.start
        # Definindo múltiplos obstáculos no tabuleiro
        self.obstacles = [(2, 2), (1, 3), (3, 1)]
        self.visited = set()

        # Contador de tentativas
        self.attempts = 0

        # Ação: 0 - cima, 1 - baixo, 2 - esquerda, 3 - direita
        self.action_space = spaces.Discrete(4)

        # Espaço de observação: posição no grid (x, y)
        self.observation_space = spaces.Discrete(self.grid_size * self.grid_size)

    def reset(self):
        self.position = self.start
        self.visited = {self.start}
        self.attempts = 0  # Reseta o contador de tentativas
        return self.position

    def step(self, action):
        x, y = self.position
        if action == 0:  # cima
            x = max(x - 1, 0)
        elif action == 1:  # baixo
            x = min(x + 1, self.grid_size - 1)
        elif action == 2:  # esquerda
            y = max(y - 1, 0)
        elif action == 3:  # direita
            y = min(y + 1, self.grid_size - 1)

        new_position = (x, y)

        # Verifica se o novo movimento atingiu o objetivo ou um obstáculo
        if new_position == self.goal:
            reward = 10  # Recompensa ao alcançar o objetivo
            done = True
        elif new_position in self.obstacles:
            reward = -5  # Penalização por colidir com o obstáculo
            done = False
        elif new_position in self.visited:
            reward = -1  # Penalização por revisitar um caminho
            done = False
        else:
            reward = -0.1  # Pequena penalização por mover-se
            done = False

        self.position = new_position
        self.visited.add(new_position)

        # Atualiza o contador de tentativas
        self.attempts += 1

        return self.position, reward, done, {}

    def render(self):
        grid = np.full((self.grid_size, self.grid_size), '.', dtype=str)

        # Marca o objetivo e os obstáculos
        grid[self.goal] = 'G'
        for obs in self.obstacles:
            grid[obs] = 'X'  # Obstáculo representado por 'X'
        grid[self.position] = 'P'  # Posição do agente representada por 'P'

        # Exibindo o tabuleiro com espaçamento entre os espaços
        for row in grid:
            print("  ".join(row))  # Espaçamento entre as células

# Exemplo de uso
env = TabuleiroEnv()
env.reset()
while True:
    action = env.action_space.sample()  # Agente escolhe uma ação aleatória
    observation, reward, done, _ = env.step(action)
    env.render()
    if done:
        print(f"Objetivo alcançado com recompensa {reward}")
        print(f"Total de tentativas: {env.attempts}")
        break
