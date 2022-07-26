![](vertopal_74952c3293c24461914b85d0b7384458/media/image2.png){width="5.763888888888889in"
height="0.5972222222222222in"}![](vertopal_74952c3293c24461914b85d0b7384458/media/image3.png){width="0.7083333333333334in"
height="0.20833333333333334in"}![](vertopal_74952c3293c24461914b85d0b7384458/media/image4.png){width="2.8194444444444446in"
height="1.125in"}![](vertopal_74952c3293c24461914b85d0b7384458/media/image5.png){width="1.9305555555555556in"
height="0.4027777777777778in"}![](vertopal_74952c3293c24461914b85d0b7384458/media/image6.png){width="0.6666666666666666in"
height="0.19444444444444445in"}![](vertopal_74952c3293c24461914b85d0b7384458/media/image7.png){width="3.0in"
height="0.19444444444444445in"}

**COE292-213 - Project \# 1: Tic-Tac-Toe**

**Using Minimax, implement an AI to play Tic-Tac-Toe optimally**

![](vertopal_74952c3293c24461914b85d0b7384458/media/image1.png){width="3.7805555555555554in"
height="2.834722222222222in"}

**Getting Started**

+---+-----------------------------------------------------------------+
| • | > Watch the following help video: https://bit.ly/3Jrm5Si        |
+===+=================================================================+
| • | > Download the file tictactoe.zip and unzip it.                 |
+---+-----------------------------------------------------------------+
| • | > Once in the directory for the project, run **pip3 install -r  |
|   | > requirements.txt**to                                          |
+---+-----------------------------------------------------------------+
|   | > install the required Python package (pygame) for this         |
|   | > project.                                                      |
+---+-----------------------------------------------------------------+

**Understanding**\
There are two main files in this project: runner.py and tictactoe.py.
tictactoe.py contains all the logic for playing the game, and for making
optimal moves. runner.py has been implemented for you, and contains all
of the code to run the graphical interface for the game. Once you've
completed all the required functions in tictactoe.py, you should be able
to run **python runner.py**to play against your AI!

Let's open up tictactoe.py to get an understanding for what's provided.
First, we define three variables: X, O, and EMPTY, to represent possible
moves of the board.

The function initial_state returns the starting state of the board. For
this problem, we've chosen to represent the board as a list of three
lists (representing the three rows of the board), where each internal
list contains three values that are either X, O, or EMPTY. What follows
are functions that we've left up to you to implement!

**Specification**\
An automated tool assists the staff in enforcing the constraints in the
below specification. Your submission will fail if any of these are not
handled properly, if you import modules other than those explicitly
allowed, or if you modify functions other than as permitted.

Complete the implementations of player, actions, result, winner,
terminal, utility, and minimax.

![](vertopal_74952c3293c24461914b85d0b7384458/media/image9.png){width="3.7777777777777777in"
height="0.8194444444444444in"}![](vertopal_74952c3293c24461914b85d0b7384458/media/image10.png){width="1.9444444444444444in"
height="0.6111111111111112in"}![](vertopal_74952c3293c24461914b85d0b7384458/media/image11.png){width="2.361111111111111in"
height="0.4027777777777778in"}![](vertopal_74952c3293c24461914b85d0b7384458/media/image12.png){width="0.18055555555555555in"
height="0.16666666666666666in"}![](vertopal_74952c3293c24461914b85d0b7384458/media/image13.png){width="1.125in"
height="0.5972222222222222in"}![](vertopal_74952c3293c24461914b85d0b7384458/media/image14.png){width="1.1111111111111112in"
height="0.19444444444444445in"}![](vertopal_74952c3293c24461914b85d0b7384458/media/image15.png){width="3.4166666666666665in"
height="0.19444444444444445in"}![](vertopal_74952c3293c24461914b85d0b7384458/media/image16.png){width="2.2083333333333335in"
height="0.5972222222222222in"}![](vertopal_74952c3293c24461914b85d0b7384458/media/image17.png){width="2.4305555555555554in"
height="0.5972222222222222in"}![](vertopal_74952c3293c24461914b85d0b7384458/media/image18.png){width="0.18055555555555555in"
height="0.375in"}![](vertopal_74952c3293c24461914b85d0b7384458/media/image19.png){width="4.861111111111111in"
height="0.8194444444444444in"}![](vertopal_74952c3293c24461914b85d0b7384458/media/image20.png){width="0.18055555555555555in"
height="0.16666666666666666in"}![](vertopal_74952c3293c24461914b85d0b7384458/media/image21.png){width="0.18055555555555555in"
height="0.16666666666666666in"}![](vertopal_74952c3293c24461914b85d0b7384458/media/image22.png){width="0.5694444444444444in"
height="0.20833333333333334in"}![](vertopal_74952c3293c24461914b85d0b7384458/media/image23.png){width="0.8055555555555556in"
height="0.20833333333333334in"}![](vertopal_74952c3293c24461914b85d0b7384458/media/image24.png){width="1.875in"
height="0.19444444444444445in"}![](vertopal_74952c3293c24461914b85d0b7384458/media/image25.png){width="0.18055555555555555in"
height="0.16666666666666666in"}![](vertopal_74952c3293c24461914b85d0b7384458/media/image26.png){width="0.18055555555555555in"
height="0.16666666666666666in"}![](vertopal_74952c3293c24461914b85d0b7384458/media/image27.png){width="0.18055555555555555in"
height="0.16666666666666666in"}

+---+-----------------------------------------------------------------+
| • | > The "player" function should take a board state as input, and |
|   | > return which player's turn it is (either X or O).             |
+---+-----------------------------------------------------------------+

> oIn the initial game state, X gets the first move. Subsequently, the
> player alternates with
>
> each additional move.
>
> oAny return value is acceptable if a terminal board is provided as
> input (i.e., the game is
>
> already over).

+---+-----------------------------------------------------------------+
| • | > The "actions" function should return a set of all the         |
|   | > possible actions that can be taken on a given board.          |
+---+-----------------------------------------------------------------+

> oEach action should be represented as a tuple (i, j) where i
> corresponds to the row of the
>
> move (0, 1, or 2) and j corresponds to which cell in the row
> corresponds to the move (also 0, 1, or 2).
>
> oPossible moves are any cells on the board that do not already have an
> X or an O in them. oAny return value is acceptable if a terminal board
> is provided as input.

+----------------------------------+----------------------------------+
| •                                | > The "result" function takes a  |
|                                  | > board and an action as input,  |
| ![](vertopal_74952c3293c2446     | > and should return a new board  |
| 1914b85d0b7384458/media/image8.p | > state, without modifying the   |
| ng){width="0.1527777777777778in" | > original board.                |
| height="0.18055555555555555in"}  |                                  |
+----------------------------------+----------------------------------+

> oIf action is not a valid action for the board, your program should
> oThe returned board state should be the board that would result from
> taking the original
>
> input board and letting the player whose turn it is make their move at
> the cell indicated by the input action.
>
> oImportantly, the original board should be left unmodified: since
> Minimax will ultimately
>
> require considering many different board states during its
> computation. This means that simply updating a cell in board itself is
> not a correct implementation of the result function. You'll likely
> want to make a of the board first before making any changes.

+---+-----------------------------------------------------------------+
| • | > The "winner" function should accept a board as input and      |
|   | > return the winner of the board if there is one.               |
+---+-----------------------------------------------------------------+

> oIf the X player has won the game, your function should return X. If
> the O player has won
>
> the game, your function should return O.
>
> oOne can win the game with three of their moves in a row horizontally,
> vertically, or
>
> diagonally.
>
> oYou may assume that there will be at most one winner (that is, no
> board will ever have
>
> both players with three-in-a-row, since that would be an invalid board
> state).
>
> oIf there is no winner of the game (either because the game is in
> progress, or because it
>
> ended in a tie), the function should return None.

+---+-------------------------------------------------------------------------+
| • | +---+-----------------------------------------------------------------+ |
|   | |   | > The "terminal" function should accept a board as input and    | |
|   | |   | > return a Boolean value indicating whether the game is over.   | |
|   | +---+-----------------------------------------------------------------+ |
|   |                                                                         |
|   | •                                                                       |
+---+-------------------------------------------------------------------------+

> oIf the game is over, either because someone has won the game or
> because all cells have
>
> been filled without anyone winning, the function should return True.
>
> oOtherwise, the function should return False if the game is still in
> progress.

+---+-----------------------------------------------------------------+
| • | > The "utility" function should accept a terminal board as      |
|   | > input and output the utility of the board.                    |
+---+-----------------------------------------------------------------+

> oIf X has won the game, the utility is 1. If O has won the game, the
> utility is -1. If the game
>
> has ended in a tie, the utility is 0.
>
> oYou may assume utility will only be called on a board if
> terminal(board) is True.

![](vertopal_74952c3293c24461914b85d0b7384458/media/image28.png){width="3.486111111111111in"
height="0.6111111111111112in"}![](vertopal_74952c3293c24461914b85d0b7384458/media/image29.png){width="1.5833333333333333in"
height="0.6111111111111112in"}![](vertopal_74952c3293c24461914b85d0b7384458/media/image30.png){width="1.4027777777777777in"
height="0.20833333333333334in"}![](vertopal_74952c3293c24461914b85d0b7384458/media/image31.png){width="0.9583333333333334in"
height="0.19444444444444445in"}![](vertopal_74952c3293c24461914b85d0b7384458/media/image32.png){width="3.625in"
height="0.20833333333333334in"}

+---+-----------------------------------------------------------------+
| • | > The "minimax" function should take a board as input and       |
|   | > return the optimal move for the player to move on that board. |
+---+-----------------------------------------------------------------+

> oThe move returned should be the optimal action (i, j) that is one of
> the allowable actions
>
> on the board. If multiple moves are equally optimal, any of those
> moves is acceptable.
>
> oIf the board is a terminal board, the minimax function should return
> None.

For all functions that accept a board as input, you may assume that it
is a valid board (namely, that it is a list that contains three rows,
each with three values of either X, O, or EMPTY). You should not modify
the function declarations (the order or number of arguments to each
function) provided.

Once all functions are implemented correctly, you should be able to run
python runner.py and play against your AI. And, since Tic-Tac-Toe is a
tie given optimal play by both sides, you should never be able to beat
the AI (though if you don't play optimally as well, it may beat you!)

**Hints**

+---+-----------------------------------------------------------------+
| • | > You're welcome to add additional helper functions to          |
|   | > tictactoe.py, provided that their                             |
+===+=================================================================+
| • | > names do not collide with function or variable names already  |
|   | > in the module.                                                |
+---+-----------------------------------------------------------------+
|   | > You may need to implement the functions max-value and         |
|   | > min-value mentioned in the                                    |
+---+-----------------------------------------------------------------+
| • | > help video above.                                             |
+---+-----------------------------------------------------------------+
|   | If you'd like to test your functions in a different Python      |
|   | file, you can import them with lines like                       |
+---+-----------------------------------------------------------------+
|   | > from tictactoe import initial_state.                          |
+---+-----------------------------------------------------------------+


*Credit:* https://cs50.harvard.edu/ai/2020/projects/0/tictactoe/