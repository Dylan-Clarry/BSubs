

# turns a list of words into a wordban
# return; set: workbank
def list_to_wordbank(words):

	wordbank = set()

	for word in words:
		if word not in wordbank:
			wordbank.add(word)

	return wordbank

# turns a wordbank into a string to be stored
# return; str: string
def wordbank_to_str(wordbank):

	string = ''
	i = 0
	for word in wordbank:
		string += word
		if i < len(wordbank) - 1:
			string += ':'
		i += 1
	return string

# turns a properly seperated sentence of words into a wordbank
# return; set: wordbank
def str_to_wordbank(string):
	words = string.split(':')
	return list_to_wordbank(words)

# determines if a sentence is 1T given a wordbank and a list of words from a sentence
# return; boolean
def is_one_target(wordbank, words):

	count = 0
	for word in words:
		if word not in wordbank:
			count += 1
		if count > 1:
			return False
	if count == 1:
		return True
	return False

# determines how many targets are in a given sentence given a wordbank and a list of words from a sentence
def how_many_targets(wordbank, words):

	count = len(words)

	for word in words:
		if word in wordbank:
			count -= 1
	return count

# adds all words to the wordbank
def add_words_to_wordbank(wordbank, words):
	for word in words:
		if word not in wordbank:
			worbank.add(word)

# for testing sentence miner functions
if __name__ == '__main__':

	words = ['你好', '漂亮', '我', '的']
	testlist = ['你好', '漂亮', '啊', '我']

	print('testing\n=======')

	wordbank = list_to_wordbank(words)
	print('wordbank:',  wordbank)
	print('testlist:',  testlist)

	print("is one target:", is_one_target(wordbank, testlist))
	print("how many targets:", how_many_targets(wordbank, testlist))

	string = wordbank_to_str(wordbank)
	print("wordbank to string:", string)

	wordbank = str_to_wordbank(string)
	print("string to wordbank:", wordbank)



