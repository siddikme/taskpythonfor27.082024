def stutter(word):
	stut = word[0:2]
	return_string = "{0}... {0}... {1}?".format(stut, word)
	return return_string
def stutter(word):
	stut = word[0:2]
	return "{0}... {0}... {1}?".format(stut, word)
def stutter(word):
	return "{0}... {0}... {1}?".format(word[0:2], word)
a = input("-> ")
print(stutter(a))