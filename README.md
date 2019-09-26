## Checkers
***simple checkers game in python***

### Game Rules
- The program receives a file/text input with a sequence of checkers moves and will print the winner: “first”, “second” or “tie”.
- In case there was an illegal move, or the game did not reach its end, the program will report it.
- 4 sample text files are available. 
- The board is 8x8
- A player can only move forward diagonally
- If you can capture the opponent, you must. Even for multiple captures.
- (0,0) is the bottom right white square. 
- In the text file a move is defined as follows: x0, y0, x1, y1 when the player’s move is from (x0, y0) to (x1, y1). A multiple capture appears as multiple lines.
- The game ends when there are no more available moves for the player that needs to play.
- The winner is whoever has more checkers at the end of the game.


#### Test files
| File            | Expected Output               |
|-----------------|-------------------------------|
| black.txt       | second                        |
| white.txt       | first                         |
| incomplete.txt  | incomplete game               |
| illegal_move.txt| line 15 illegal move: 1,0,0,5 |
