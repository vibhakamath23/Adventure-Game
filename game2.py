import random
import time

def get_choice(room,dir):
    if dir=='N':
        choice = 0
    elif dir=='E':
        choice = 1
    elif dir=='S':
        choice = 2
    elif dir=='W':
        choice = 3
    else:
        return -1

    if room['directions'][choice] == 0:
        return 4
    else:
        return choice

def main():
    dirs = (0,0,0,0)

    entrance = {'name':'Entrance Way','directions':dirs,'msg':'You are in the entrance.'}
    dungeon = {'name':'Dungeon','directions':dirs,'msg':'hksjl'}
    hallway = {'name':'Hallway','directions':dirs,'msg':'dfsafd'}
    trophyroom = {'name':'Trophy Room','directions':dirs,'msg':'fds'}
    dininghall = {'name':'Dining Hall','directions':dirs,'msg':'sdaf'}
    closet = {'name':'Closet','directions':dirs,'msg':'dsfa'}
    courtyard = {'name':'Courtyard','directions':dirs,'msg':'asdf'}
    weaponry = {'name':'Weaponry','directions':dirs,'msg':'sdaf'}
    armory = {'name':'Armory','directions':dirs,'msg':'asdf'}

    #N,E,S,W

    entrance['directions'] = (trophyroom,dungeon,weaponry,closet)
    dungeon['directions'] = (dininghall,0,armory,entrance)
    hallway['directions'] = (0,trophyroom,closet,0)
    trophyroom['directions'] = (0,dininghall,entrance,hallway)
    dininghall['directions'] = (0,0,dungeon,trophyroom)
    closet['directions'] = (hallway,entrance,courtyard,0)
    courtyard['directions'] = (closet,weaponry,0,0)
    weaponry['directions'] = (entrance,armory,0,courtyard)
    armory['directions'] = (dungeon,0,0,weaponry)

    rooms = [dungeon, hallway, trophyroom, dininghall, closet, courtyard, weaponry, armory]
    random.shuffle(rooms)
    #room_with_killer = rooms[1]
    room_with_key = rooms[2]
    found_key = False
    room = entrance
    gameIsPlaying = True
    print("You have been locked in an abandoned castle by an unknown killer.")
    time.sleep(1)
    print("There are 9 rooms total, and you start in the center.")
    time.sleep(1)
    print("Each room you choose to enter brings choice...")
    time.sleep(1)
    print("Be careful what you do.")
    time.sleep(1)
    print("Answers lie everywhere- but so does danger.")
    time.sleep(1)
    print("A key to the door is hiding in one of the rooms around you...")
    time.sleep(1)
    print("Choose wisely, stay alive, and pay attention to the clues you find- you'll need them to escape!")
    time.sleep(1)
    rooms_entered = []

#MAIN GAME FUNCTION
    while gameIsPlaying:
        #So the room message won't repeat
        if found_key and room['name'] == 'Entrance Way':
            print('You have found the key and returned to the entrance.')
            time.sleep(1)
            print("One last thing before you can leave...")
            time.sleep(1)
            print("You were told to pay attention to the clues around you.")
            time.sleep(1)
            print("To escape, you must identify the killer who trapped you here...")
            time.sleep(1)
            print("Based on what you have seen around the castle.")
            time.sleep(1)
            choice15 = raw_input("Press ENTER to see the suspects!")
            if choice15 == 'x':
                raw_input("PRESS ENTER!")
            else:
                print("They are...")
                time.sleep(1)
                print("1. Steve McEvilScientist, a renowned biologist who may have a dark side...")
                time.sleep(1)
                print("2. Doctor DeathDinosaur, an archaeologist who may have more than a few skeletons buried in her closet...")
                time.sleep(1)
                print("3. The Snapshooter, a journalist whose documentation can be more than a little deadly...")
                time.sleep(1)
                finalChoice = raw_input("So, according to your deduction, who trapped you in here? (1, 2, or 3)")
                if finalChoice == '1':
                    print("SO CLOSE! Steve McEvilScientist, despiting being very evil, did not trap you here.")
                    time.sleep(1)
                    print("You didn't pay enough attention to the clues!")
                    time.sleep(1)
                    print("You failed! GAME OVER! Better luck next time.")
                    exit(gameIsPlaying)
                elif finalChoice == '2':
                    print("SO CLOSE! Doctor DeathDinosaur did not trap you here.")
                    time.sleep(1)
                    print("You didn't pay enough attention to the clues!")
                    time.sleep(1)
                    print("You failed! GAME OVER! Better luck next time.")
                    exit(gameIsPlaying)
                elif finalChoice == '3':
                    print("YES! You paid attention to the pictures, the cameras, the journalist equipment!")
                    time.sleep(1)
                    print('You have beat the game and have successfully escaped. Congrats!')
                    time.sleep(1)
                    break
                else:
                    print("You must pick a suspect. (1,2,3)")

        elif room['name'] in rooms_entered:
            print('You are back in the ' + room['name'] + '.')
        #
        # elif room['name'] == room_with_killer['name']:
        #     print("AAAAA! The killer was hiding there! You were killed!")
        #     break

        #Once you find the key
        elif room_with_key['name'] == room['name']:
            found_key = True
            print "You have entered the", room['name'], "and found the key!"
            time.sleep(1)
            print("Hurry back to the Entrance Way and escape!")
            time.sleep(1)

        elif found_key and room['name'] == room_with_key['name']:
            print("You're back in the",room_with_key['name'],"!")
            print("You've already found the key here! Find the entrance so you can escape!")


        #STORIES IN EACH ROOM

        else:
#ROOMS: entrance, dungeon, hallway, trophyroom, dininghall, closet, courtyard, weaponry, armory
            if room['name'] == 'Entrance Way':
                rooms_entered.append('Entrance Way')
                print("You are currently in the Entrance Way.")
                time.sleep(1)
                print("To your left is a large iron box, and to your right is an enormous dresser.")
                time.sleep(1)
                choice = raw_input("Which one do you want to open? (box or dresser)")
                if choice == 'box':
                    print("You have opened the box!")
                    time.sleep(1)
                    print("Inside, you find notebooks with scribbles of writing.")
                    time.sleep(1)
                    print("It looks like observations of an event.")
                    time.sleep(1)
                else:
                    print("You open the dresser!")
                    time.sleep(1)
                    print("You find hiking clothes and a camera in the corner.")

            if room['name'] == 'Trophy Room':
                rooms_entered.append('Trophy Room')
                print("You enter a huge, round room with the highest ceiling you've ever seen.")
                time.sleep(1)
                print("The glass cases around you appear to hold medals and awards.")
                time.sleep(1)
                choice4 = raw_input("Do you want to explore the trophy case or the set of drawers? (case or drawers)")
                if choice4 == 'drawers':
                    print("You open the drawers and find news articles from the 'New York Times'")
                    time.sleep(1)
                    print("The pages are too faded to make out the author's name.")
                    time.sleep(1)
                else:
                    print("The largest trophy in the case appears to be...A Pulitzer Prize?")
                    time.sleep(1)
                    print("You can't seem to make out the name at the bottom.")
                    time.sleep(1)

            if room['name'] == 'Dining Hall':
                rooms_entered.append('Dining Hall')
                print("You enter the Dining Hall.")
                time.sleep(1)
                print("The surface of the table appears to be covered with a giant world map.")
                time.sleep(1)
                choice5 = raw_input("You're really hungry - do you want to grab something to eat? (yes or no)")
                if choice5 == 'yes':
                    print("You open the fridge. The only thing in there is milk...spoiled milk.")
                    time.sleep(1)
                    choice6 = raw_input("Do you want to chug the spoiled milk anyway? (yes or no)")
                    if choice6 == 'yes':
                        print("Why would you drink spoiled milk???")
                        time.sleep(1)
                        print("You made it this far only to die of food poisoning?")
                        time.sleep(1)
                        print("GAME OVER!! Better luck next time!")
                        exit(gameIsPlaying)
                    else:
                        print("Good choice. Moving on...")


                else:
                    print("Okay. You try to leave, but the door slams in front of you.")
                    time.sleep(1)
                    print("Kim Kardashian appears. She won't let you out...")
                    time.sleep(1)
                    print("...Unless you answer her trivia question correctly!")
                    question = raw_input("What is the capital of Arkansas? (answer in all lowercase)")
                    if question == 'little rock':
                        print("That's correct! You outsmarted Kim Kardashian and escaped the Dining Hall!")
                        time.sleep(1)
                    else:
                        print("That's incorrect!")
                        time.sleep(1)
                        print("You failed to outsmart Kim Kardashion!")
                        time.sleep(1)
                        print("GAME OVER!")
                        exit(gameIsPlaying)

            if room['name'] == 'Closet':
                rooms_entered.append('Closet')
                print("You're in the Storage Closet.")
                time.sleep(1)
                print("There's a cardboard box on the shelf above you, and a plastic bag by your feet.")
                time.sleep(1)
                choice7 = raw_input("Which one do you want to open? (box or bag)")
                time.sleep(1)
                if choice7 == 'box':
                    print("You open the box.")
                    time.sleep(1)
                    print("To your surprise, it's full of old video cameras.")
                    time.sleep(1)
                else:
                    print("You open the bag.")
                    time.sleep(1)
                    print("Weirdly, it's full of ruined film.")
                    time.sleep(1)

            if room['name'] == 'Courtyard':
                rooms_entered.append('Courtyard')
                print("You enter a large, open courtyard.")
                time.sleep(1)
                print("There's a tripod in the corner, and a box of chalk on the ground.")
                time.sleep(1)
                print("Something's written on the ground a few feet away.")
                time.sleep(1)
                choice8 = raw_input("Do you want to see what it says? (yes or no)")
                if choice8 == 'yes':
                    print("OH NO! It's a trap...the chalk is rigged!")
                    time.sleep(1)
                    print("Kanye West appears and challenges you to a game of Tic Tac Toe...")
                    time.sleep(1)
                    print("...to the DEATH!")
                    time.sleep(1)
                #TIC TAC TOE CODE
                    def drawBoard(board):
                        # This function prints out the board that it was passed.

                        # "board" is a list of 10 strings representing the board (ignore index 0)
                        print('   |   |')
                        print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
                        print('   |   |')
                        print('-----------')
                        print('   |   |')
                        print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
                        print('   |   |')
                        print('-----------')
                        print('   |   |')
                        print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
                        print('   |   |')

                    def inputPlayerLetter():
                        # Let's the player type which letter they want to be.
                        # Returns a list with the player's letter as the first item, and the computer's letter as the second.
                        letter = ''
                        while not (letter == 'X' or letter == 'O'):
                            print("The board works like this:")
                            print(" 7  8  9 ")
                            print(" 4  5  6 ")
                            print(" 1  2  3 ")
                            print('Do you want to be X or O?')
                            letter = raw_input().upper()

                        # the first element in the tuple is the player's letter, the second is the computer's letter.
                        if letter == 'X':
                            return ['X', 'O']
                        else:
                            return ['O', 'X']

                    def whoGoesFirst():
                        # Randomly choose the player who goes first.
                        if random.randint(0, 1) == 0:
                            return 'Kanye'
                        else:
                            return 'You'

                    def makeMove(board, letter, move):
                        board[move] = letter

                    def isWinner(bo, le):
                        # Given a board and a player's letter, this function returns True if that player has won.
                        # We use bo instead of board and le instead of letter so we don't have to type as much.
                        return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
                                (bo[4] == le and bo[5] == le and bo[6] == le) or  # across the middle
                                (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom
                                (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the left side
                                (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the middle
                                (bo[9] == le and bo[6] == le and bo[3] == le) or  # down the right side
                                (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
                                (bo[9] == le and bo[5] == le and bo[1] == le))  # diagonal

                    def getBoardCopy(board):
                        # Make a duplicate of the board list and return it the duplicate.
                        dupeBoard = []

                        for i in board:
                            dupeBoard.append(i)

                        return dupeBoard

                    def isSpaceFree(board, move):
                        # Return true if the passed move is free on the passed board.
                        return board[move] == ' '

                    def getPlayerMove(board):
                        # Let the player type in his move.
                        move = ' '
                        while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
                            print('What is your next move? (1-9)')
                            move = raw_input()
                        return int(move)

                    def chooseRandomMoveFromList(board, movesList):
                        # Returns a valid move from the passed list on the passed board.
                        # Returns None if there is no valid move.
                        possibleMoves = []
                        for i in movesList:
                            if isSpaceFree(board, i):
                                possibleMoves.append(i)

                        if len(possibleMoves) != 0:
                            return random.choice(possibleMoves)
                        else:
                            return None

                    def getComputerMove(board, computerLetter):
                        # Given a board and the computer's letter, determine where to move and return that move.
                        if computerLetter == 'X':
                            playerLetter = 'O'
                        else:
                            playerLetter = 'X'

                        # Here is our algorithm for our Tic Tac Toe AI:
                        # First, check if we can win in the next move
                        for i in range(1, 10):
                            copy = getBoardCopy(board)
                            if isSpaceFree(copy, i):
                                makeMove(copy, computerLetter, i)
                                if isWinner(copy, computerLetter):
                                    return i

                        # Check if the player could win on his next move, and block them.
                        for i in range(1, 10):
                            copy = getBoardCopy(board)
                            if isSpaceFree(copy, i):
                                makeMove(copy, playerLetter, i)
                                if isWinner(copy, playerLetter):
                                    return i

                        # Try to take one of the corners, if they are free.
                        move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
                        if move != None:
                            return move

                        # Try to take the center, if it is free.
                        if isSpaceFree(board, 5):
                            return 5

                        # Move on one of the sides.
                        return chooseRandomMoveFromList(board, [2, 4, 6, 8])

                    def isBoardFull(board):
                        # Return True if every space on the board has been taken. Otherwise return False.
                        for i in range(1, 10):
                            if isSpaceFree(board, i):
                                return False
                        return True

                    print('May the best man win!')

                    while True:
                        # Reset the board
                        theBoard = [' '] * 10
                        playerLetter, computerLetter = inputPlayerLetter()
                        turn = whoGoesFirst()
                        print(turn + ' will go first.')
                        gameIsGoing = True

                        while gameIsGoing:
                            if turn == 'player':
                                # Player's turn.
                                drawBoard(theBoard)
                                move = getPlayerMove(theBoard)
                                makeMove(theBoard, playerLetter, move)

                                if isWinner(theBoard, playerLetter):
                                    drawBoard(theBoard)
                                    print('Hooray! You have won the game and escaped the Courtyard!')
                                    gameIsGoing = False
                                else:
                                    if isBoardFull(theBoard):
                                        drawBoard(theBoard)
                                        print('The game is a tie! You have failed to escape!')
                                        time.sleep(1)
                                        print("GAME OVER! Better luck next time!")
                                        exit(gameIsPlaying)
                                    else:
                                        turn = 'computer'

                            else:
                                # Computer's turn.
                                move = getComputerMove(theBoard, computerLetter)
                                makeMove(theBoard, computerLetter, move)

                                if isWinner(theBoard, computerLetter):
                                    drawBoard(theBoard)
                                    print('Kanye West has beaten you. You lose.')
                                    time.sleep(1)
                                    print("GAME OVER! Better luck next time!")
                                    exit(gameIsPlaying)
                                else:
                                    if isBoardFull(theBoard):
                                        drawBoard(theBoard)
                                        print('The game is a tie!')
                                        time.sleep(1)
                                        print("GAME OVER! Better luck next time!")
                                    else:
                                        turn = 'player'
                else:
                    print("Okay. You try to leave, but the gate won't open")
                    time.sleep(1)
                    print("Donald Trump appears. He won't let you out...")
                    time.sleep(1)
                    print("...Unless you answer his trivia question correctly!")
                    question = raw_input("Who was the shortest president? (madison, taft, or adams?)")
                    if question == 'madison':
                        print("That's correct! You outsmarted Donald Trump and escaped!")
                        time.sleep(1)
                    else:
                        print("That's incorrect!")
                        time.sleep(1)
                        print("You failed to outsmart Donald Trump!")
                        time.sleep(1)
                        print("GAME OVER!")
                        exit(gameIsPlaying)

            if room['name'] == 'Weaponry':
                rooms_entered.append('Weaponry')
                print("You enter a dimly lit, circular room.")
                time.sleep(1)
                print("It looks like...a Weaponry.")
                time.sleep(1)
                print("You find an envelope of old pictures, and a light switch.")
                time.sleep(1)
                choice10 = raw_input("Do you want to turn the lights on? (yes or no)")
                if choice10 == 'yes':
                    print("The lights become stronger, and you see a rope near your feet...")
                    time.sleep(1)
                    print("and...you find yourself lifted off the ground!")
                    time.sleep(1)
                    print("OH NO! Brad Pitt is here...He's challenged you to a real life game of HANGMAN!")
                    time.sleep(1)
                    #HANGMAN GAME
                    def main():
                        print('A word will be chosen at random.')
                        time.sleep(1)
                        print('You must try to guess the word correctly letter by letter...')
                        time.sleep(1)
                        print('...before you run out of attempts. Good luck!')
                        time.sleep(1),
                        # setting up the play_again loop

                        play_again = True

                        while play_again:
                            # set up the game loop

                            words = ["hangman", "chairs", "backpack", "bodywash", "clothing",
                                     "computer", "python", "program", "glasses", "sweatshirt",
                                     "sweatpants", "mattress", "friends", "clocks", "biology",
                                     "algebra", "suitcase", "knives", "ninjas", "shampoo"
                                     ]

                            chosen_word = random.choice(words).lower()
                            player_guess = None  # will hold the players guess
                            guessed_letters = []  # a list of letters guessed so far
                            word_guessed = []
                            for letter in chosen_word:
                                word_guessed.append("-")  # create an unguessed, blank version of the word
                            joined_word = None  # joins the words in the list word_guessed

                            HANGMAN = (
                                """
                                -----
                                |   |
                                |
                                |
                                |
                                |
                                |
                                |
                                |
                                --------
                                """,
                                """
                                -----
                                |   |
                                |   0
                                |
                                |
                                |
                                |
                                |
                                |
                                --------
                                """,
                                """
                                -----
                                |   |
                                |   0
                                |  -+-
                                |
                                |
                                |
                                |
                                |
                                --------
                                """,
                                """
                                -----
                                |   |
                                |   0
                                | /-+-
                                |
                                |
                                |
                                |
                                |
                                --------
                                """,
                                """
                                -----
                                |   |
                                |   0
                                | /-+-\ 
                                |
                                |
                                |
                                |
                                |
                                --------
                                """,
                                """
                                -----
                                |   |
                                |   0
                                | /-+-\ 
                                |   | 
                                |
                                |
                                |
                                |
                                --------
                                """,
                                """
                                -----
                                |   |
                                |   0
                                | /-+-\ 
                                |   | 
                                |   | 
                                |
                                |
                                |
                                --------
                                """,
                                """
                                -----
                                |   |
                                |   0
                                | /-+-\ 
                                |   | 
                                |   | 
                                |  |
                                |
                                |
                                --------
                                """,
                                """
                                -----
                                |   |
                                |   0
                                | /-+-\ 
                                |   | 
                                |   | 
                                |  | 
                                |  | 
                                |
                                --------
                                """,
                                """
                                -----
                                |   |
                                |   0
                                | /-+-\ 
                                |   | 
                                |   | 
                                |  | | 
                                |  | 
                                |
                                --------
                                """,
                                """
                                -----
                                |   |
                                |   0
                                | /-+-\ 
                                |   | 
                                |   | 
                                |  | | 
                                |  | | 
                                |
                                --------
                                """)

                            print(HANGMAN[0])
                            attempts = len(HANGMAN) - 1

                            while (attempts != 0 and "-" in word_guessed):
                                print(("\nYou have {} attempts remaining").format(attempts))
                                joined_word = "".join(word_guessed)
                                print(joined_word)

                                try:
                                    player_guess = str(raw_input("\nPlease select a letter between A-Z" + "\n> ")).lower()
                                except:  # check valid input
                                    print("That is not valid input. Please try again.")
                                    continue
                                else:
                                    if not player_guess.isalpha():  # check the input is a letter. Also checks an input has been made.
                                        print("That is not a letter. Please try again.")
                                        continue
                                    elif len(player_guess) > 1:  # check the input is only one letter
                                        print("That is more than one letter. Please try again.")
                                        continue
                                    elif player_guess in guessed_letters:  # check it letter hasn't been guessed already
                                        print("You have already guessed that letter. Please try again.")
                                        continue
                                    else:
                                        pass

                                guessed_letters.append(player_guess)

                                for letter in range(len(chosen_word)):
                                    if player_guess == chosen_word[letter]:
                                        word_guessed[
                                            letter] = player_guess  # replace all letters in the chosen word that match the players guess

                                if player_guess not in chosen_word:
                                    attempts -= 1
                                    print(HANGMAN[(len(HANGMAN) - 1) - attempts])

                            if "-" not in word_guessed:  # no blanks remaining
                                print "\nCongratulations! {} was the word!".format(chosen_word)
                                time.sleep(1)
                                print "You've beaten Brad Pitt and escaped the Weaponry!"
                                break
                            else:  # loop must have ended because attempts reached 0
                                print "\nUnlucky! The word was {}.".format(chosen_word)
                                time.sleep(1)
                                print "Brad Pitt beat you!"
                                time.sleep(1)
                                print "GAME OVER! Better luck next time!"
                                exit(gameIsPlaying)

                    if __name__ == "__main__":
                        main()

                else:
                    print("Okay, your choice.")
                    time.sleep(1)
                    print("But if you can't see anything, you can't go anywhere!")
                    time.sleep(1)
                    print("Bill and Melinda Gates appear.")
                    time.sleep(1)
                    print("They offer to give you some light...")
                    time.sleep(1)
                    print("...But you need to answer their trivia question!")
                    question = raw_input("Around how many billions is Bill Gates worth? (90, 103, or 120?)")
                    time.sleep(1)
                    if question == '103':
                        print("That's correct! You outsmarted Bill and Melinda and escaped!")
                        time.sleep(1)
                    else:
                        print("That's incorrect!")
                        time.sleep(1)
                        print("You failed to outsmart Bill and Melinda!")
                        time.sleep(1)
                        print("GAME OVER!")
                        exit(gameIsPlaying)

            if room['name'] == 'Armory':
                print("You enter the armory.")
                time.sleep(1)
                print("All around you are suits of chain mail.")
                time.sleep(1)
                choice10 = raw_input("Do you want to go left or right?")
                if choice10 == 'left':
                    print("You move to your left and trip over an old helmet...")
                    time.sleep(1)
                    print("Falling directly on a trapdoor.")
                    time.sleep(1)
                    choice11 = raw_input("Do you want to open it? (yes or no)")
                    if choice11 == 'yes':
                        print("You swing the trapdoor open and descend some stairs.")
                        time.sleep(1)
                        print("Here, you find dozens of pictures covering the walls...")
                        time.sleep(1)
                        print("All pictures of YOU!")
                        time.sleep(1)
                        choice13 = raw_input("Do you want to run away in panic or stand there? (run or stand)")
                        if choice13 == 'run':
                            print("You sprint up the stairs and out the door.")
                        else:
                            print("Too bad, you don't have the time!")
                            time.sleep(1)
                            print("You sprint up the stairs to keep looking for the key.")
                    else:
                        print("Okay. You try to get up to leave...")
                        time.sleep(1)
                        print("and Mark Zuckerberg, who just appeared, won't let you,")
                        time.sleep(1)
                        print("unless you answer his trivia question correctly!")
                        question = raw_input("What year was Facebook created? (2001, 2002, 2004)")
                        if question == '2004':
                            print("That's correct! You outsmarted Zuckerberg and escaped!")
                            time.sleep(1)
                        else:
                            print("That's incorrect!")
                            time.sleep(1)
                            print("You failed to outsmart Zuckerberg!")
                            time.sleep(1)
                            print("GAME OVER!")
                            exit(gameIsPlaying)

                else:
                    print("You move right and see what appears to be an old fashioned elevator.")
                    time.sleep(1)
                    choice12 = raw_input("Do you want to call the elevator? (yes or no)")
                    if choice12 == 'yes':
                        print("You call the elevator...")
                        time.sleep(1)
                        print("It arrives...but Darth Vader is inside!")
                        time.sleep(1)
                        print("The last thing you see is his lightsaber.")
                        time.sleep(1)
                        print("GAME OVER! Better luck next time!")
                        time.sleep(1)
                        exit(gameIsPlaying)
                    else:
                        print("A seemingly good choice, but as you try to leave...")
                        print("Jeff Bezos appears and demands you answer his trivia question.")
                        question = raw_input("Around how many square miles does the Amazon rainforest occupy?(2, 4, or 5?)")
                        if question == '2':
                            print("That's correct! You outsmarted Jeff Bezos and escaped!")
                            time.sleep(1)
                        else:
                            print("That's incorrect!")
                            time.sleep(1)
                            print("You failed to outsmart Jeff Bezos!")
                            time.sleep(1)
                            print("GAME OVER!")
                            exit(gameIsPlaying)

            if room['name'] == 'Hallway':
                rooms_entered.append('Hallway')
                print("You enter a long, dark Hallway.")
                time.sleep(1)
                print("The only light comes from torches lining the walls.")
                time.sleep(1)
                print("The low flames illuminate several newspapers that have been ripped out and hung up.")
                time.sleep(1)
                choice3= raw_input("Do you want to grab a torch to help light your way? (yes or no)")
                if choice3 == 'yes':
                        print("You try to grab one, but before you can...")
                        time.sleep(1)
                        print("Steve Harvey appears and demands you answer his question...")
                        time.sleep(1)
                        print("...In return for the torch.")
                        question = raw_input("How many seasons does 'Friends' have? (8, 9, or 10)")
                        if question == '10':
                            print("That's correct! You outsmarted Steve Harvey and won the torch!")
                            time.sleep(1)
                        else:
                            print("That's incorrect!")
                            time.sleep(1)
                            print("You failed to outsmart Steve Harvey!")
                            time.sleep(1)
                            print("GAME OVER!")
                            exit(gameIsPlaying)
                else:
                    print("Okay. You stumble to the end of the hall in darkness.")
                    time.sleep(1)
                    print("There, you find Danny Devito, who challenges you to a game of dice...to the DEATH!")
                    time.sleep(1)
                    print("Six turns each.")
                    time.sleep(1)

                    def playerRoll():
                        num_rolled = random.randint(1, 6)
                        roll_again = raw_input("Press ENTER to roll!")
                        if roll_again.lower() != 'q':
                            print "You have rolled a",num_rolled,"."
                            player_rolls.append(num_rolled)

                    def computerMove():
                        print "Danny Devito will now roll."
                        number = random.randint(1, 6)
                        print "He rolled a",number,"."
                        computer_rolls.append(number)

                    player_rolls = []
                    computer_rolls = []
                    playing = True

                    while playing:
                        for x in range(0, 5):
                            sides = 6
                            playerRoll()
                            time.sleep(1)
                            computerMove()
                        print "Your total is", sum(player_rolls)
                        time.sleep(1)
                        print "Danny Devito's total is", sum(computer_rolls)
                        if sum(player_rolls) > sum(computer_rolls):
                            print("You have won and escaped the Hallway!")
                            break
                        else:
                            print("You didn't beat him!")
                            time.sleep(1)
                            print("GAME OVER! Better luck next time!")
                            exit(gameIsPlaying)

            if room['name'] == 'Dungeon':
                rooms_entered.append('Dungeon')
                print("You have entered the Dungeon. You see a secret door, labeled 'PHOTOGRAPHIC DARKROOM'.")
                time.sleep(1)
                choice2 = raw_input("Do you want to open it? (yes or no)")
                if choice2 == 'yes':
                    print("AH! The door slams shut behind you and you are trapped...")
                    time.sleep(1)
                    print("Barack Obama appears and condemns you to your fate...")
                    time.sleep(1)
                    print("Unless you can guess the number he's thinking of in 7 tries!")
                    time.sleep(1)

                    def valid_num(s):
                        if s.isdigit() and 1 <= int(s) <= 50:
                            return True
                        else:
                            return False

                    def numberGame():
                        number = random.randint(1, 50)
                        guessed_number = False
                        num_guesses = 0
                        guess = raw_input("Guess a number between 1 and 50!")
                        while not guessed_number:
                            if not valid_num(guess):
                                guess = raw_input("That doesn't count. A number between 1 and 50 please:")
                                continue
                            else:
                                num_guesses += 1
                                guess = int(guess)

                            if guess > number:
                                print "Too high. You have guessed",num_guesses, "time(s)."
                                guess = raw_input("Guess again:")
                            elif guess < number:
                                print "Too low. You have guessed ", num_guesses, "times."
                                guess = raw_input("Guess again:")

                            else:
                                print "You got Obama's number in", num_guesses, "guesses!"
                                guessed_number = True
                                if num_guesses > 7:
                                    print "But the limit was 7...YOU FAILED TO ESCAPE!"
                                    time.sleep(1)
                                    print "GAME OVER! Better luck next time!"
                                    exit(gameIsPlaying)
                                else:
                                    print("Congrats! You beat Obama's game and escaped the Dungeon!")

                    numberGame()



                else:
                    print("Okay. You try to leave, but your exit is blocked!")
                    time.sleep(1)
                    print("Taylor Swift appears. She won't let you out...")
                    time.sleep(1)
                    print("...Unless you answer her trivia question correctly!")
                    question = raw_input("How many cats does Taylor Swift have? (1, 2, 3)")
                    if question == '3':
                        print("That's correct! You outsmarted Taylor and escaped!")
                        time.sleep(1)
                    else:
                        print("That's incorrect!")
                        time.sleep(1)
                        print("You failed to outsmart Taylor!")
                        time.sleep(1)
                        print("GAME OVER!")
                        exit(gameIsPlaying)


        stuck = True
        while stuck:
            dir = raw_input("Which room (direction) do you want to go to: N,E,S, or W? ")
            choice= get_choice(room,dir)
            if choice == -1:
                print("Please enter N,E,S, or W ")
            elif choice == 4:
                print("You cannot go in the direction, it is a wall. Try another idea.")
            else:
                room = room['directions'][choice]
                stuck = False

main()

print("Thanks for playing!")