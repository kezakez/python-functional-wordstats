def excludeWords(x):
	return not x in ['a', 'an', 'the', 'on', 'in', 'for', 'and', 'to']

def getCounts(words):
	def count(word):
		return (word, words.count(word))
	return map(count, words)

def getLen(x):
	return x[1]

def compareSize(x, y):
	return	len(x) - len(y)

def stats(input):
	result = Statistics()

	nochars = input.replace(".", "").replace(",", "")
	words = nochars.split()
	bigwords = filter(excludeWords, words)

	wordsize = sorted(bigwords, compareSize)
	result.shortest = wordsize[0]
	result.longest = wordsize[len(wordsize)-1]
		
	wordcount = getCounts(bigwords)
	uniquewordCount = dict(wordcount)

	sortedwordcount = sorted(uniquewordCount.items(), cmp, getLen, True)
	result.wordcount = sortedwordcount[:10]

	return result
	
class Statistics:
	wordcount = {}
	shortest = ""
	longest = ""
