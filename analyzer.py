#!/usr/bin/env python
# -*- coding: utf-8 -*- 


import phonetic_distance
import re 


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

vowels = ('a','e','i','o','u')


def remove_vowel(word):
    return ''.join([l for l in word if l not in vowels])
def remove_spaces(word):
	word = word.strip()
	return ' '.join(word.split())
def preprocess(word):
	word = word.lower()
	consonant_roots = remove_vowel(word)
	trimmed = remove_spaces(consonant_roots)
	return trimmed
def tokenize(word):
	if(len(word) <1):
		return None
	tokenized = []
	for i in range(0, len(word) -1):
		if(word[i+1] == 'ʰ' or word[i+1] =='ʷ'):
			tokenized.append(word[i:i+2])
			i = i+1
		else:
			tokenized.append(word[i])
	if(word[len(word)-1] == 'ʰ' or word[len(word)-1] =='ʷ'):
		tokenized.append(word[len(word)-2:len(word)-1])
		del tokenized[len(tokenized)-2]
	else:
		tokenized.append(word[len(word)-1])
	return tokenized

word_1 = input("Enter your first word or phrase for analysis: ")
word_2 = input("Enter your second word or phrase for analysis: ")
word_1, word_2 = preprocess(word_1), preprocess(word_2)
print(tokenize(word_1))
