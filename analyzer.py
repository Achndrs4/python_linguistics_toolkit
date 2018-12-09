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

def remove_vowel(word, vowels=b'aeiou'):
    return word.translate(None, vowels)

def tokenize(word_1, word_2):
	word_1, word_2 = word_1.lower(), word_2.lower()
	print(remove_vowel(word_1))
	
	

word_1 = input("Enter your first word or phrase for analysis")
word_2 = input("Enter your second word or phrase for analysis")

tokenize(word_1, word_2)


