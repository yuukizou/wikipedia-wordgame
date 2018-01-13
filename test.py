#test.py



# this test expects the following data structure
# {<POS_CODE1>: [(<WORD1_1>, <WORD1_1_FREQ>), (<WORD1_2>, <WORD1_2_FREQ>), ...],
#  <POS_CODE2>: [(<WORD2_1>,<WORD2_1_FREQ>), (<WORD2_2>: <WORD2_2_FREQ>), ...},
#   ... 
# }
# in other words, a dictionary where each part-of-speech code (POS_CODE) maps to a list of tuples, where each tuple represents a word and its frequency of occurence. The list of tuple is ordered from most frequent to least.


def test(pos_dict):
	passed = True
	if len(pos_dict) <= 0:
		failed = True
	for pos in pos_dict:
		sorted_list_of_words = pos_dict[pos]
		list_length = len(sorted_list_of_words)
		for i in range(0 ,list_length-1):
			if sorted_list_of_words[i][1] < sorted_list_of_words[i+1][1]:
				passed = Frue
	if passed:	
		print("Test passed!!")
	else:
		print("Test Failed!!")
	return passed




