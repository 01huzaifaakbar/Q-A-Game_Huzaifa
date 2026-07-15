#!/usr/bin/env python3
"""
Kids Game Collection

A simple text-based collection of mini-games for children.
Run and follow on-screen prompts. Designed to be friendly and safe.
"""

import random
import time
import sys


def slow_print(text, delay=0.02):
	for ch in text:
		print(ch, end='', flush=True)
		time.sleep(delay)
	print()


def welcome():
	slow_print("Welcome to the Kids Game Collection!")
	slow_print("Choose a game and have fun. Type the number to play, or q to quit.")


def menu():
	print("\nGames:")
	print("1) Count and Clap (counting practice)")
	print("2) Guess the Animal (riddle + guess)")
	print("3) Fast Math (simple add/subtract)")


def count_and_clap():
	slow_print("Let's practice counting! I will ask you to count to a number.")
	n = random.randint(3, 12)
	slow_print(f"Count up to {n} out loud, clap your hands at each number! Ready? (press Enter)")
	input()
	slow_print("Start counting now:")
	for i in range(1, n+1):
		slow_print(str(i), delay=0.1)
		time.sleep(0.2)
	slow_print("Great job! You counted and clapped.\n")


ANIMALS = [
	("I have a mane and I roar. I am the king of the jungle.", "lion"),
	("I like to hop and I have long ears.", "rabbit"),
	("I am big, gray and have a trunk.", "elephant"),
	("I say meow and I like milk.", "cat"),
	("I say woof and I wag my tail.", "dog"),
]


def guess_the_animal():
	riddle, answer = random.choice(ANIMALS)
	slow_print("Guess the Animal!")
	slow_print("Here is a hint:")
	slow_print(riddle)
	guess = input("Your guess: ").strip().lower()
	if guess == answer:
		slow_print("Correct! Well done!\n")
	else:
		slow_print(f"Nice try. The answer was: {answer}.\n")


def fast_math():
	slow_print("Fast Math: Answer simple addition or subtraction questions.")
	score = 0
	for i in range(5):
		a = random.randint(1, 10)
		b = random.randint(1, 10)
		op = random.choice(['+', '-'])
		if op == '-':
			a, b = max(a, b), min(a, b)
		correct = a + b if op == '+' else a - b
		ans = None
		try:
			ans = int(input(f"Question {i+1}: {a} {op} {b} = "))
		except ValueError:
			slow_print("That's not a number. Moving on.")
		if ans == correct:
			slow_print("Great! That's correct.")
			score += 1
		else:
			slow_print(f"Oops, the correct answer was {correct}.")
	slow_print(f"You got {score}/5 correct!\n")
	
def main():
	welcome()
	while True:
		menu()
		choice = input("Pick a game: ").strip().lower()
		if choice == '1':
			count_and_clap()
		elif choice == '2':
			guess_the_animal()
		elif choice == '3':
			fast_math()
		else:
			slow_print("I didn't understand that. Try again.")


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print('\nGoodbye!')
