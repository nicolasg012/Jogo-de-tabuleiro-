# Jogo de Tabuleiro com IA

Este projeto implementa um jogo de tabuleiro com inteligência artificial, onde o objetivo é encontrar o melhor caminho até um ponto de destino em um tabuleiro, evitando obstáculos e utilizando uma abordagem inteligente para não repetir caminhos falhos.

## Descrição

O jogo se passa em um tabuleiro de tamanho configurável. O jogador e a IA começam em pontos específicos do tabuleiro e devem encontrar o melhor caminho até o ponto de destino. A IA usa algoritmos de busca para identificar o melhor caminho, evitando obstáculos e tentando otimizar o número de tentativas até encontrar o ponto de destino.

### Funcionalidades
- Tabuleiro com obstáculos aleatórios.
- Algoritmos de busca para a IA encontrar o melhor caminho.
- Registro do número de tentativas feitas pela IA até alcançar o destino.
- Visualização do progresso da IA no tabuleiro.

## Tecnologias Usadas
- Python
- Biblioteca `gymnasium` para criar o ambiente do jogo
- Algoritmos de busca para a inteligência artificial (como Busca em Largura, Busca A*)

## Como Rodar o Projeto

### Pré-requisitos
Antes de rodar o projeto, você precisa ter o Python instalado em sua máquina. Recomendamos usar um ambiente virtual para gerenciar as dependências.

1. Instale o Python (versão 3.6 ou superior) em [python.org](https://www.python.org/downloads/).
2. Crie e ative um ambiente virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Linux/macOS
   venv\Scripts\activate     # Para Windows

#   Instale as dependências do projeto:

bash
pip install -r requirements.txt
Rodando o Jogo
Para rodar o jogo, execute o seguinte comando:

bash
python jogo.py

