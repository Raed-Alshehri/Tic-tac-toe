
# Tic-tac-toe

This project is an implementation of Minimax algorithm for an AI to play Tic-Tac-Toe optimally.

To play the game, download and run the following two files
- [tictactoe.py](https://github.com/Raed-Alshehri/Tic-tac-toe/blob/main/tictactoe.py): contains all the logic for playing the game and  making optimal moves
- [runner.py](https://github.com/Raed-Alshehri/Tic-tac-toe/blob/main/runner.py): to run the graphical interface for the game

## Screenshot


![App Screenshot](https://raw.githubusercontent.com/Raed-Alshehri/Tic-tac-toe/main/Img/image1.png)

## Functions and Description:

```
The “player” function takes a board state as input, and return which player’s turn it is (either X or O).
o In the initial game state, X gets the first move. Subsequently, the player alternates with each additional move.
o if a terminal board is provided as input (i.e., the game is already over), the function returns None.
```
```
The “actions” function returns a set of all the possible actions that can be taken on a given board.
o Each action is represented as a tuple (i, j) where i corresponds to the row of the move (0, 1, or 2) and j corresponds to which cell in the row corresponds to the move (also 0, 1, or 2).
o Possible moves are any cells on the board that do not already have an X or an O in them.
```
```
The “result” function takes a board and an action as input, and returns a new board state, without modifying the original board.
o If action is not a valid action for the board, the program raises an exception.
o The returned board state is the board that would result from taking the original input board and letting the player whose turn it is make their move at the cell indicated by the input action.
```
```
The “winner” function accepts a board as an input and returns the winner of the board (if there is one).
o If the X player has won the game, the function returns X. If the O player has won the game, the function returns O.
o One can win the game with three of their moves in a row horizontally, vertically, or diagonally.
o If there is no winner of the game (either because the game is in progress, or because it ended in a tie), the function returns None.
```
```
The “terminal” function accepts a board as input and return a Boolean value indicating whether the game is over.
o If the game is over, (someone has won the game or all cells have been filled without anyone winning), the function returns True.
o Otherwise, the function returns False if the game is still in progress.
```
```
The “utility” function accepts a terminal board as input and outputs the utility of the board.
o If X has won the game, the utility is 1. If O has won the game, the utility is -1. If the game has ended in a tie, the utility is 0.
```
```
The “minimax” function takes a board as input and returns the optimal move for the player to move on that board.
o The move returned is the the optimal action (i, j) that is one of the allowable actions on the board. If multiple moves are equally optimal, any of those moves is acceptable.
o If the board is a terminal board, the minimax function returns None.
```


## 🛠 Skills Used

Python, Pygame, Minimax
## 🚀 About Me
👋 Hi, I’m @Raed-Alshehri

👀 I’m interested in data science, machine learning, and statistics.

🌱 I’m applying my skills in the data analytics field using Python, R, and SQL


## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://raed-alshehri.github.io/RaedAlshehri.github.io/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/raedalshehri/)


## Feedback

If you have any feedback, please reach out to me at alshehri.raeda@gmail.com


## Credits

[Harvard cs50](https://cs50.harvard.edu/ai/2020/projects/0/tictactoe/)

