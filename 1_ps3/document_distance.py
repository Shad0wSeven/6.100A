# 6.100A Fall 2023
# Problem Set 3
# Name: <insert name>
# Collaborators: <insert collaborators>

"""
Description:
	Computes the similarity between two texts using two different metrics:
	(1) shared words, and (2) term frequency-inverse document
	frequency (TF-IDF).
"""

import string
import math
import re

### DO NOT MODIFY THIS FUNCTION
def load_file(filename):
	"""
	Args:
		filename: string, name of file to read
	Returns:
		string, contains file contents
	"""
	# print("Loading file %s" % filename)
	inFile = open(filename, 'r')
	line = inFile.read().strip()
	for char in string.punctuation:
		line = line.replace(char, "")
	inFile.close()
	return line.lower()


### Problem 1: Prep Data ###
def prep_data(input_text):
	"""
	Args:
		input_text: string representation of text from file,
					assume the string is made of lowercase characters
	Returns:
		list representation of input_text, where each word is a different element in the list
	"""
	return input_text.split()


### Problem 2: Get Frequency ###
def get_frequencies(word_list):
	"""
	Args:
		word_list: list of strings, all are made of lowercase characters
	Returns:
		dictionary that maps string:int where each string
		is a word in l and the corresponding int
		is the frequency of the word in l
	"""
	outputDict = {}
	for word in word_list:
		if word in outputDict:
			outputDict[word] += 1
		else:
			outputDict[word] = 1
	return outputDict


### Problem 3: Get Words Sorted by Frequency
def get_words_sorted_by_frequency(frequencies_dict):
	"""
	Args:
		frequencies_dict: dictionary that maps a word to its frequency
	Returns:
		list of words sorted by decreasing frequency with ties broken
		by alphabetical order
	"""
	return sorted(frequencies_dict, key=lambda x: (-frequencies_dict[x], x))


### Problem 4: Most Frequent Word(s) ###
def get_most_frequent_words(dict1, dict2):
	"""
	The keys of dict1 and dict2 are all lowercase,
	you will NOT need to worry about case sensitivity.

	Args:
		dict1: frequency dictionary for one text
		dict2: frequency dictionary for another text
	Returns:
		list of the most frequent word(s) in the input dictionaries

	The most frequent word:
		* is based on the combined word frequencies across both dictionaries.
		  If a word occurs in both dictionaries, consider the sum the
		  frequencies as the combined word frequency.
		* need not be in both dictionaries, i.e it can be exclusively in
		  dict1, dict2, or shared by dict1 and dict2.
	If multiple words are tied (i.e. share the same highest frequency),
	return an alphabetically ordered list of all these words.
	"""
	combindedDict = {}
	for key in dict1:
		if key in combindedDict:
			combindedDict[key] += dict1[key]
		else:
			combindedDict[key] = dict1[key]
	for key in dict2:
		if key in combindedDict:
			combindedDict[key] += dict2[key]
		else:
			combindedDict[key] = dict2[key]
	return sorted([key for key in combindedDict if combindedDict[key] == max(combindedDict.values())])

### Problem 5: Similarity ###
def calculate_similarity_score(dict1, dict2):
	"""
	The keys of dict1 and dict2 are all lowercase,
	you will NOT need to worry about case sensitivity.

	Args:
		dict1: frequency dictionary of words of text1
		dict2: frequency dictionary of words of text2
	Returns:
		float, a number between 0 and 1, inclusive
		representing how similar the words/texts are to each other

		The difference in words/text frequencies = DIFF sums "frequencies"
		over all unique elements from dict1 and dict2 combined
		based on which of these three scenarios applies:
		* If an element occurs in dict1 and dict2 then
		  get the difference in frequencies
		* If an element occurs only in dict1 then take the
		  frequency from dict1
		* If an element occurs only in dict2 then take the
		  frequency from dict2
		 The total frequencies = ALL is calculated by summing
		 all frequencies in both dict1 and dict2.
		Return 1-(DIFF/ALL) rounded to 2 decimal places
	"""
	diff = 0
	for key in dict1:
		if key in dict2:
			diff += abs(dict1[key] - dict2[key])
		else:
			diff += dict1[key]
	for key in dict2:
		if key not in dict1:
			diff += dict2[key]
	all = sum([dict1[key] for key in dict1]) + sum([dict2[key] for key in dict2])
	return round(1 - (diff / all), 2)
	


### Problem 6: Finding TF-IDF ###
def get_tf(text_file):
	"""
	Args:
		text_file: name of file in the form of a string
	Returns:
		a dictionary mapping each word to its TF

	* TF is calculated as TF(i) = (number times word *i* appears
		in the document) / (total number of words in the document)
	* Think about how we can use get_frequencies from earlier
	"""
	returnDict = {}
	dict = get_frequencies(prep_data(load_file(text_file)))
	print(dict)
	for key in dict:
		returnDict[key] = dict[key] / sum([dict[key] for key in dict])
	return returnDict


def get_idf(text_files):
	"""
	Args:
		text_files: list of names of files, where each file name is a string
	Returns:
	   a dictionary mapping each word to its IDF

	* IDF is calculated as IDF(i) = log_10(total number of documents / number of
	documents with word *i* in it), where log_10 is log base 10 and can be called
	with math.log10()

	"""
	dict = {}
	for file in text_files:
		for key in get_frequencies(prep_data(load_file(file))):
			if key in dict:
				dict[key] += 1
			else:
				dict[key] = 1
	for key in dict:
		dict[key] = math.log10(len(text_files) / dict[key])
	return dict


def get_tfidf(text_file, text_files):
	"""
	Args:
		text_file: name of file in the form of a string (used to calculate TF)
		text_files: list of names of files, where each file name is a string
		(used to calculate IDF)
	Returns:
	   a sorted list of tuples (in increasing TF-IDF score), where each tuple is
	   of the form (word, TF-IDF). In case of words with the same TF-IDF, the
	   words should be sorted in increasing alphabetical order.

	* TF-IDF(i) = TF(i) * IDF(i)
	"""
	tf = get_tf(text_file)
	idf = get_idf(text_files)
	return sorted([(key, tf[key] * idf[key]) for key in tf], key=lambda x: (x[1], x[0]))


if __name__ == "__main__":
	pass
	##Uncomment the following lines to test your implementation
	# Tests Problem 1: Prep Data
	test_directory = "tests/student_tests/"
	hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
	world, friend = prep_data(hello_world), prep_data(hello_friend)
	# print(world) ## should print ['hello', 'world', 'hello', 'there']
	# print(friend) ## should print ['hello', 'friends']

	## Tests Problem 2: Get Frequencies
	world_word_freq = get_frequencies(world)
	friend_word_freq = get_frequencies(friend)
	# print(world_word_freq) ## should print {'hello': 2, 'world': 1, 'there': 1}
	# print(friend_word_freq) ## should print {'hello': 1, 'friends': 1}

	# ## Tests Problem 3: Get Words Sorted by Frequency
	world_words_sorted_by_freq = get_words_sorted_by_frequency(world_word_freq)
	friend_words_sorted_by_freq = get_words_sorted_by_frequency(friend_word_freq)
	# print(world_words_sorted_by_freq) ## should print ['hello', 'there', 'world']
	# print(friend_words_sorted_by_freq) ## should print ['friends', 'hello']

	## Tests Problem 4: Most Frequent Word(s)
	freq1, freq2 = {"hello":5, "world":1}, {"hello":1, "world":5}
	most_frequent = get_most_frequent_words(freq1, freq2)
	# print(most_frequent) ## should print ["hello", "world"]

	## Tests Problem 5: Similarity
	test_directory = "tests/student_tests/"
	hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
	world, friend = prep_data(hello_world), prep_data(hello_friend)
	world_word_freq = get_frequencies(world)
	friend_word_freq = get_frequencies(friend)
	word_similarity = calculate_similarity_score(world_word_freq, friend_word_freq)
	# print(word_similarity)        # should print 0.33

	## Tests Problem 6: Find TF-IDF
	text_file = 'tests/student_tests/hello_world.txt'
	text_files = ['tests/student_tests/hello_world.txt', 'tests/student_tests/hello_friends.txt']
	tf = get_tf(text_file)
	idf = get_idf(text_files)
	tf_idf = get_tfidf(text_file, text_files)
	# print(tf) ## should print {'hello': 0.5, 'world': 0.25, 'there': 0.25}
	# print(idf) ## should print {'there': 0.3010299956639812, 'world': 0.3010299956639812, 'hello': 0.0, 'friends': 0.3010299956639812}
	print(tf_idf) ## should print [('hello', 0.0), ('there', 0.0752574989159953), ('world', 0.0752574989159953)]