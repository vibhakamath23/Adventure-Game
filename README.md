# Adventure-Game

This is a choose-your-own-adventure game built from self-interest that relies on user input to run appropriate paths. The built-in game map consists of nine rooms, but the structure is not revealed, and the player begins in the same place every time. The possibile directions to move are North, South, East, and West (the user is directed to type N, S, E, or W). Every time the game is run, a "key" is randomly assigned into one of the rooms, and the goal of the player is to search the rooms until you find the key and return back to where you started in order to escape. Each room contains its own set of choices and resulting minigames, such as tic tac toe, hangman, and various trivia questions, with frequent cameo appearances from a variety of celebrities. 

The game terminates if the player wins or meets an untimely end, which is possible in some of the rooms. 

The structure of the game involves mainly if/else statements. The rooms are defined as dictionaries and stored as a list. A list of rooms already visited also exists, starting as empty, to which every room visited is added so as to avoid repetition. 
