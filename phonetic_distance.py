#!/usr/bin/env python
# -*- coding: utf-8 -*- 
phonetically_similar_segment = {

'p':['b','f','pʰ','bʰ'], 
'b':['pʰ','bʰ','p','m'], 
'pʰ':['b','f','p','bʰ'], 
'bʰ':['pʰ','b','p','m'], 
'f':['p','v','θ'],

't':['tʰ','d','dʰ','z','k'],
'tʰ':['θ','ð','t','d','z'], 
'd':['t','z','dʰ'],
'dʰ':['ð','d','z'],
'dʰ':['d','z','ð'],


's':['z','θ','ð','ʒ','ʃ','h'],
'z':['θ','s','ð','ʒ','ʃ'],
'ð':['z','ʒ','ʃ','θ','s'],
'θ':['z','θ','s'],
'ʒ':['ʃ','d','z','θ','ð'],
'ʃ':['ʒ','h','s','θ','ð','z'],


'm':['n' , 'ŋ'],
'n':['m' , 'ŋ'],
'ŋ':['n' , 'm'],

'w':['v'],
'v':['v','b'],

'k':['g','?', 'kʰ','kʷ','q','x', 'kʷ'],
'kʷ':['gʷ', 'kʰ','k','qʷ','x','q'],
'kʰ':['gʰ','?','k','kʰ','kʷ','q','x', 'kʷ','h'],
'g':['gʷ','gʰ', 'kʰ','kʷ','q','x','h','kʷ'],
'gʷ':['kʷ', 'h','kʰ','g','qʷ','q'],
'gʰ':['kʰ','?','h','kʰ'],

'?':['h','','x'],
'x':['k','kʰ','q'],
'q':['?','k','kʰ','kʷ'],
'h':['?', '', 'q', 'x' ,'gʰ','kʰ','s']
}

def del_cost():
    return 1


def ins_cost():
    return 1


def sub_cost(source, target):
    if (target not in phonetically_similar_segment[source]):
        return 2
    return 0


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
                delete_cost = distances[i - 1][j] + del_cost(self.source[i - 1])
                substitution_cost = (distances[i - 1][j - 1]) + sub_cost(self.source[i - 1], self.target[j - 1])
                insert_cost = (distances[i][j - 1]) + ins_cost(self.target[j - 1])
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
