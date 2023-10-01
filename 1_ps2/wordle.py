# Problem Set 2, wordle.py
# Name: Ayush Nayak
# Collaborators: None
# Time spent: 1 hour

# Wordle Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
	"""
	Returns a list of valid words. Words are strings of lowercase letters.
	
	Depending on the size of the word list, this function may
	take a while to finish.
	"""
	print("Loading word list from file...")
	# inFile: file
	inFile = open(WORDLIST_FILENAME, 'r')
	# line: string
	line = inFile.readline()
	# wordlist: list of strings
	wordlist = line.split()
	print("  ", len(wordlist), "words loaded.")
	return wordlist

def choose_word(wordlist):
	"""
	wordlist (list): list of words (strings)
	
	Returns a word from wordlist at random
	"""
	return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

def check_user_input(secret_word, user_guess):
	"""
	:param secret_word: a string, the word to be guessed
	:param user_guess: a string, the users guess
	:return: False if user_guess does not satisfy at least
		one of the below conditions, True otherwise.
	1. must consist of only letters (uppercase or lowercase)
	2. must be the same length as secret_word
	3. must be a word found in words.txt
	"""
	user_guess = user_guess.lower()
	if len(user_guess) != len(secret_word):
		print("Oops! That word length is not correct.")
		return False
	if not user_guess.isalpha():
		print('Oops! That is not a valid word.')
		return False
	if user_guess not in wordlist:
		print("Oops! That is not a real word.")
		return False
	
	return True
	
	

def get_guessed_feedback(secret_word, user_guess):
	"""

	:param secret_word: a string, the word to be guessed
	:param user_guess: a string, a valid user guess
	:return: a string with uppercase and lowercase letters and 
		 underscores, each separated by a space (e.g. 'B _ _ S u')
	"""
	# print(secret_word, user_guess)
	secret_word = secret_word.lower()
	user_guess = user_guess.lower()
	out_list = []
	for i in range(len(user_guess)):
		if secret_word[i] == user_guess[i]:
			out_list.append(user_guess[i].upper())
		elif user_guess[i] in secret_word:
			out_list.append(user_guess[i].lower())
		else:
			out_list.append('_')
		
		
	return ' '.join(out_list)

def get_alphabet_hint(secret_word, all_guesses):
	"""
	takes in the secret word and a list of all previous guesses and returns a string of hint text
	:param secret_word: a string, the word to be guessed
	:param all_guesses: a list of all the previous valid guesses the user inputed
	:return: a string which replaces letters that were incorrect guesses with underscores and puts
		 semi-correct guesses (correct letter, incorrect place) in /x/
	"""
	# we have coded this for you
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	out_list = []
	for char in alphabet:
		out_list.append(" "+char+" ")

	for guess in all_guesses:
		for i, char in enumerate(list(guess)):
			if char not in secret_word:
				out_list[alphabet.find(char)]=" _ "
			elif char != secret_word[i]:
				out_list[alphabet.find(char)] = "/"+char+"/"
			elif char == secret_word[i]:
				if secret_word.count(char) > guess.count(char):
					out_list[alphabet.find(char)] = "/" + char + "/"
				else:
					out_list[alphabet.find(char)] = "|" + char.upper() + "|"
	return "".join(out_list)

def wordle(secret_word):
	'''
	secret_word: string, the secret word to guess.
	
	Starts up an interactive game of Wordle.
	
	* At the start of the game, let the user know how many letters the 
	  secret_word contains and how many guesses and warnings they start with.
	  
	* The user should start with 6 guesses and 3 warnings

	* Before each round, you should display to the user how many guesses
	  they have left.
	
	* Ask the user to supply one guess per round. Remember to make
	  sure that the user puts in a valid word!
	
	* The user should receive feedback immediately after each guess about 
	  whether their guess is valid, how closely it matches the secret_word,
	  and the alphabet hint.

	* After each guess, you should display to the user the progression of 
	  their partially guessed words so far.
	
	Follows the other limitations detailed in the problem write-up.
	'''
	print("Welcome to Wordle!")
	print("I am thinking of a word that is", len(secret_word), "letters long.")
	guesses = []
	number_of_guesses = 6
	warnings_left = 3
	print("You have", warnings_left, "warnings remaining.")
	while number_of_guesses > 0:
		print("You have", number_of_guesses, "guesses left.")
		# print("Available letters:", get_alphabet_hint(secret_word, guesses))
		guess = input("Please guess a word: ")
		if secret_word == guess.lower():
			print("Congratulations, you won!")
			print("You guessed correct the word in", (len(guesses) + 1), "tries!")
			print(f'Your total score for this game is: {(number_of_guesses - 1)*len(set(secret_word))}.')
			break
		if not check_user_input(secret_word, guess):
			if warnings_left != 0:
				warnings_left -= 1
			else:
				number_of_guesses -= 1
			print("You have", warnings_left, "warnings remaining.")
			print("----------")
			continue
		guesses.append(guess)
		for item in guesses:
			print(get_guessed_feedback(secret_word, item))
		print("Alphabet HINT:")
		print(get_alphabet_hint(secret_word, guesses))
		if(number_of_guesses > 1):
			print("----------------")

		number_of_guesses -= 1
	if number_of_guesses == 0:
		print(f'Sorry, you ran out of guesses. The word was {secret_word}.')
		


if __name__ == "__main__":
	# pass

	# To test, comment out the `pass` line above and uncomment:
	# - either of the `secret_word = ...` lines below, depending on how you want to set the secret_word
	# - the `wordle(secret_word)` line to run the game

	# uncomment and change the line below to a specific word for testing
	secret_word = "rink"

	# uncomment the line below for a randomly generated word
	# secret_word = choose_word(wordlist)

	wordle(secret_word)