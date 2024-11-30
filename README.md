# Connect Four Game 
This repository features a coded version of the classic Connect Four game with a unique scoring system. Instead of ending when a player achieves a traditional “Connect Four,” the game evaluates based on the number of potential Connect Four positions created by each player. The player with the most potential winning opportunities when the board is full wins.

## Key Features
### Game Modes

* **Player vs. Play**: Two players can compete against each other.

* **Player vs. Computer AI**: The game featurs an AI opponent that anlayzes the board to find th eoptimal moves based on available positions.

### Console-based Interface
The  game includes a simple, text-based landing page that runs in the Python Terminl. From this mennu players can choose the following: 

* Choose between the game modes.
* Read detailed instructions on how to play.
* Exit the game at any time.

### AI Logic
The computer AI is designed to make strategic decisions by evaluating the board and selecting moces that maximize its chances of winning.

## Instructions

1. **Start the Game**: Run the game script in your Python terminal to access the landing page.

2. **Chose a Game mode**: Select whether to play against another player or the AI.

3. **Gameplay**: Take turns dropping pieces into the columns. The game will track and count potential Connect Four Positions. 

4. **Winning**: The player with the most potential Connect Four opportunities at the end wins. 

## How to Run
Run the game using the following command:

```bash
python connect_four.py
```
Enjoy playing and strategizing in this new twist on Connect Four. 

## Technologies used 
Python
