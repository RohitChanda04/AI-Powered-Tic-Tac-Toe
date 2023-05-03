# AI-Powered-Tic-Tac-Toe

AI bot, ***Jared***, working in the background of this simple AI implementation of the game, Tic-Tac-Toe.

A simple implementation of the ***"Tic Tac Toe"*** game made with love and passion in Python with a twist of Artificial Intelligence. Our AI bot, Jared, works on defeating the user in every which way possible. Can you defeat him?
Not to worry if you can't, you can tone down the capabilities of Jared according to your preference and beat him too!

>Special thanks to my friend and senior, ***Charly DeKoning***, for it was his idea that I should have the option of playing against AI too!

This is the complete version of the game which simply works on the background logic which basically just checks if the entered position is already taken, and update the board if not. The program then keeps on checking the current status of the game at every turn.

>Technology used: Python

>Platform: terminal/console/command prompt

>Framework used: None

>Solely because I wanted to keep this as a fairly straightforwarded application that could run on the terminal while taking the input                  from the user through built-in modules and packages of Python using prompts.

Although this could be implemented in a single Python script file, I have implemented the modular apporach so that it could be modified and new funcitonalities could be added to it easily.


>_________________________________________________________________________________________________________________________________________________________


## How to run the application

Just like how you need to have **JRE** installed on your system in order to run a Java application, you need not necessarily have **JDK** installed for just running a Java application; similarly, you need to have ***Python*** installed on youer system for running this application as it provides the environment for it to run.

Download the repository on to your system and extract the project files and folders from the zip folder to the location where you want it to be in. Open your terminal/console/command prompt and navigate to the folder where the project is, then run the following command -

>python RunTicTacToe.py

Once you hit 'enter', the game starts and you see a sequence of prompts as explained in the next section.


>_________________________________________________________________________________________________________________________________________________________


## Walkthrough

Following is the sequence of prompts you get to see when you run the application -

1. *Welcome to then game of Tic-Tac-Toe!*


2. *Game options :-*

   1. *Play a two-player game.*

   2. *Play against Jared, the AI-powered futuristic bot.*
   
   *Choose an option:*
   
>The two-player mode is exactly the same as the one in the repository, Tic-Tac-Toe.


3. *You are playing against the AI-powered futuristic bot, Jared!*
>This appears when the user selects the second option.


4. *Choose the difficulty level:*
    1. *Beginner*
    2. *Intermediate*
    3. *Expert*
    
>The user has to select the difficulty level here.


5. *Paths from here -*
    1. *Beginner level selected!*
    2. *Intermediate level selected!*
    3. *Expert level selected!*

>The beginner level activates if the user enters 1.

>The intermediate level activates if the user enters 2.

>The expert level activates if the user enters 3.


4. *Choose your sign "x" or "o":*
>Now, Player 1 would have to choose his/her sign and the program would automatically assign the other sign to Jared.


5. *Player 1, you have chosen "x".*
>If the user chooses 'x'.


6. *Jared is "o".*
>The program assigns 'o' automatically to Jared.


7. *Do you want to start first?*
>It is a yes/no question which sets the game accordingly. Suppose, if the user says 'yes', the game continues as follows...


8. *Enter the position numbers corresponding to those in the board below...*
>You see a demo board with the position numbers set to let the user understand the corresponding values.


9. *Okay, so presenting the empty board now...*
>Then you see an empty board which is the game board.


10. *Player 1, it's your turn...*
>The prompt notifies Player 1 that it's his/her turn now.


11. *Enter position between 1 and 9, both inclusive:*
>Player 1 would then have to enter a position as described above; the program would evaluate the input and provide suitable response.


And the game goes on like this until someone wins, or is a tie. After that the prompt would ask if they want to play another round like below :-
Like in the below example, Player 1 wins and the prompt says -

>Game over! Player 1 wins!

>Do you want to play again?

If the players say yes, then the game starts over again with the same sequence of options and prompts.


>_________________________________________________________________________________________________________________________________________________________


## MiniMax Algorithm

What is Aritificial Intelligence?

In simpler wrods, Aritificial Intelligence, or AI, is an implementation tier on top of the main tier to facilitate some task smartly. As for example, in this game, there should be a program that automatically detects what the player's move is going to be in the next state and take the appropriate step in the current state. In AI systems, we use **sensors** to sense and detect movement and change in the environment. These sensors send in the information to the system which in turn takes an appropriate step through something called as the ***actuator***. For instance, in a Vacuum Robot, sensors could be infrared signals, camera, etc.

In this application, we do not need such physical elements to implement AI. Rather we just need an algorithm that calculates the best move at every step. For this, I have implemented the *Minimax algorithm*. In this application, Minimax gets called every time Jared is playing. Some references to Minimax algorithm can be found below :-

- Wikipedia: [https://en.wikipedia.org/wiki/Minimax]
- GeeksForGeeks: [https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-1-introduction/]



>_________________________________________________________________________________________________________________________________________________________



## 3 Modes in the game

Since the Minimax algorithm always finds the ideal position and gives the best move, it is practically impossible to beat the AI bot, Jared unless the player playing the game is highly skilled at it and has a gameplan. This could be disheartening after a while and so, I have implemented 3 different levels in the game to help tone down Jared's capabilities according to the user's preference.

The 3 levels are :-

1. *Beginner:*
In this level, Jared picks up the position randomly without implementing the Minimax algorithm. To implement this, I have ussed the random package which randomly selects an index from the available ones.

2. *Intermediate:*
In this level, there is a list that contains 2 values: True and False. Jared picks one item randomly from this list. If the picked item is True, then Jared picks the index randomly as in the Beginner level, otherwise he goes AI.

3. *Expert:*
In this level, Jared always implements the Minimax algorithm to make a selection, hence it is almost impossible to beat him.



>_________________________________________________________________________________________________________________________________________________________



## Error and Edge Case Handling

The prompt asks for appropirate input with the input range specified everytime. However, there could be typing errors from the users' end and so, the application is developed to be equipped to handle all the edge cases appropriately. The input range for the positions could only be 1 to 9, both inclusive. The prompt that asks the user to choose his/her sign could only rake in 'x' or 'o' as input, case insensitive. The prompt at the end of the game asks for a 'yes' or 'no', case insensitive.

There could be a variety of wrong inputs which could crash the application. Some of these are mentioned below :-
- What if the user enters an integer that is out of range of the input.
- What if the user enters 'a' instead of an integer.
- What if the user enters a digit instead of 'x' and 'o'.
- What if the user enters 'X' or 'O' when the prompt clearly mentions 'x' or 'o'.
- What if the user enters something other than 'yes' and 'no.

The application should be smart enough to take a valid input and process it accordingly. hence, the input is not restricted to case-sensitivity.



>_________________________________________________________________________________________________________________________________________________________



## Ending Note

I really hope this repository intrigues the mind for future possibilities. In this AI-version of the game, the user has an additional mode wherein he/she could play with the computer and select the difficulty of the game too. I highly encourage you to have a look at it and try your hands at beating Jared. I hope you learn something from this AI implementation of the simple game of Tic-Tac-Toe, and more importantly, I really hope that you have immense fun going through it. Otherwise, it's not worth it.

Happy learning, happy coding :)
