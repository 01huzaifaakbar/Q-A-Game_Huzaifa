Kids Game Collection - Quick Docs
A simple command-line Python program with 5 mini-games for kids, all played by typing answers in the
terminal.

How it works (big picture)
1 main() runs in a loop: show a menu, ask the player to pick a game, run that game, repeat.
2 Each game is its own function (count_and_clap(), guess_the_animal(), etc.)
3 slow_print() is a helper that prints text one letter at a time, like a typewriter, to make it feel more fun for
kids

The Games

Function

count_and_clap()

guess_the_animall)

fast_math()

Helper Functions
slow_print(text, delay) -prints text character-by-character for a friendly effect
get_int(prompt, lo, hi)-keeps asking until the user types a valid number in range (used by
shape_drawer)
farewell[) - prints goodbye and exits the program
welcome[) / menu() - print the intro message and the game menu

How to Run It
python3 game_collection.py
Then type a number (1-5) to play a game, or q to quit.

Key Beginner Concepts Used Here
random.randint() / random.choice[) - picking random numbers/items
input() - reading what the player types
while True loop -keeps the menu running until they quit
try/except - catches errors if someone types letters instead of numbers
Functions - each game is broken into its own reusable function, keeping code organized

3

4

What it does

Picks a random number (3-12) and asks the child to count up to it
Shows a riddle from the ANIMALS list; child guesses the animal
Asks 5 quick addition/subtraction questions and tracks score
Shows a growing sequence of colors; child repeats it back (like Simon Says)
Draws a square, triangle, or rectangle using " characters
