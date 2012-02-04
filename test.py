import wordsearch

input = "this is a test to see how well this search thing works. a word like test which is used multiple times in a test should test if the number of times test shows worked."

output = wordsearch.stats(input)

#print output.wordcount
assert len(output.wordcount) == 10

#print output.shortest
assert output.shortest == "is"

#print output.longest
assert output.longest == "multiple"
