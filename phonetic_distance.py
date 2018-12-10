#!/usr/bin/env python
# -*- coding: utf-8 -*- 

phonetically_similar_segment = {

'𝘝':['i','ɪ','e', 'ɛ','æ','a','ə','ɔ','ɒ','ʌ','o','ʊ','u','ᴶa', 'ᴶe', 'ᴶo', 'ᴶi','ᴶo','ᴶu','ᵂa', 'ᵂe','ᵂi','ᵂo','ᵂu'],


'p':['b','f','pʰ','bʰ','p'], 
'b':['pʰ','bʰ','p','b','m'], 
'pʰ':['b','f','p','bʰ','pʰ'], 
'bʰ':['pʰ','b','p','bʰ'], 
'f':['p','v','θ','f'],

't':['tʰ','d','dʰ','z','k','t'],
'tʰ':['θ','ð','t','d','z','tʰ'], 
'd':['t','ð','d','z','d'],
'dʰ':['d','z','ð','dʰ'],

'r':['r',''], 

's':['z','θ','ð','ʒ','ʃ','h','s'],
'z':['θ','s','ð','ʒ','ʃ','z'],
'ð':['z','ʒ','ʃ','θ','s','ð'],
'θ':['z','θ','s','θ'],
'ʒ':['ʃ','d','z','θ','ð','ʒ'],
'ʃ':['ʒ','h','s','θ','ð','z','ʃ'],

'm':['n', 'nm', 'ŋ', 'm'],
'n':['m' , 'ŋ', 'n'],
'ŋ':['n' , 'm', 'ŋ'],

'w':['v', 'j', 'w'],
'v':['v','b', 'w'],

'k':['g','?', 'kʰ','kʷ','q','x', 'kʷ','k'],
'kʷ':['gʷ', 'kʰ','k','qʷ','x','q','kʷ'],
'kʰ':['gʰ','?','k','kʰ','kʷ','q','x', 'kʷ','h','kʰ'],
'g':['gʷ','gʰ', 'kʰ','kʷ','q','x','h','kʷ','g'],
'gʷ':['kʷ', 'h','kʰ','g','qʷ','q','gʷ'],
'gʰ':['kʰ','?','h','kʰ','gʰ'],

'?':['h','','x','?'],
'x':['k','kʰ','q','x'],
'q':['?','k','kʰ','kʷ','q'],
'h':['?', '', 'q', 'x' ,'gʰ','kʰ','s','h']
}

vowels = ('a','e','i','o','u','i','ɪ','e', 'ɛ','æ','a','ə','ɔ','ɒ','ʌ','o','ʊ','u','ᴶa', 'ᴶe', 'ᴶo', 'ᴶi','ᴶo','ᴶu','ᵂa', 'ᵂe','ᵂi','ᵂo','ᵂu')

def del_cost():
    return 1

def ins_cost():
    return 1


def sub_cost(source, target):
	if(target == source):
		return 0
	if source in vowels and target in vowels:
		return 1
	if source in phonetically_similar_segment:	
		if(target in phonetically_similar_segment[source]):
			return 1
	return 2


class Matrix:

    def __init__(self, nrow, ncol, default=None):
        self.list_of_lists = [[default] * (ncol) for i in range(nrow)]
        self.numRows = nrow
        self.numCols = ncol

    def nrow(self):
        return self.numRows

    def ncol(self):
        return self.numCols

    def __getitem__(self, index):
        return self.list_of_lists[index]

    def __str__(self):
        ret_string = "\n"
        for i in range(0, self.numRows):
            for j in range(0, self.numCols):
                ret_string += str(self.list_of_lists[i][j])
                if (j == self.numCols - 1):
                    ret_string += "\n"
                else:
                    ret_string += "\t"
        return ret_string


class Min_Edit_Distance_Calculator:

    def __init__(self, source, target):
        self.source = source
        self.target = target

    # initialize distance matrix: zero-th row and column
    def initialize_distance_matrix(self, distances):
        for i in range(0, distances.numRows):
            distances[i][0] = i
        for j in range(1, distances.numCols):
            distances[0][j] = j
        return distances

    # calculate recurrence
    def calculate_recurrence(self, distances):
        for i in range(1, distances.numRows):
            for j in range(1, distances.numCols):
                delete_cost = distances[i - 1][j] + del_cost()
                substitution_cost = (distances[i - 1][j - 1]) + sub_cost(self.source[i - 1], self.target[j - 1])
                insert_cost = (distances[i][j - 1]) + ins_cost()
                distances[i][j] = min(delete_cost, substitution_cost, insert_cost)
        return distances
    # minimum edit distance algorithm


def min_edit_distance(source, target):
	sourceLen, targetLen = len(source), len(target)
	if (sourceLen == 0):
		return targetLen
	if ((targetLen) == 0):
		return sourceLen

	dist = Matrix(sourceLen + 1, (targetLen) + 1)
	dist = (Min_Edit_Distance_Calculator(source, target).initialize_distance_matrix(dist))
	dist = Min_Edit_Distance_Calculator(source, target).calculate_recurrence(dist)
	return dist[sourceLen][(targetLen)]
