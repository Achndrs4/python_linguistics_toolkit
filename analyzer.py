#!/usr/bin/env python
# -*- coding: utf-8 -*- 


import phonetic_distance
import re 
import itertools
import operator
import sys 
from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import Frame
from tkinter.ttk import Progressbar
from tkinter.ttk import Notebook
from tkinter import messagebox
from tkinter import Label
from PIL import ImageTk, Image


phonetically_similar_segment = {

'𝘝':['i','ɪ','e', 'ɛ','a','ə','ɔ','ɒ','ʌ','o','ʊ','u','ᴶa', 'ᴶe', 'ᴶo', 'ᴶi','ᴶo','ᴶu','ᵂa', 'ᵂe','ᵂi','ᵂo','ᵂu'],


'p':['b','f','pʰ','bʰ','p'], 
'b':['pʰ','bʰ','p','b','m'], 
'pʰ':['b','f','p','bʰ','pʰ'], 
'bʰ':['pʰ','b','p','bʰ'], 
'f':['p','v','θ','f'],

't':['tʰ','d','dʰ','z','k','t'],
'tʰ':['θ','ð','t','d','z','tʰ'], 
'd':['t','ð','d','z','d'],
'dʰ':['d','z','ð','dʰ'],

'r':['r','','l'], 
'l':['r','','l'],

's':['z','θ','ð','ʒ','ʃ','h','s'],
'z':['θ','s','ð','ʒ','ʃ','z'],
'ð':['z','ʒ','ʃ','θ','s','ð'],
'θ':['z','θ','s','θ'],
'ʒ':['ʃ','d','z','θ','ð','ʒ'],
'ʃ':['ʒ','h','s','θ','ð','z','ʃ'],

'm':['n', 'nm', 'ŋ', 'm', 'b'],
'mᴶ':['n', 'nm', 'ŋ', 'm', 'b'],
'n':['m' , 'ŋ', 'n'],
'ŋ':['n' , 'm', 'ŋ'],

'w':['v', 'j', 'w'],
'v':['v','b', 'w'],

'k':['g','?', 'kʰ','kʷ','q','x', 'kʷ','k', ''],
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

vowels = ('a','e','i','o','u','i','ɪ','e', 'ɛ','a','ə','ɔ','ɒ','ʌ','o','ʊ','u','ᴶa', 'ᴶe', 'ᴶo', 'ᴶi','ᴶo','ᴶu','ᵂa', 'ᵂe','ᵂi','ᵂo','ᵂu')



def replace_vowels(word):
	return_word = ""
	for letter in word:
		if letter in vowels:
			return_word = return_word + "𝘝"
		else:
			return_word = return_word + letter
	return return_word
def remove_spaces(word):
	word = word.strip()
	return ' '.join(word.split())
def preprocess(word):
	word = word.lower()
	consonant_roots = replace_vowels(word)
	trimmed = remove_spaces(consonant_roots)
	return trimmed
def tokenize(word):
	if(len(word) <1):
		return None
	tokenized = []
	i = 0
	while i < len(word)-1:
		if(word[i+1] == 'ʰ' or word[i+1] =='ʷ'):
			tokenized.append(word[i:i+2])
			i = i+2
		elif(word[i] == 'ᴶ'):
			tokenized.append(word[i:i+2])
			i = i+2
		else:
			tokenized.append(word[i])
			i = i +1
	if(word[len(word)-1] == 'ʰ' or word[len(word)-1] =='ʷ'):
		tokenized.append(word[len(word)-2:len(word)])
		del tokenized[len(tokenized)-2]
	else:
		tokenized.append(word[len(word)-1])
	return tokenized
	
def return_possibilities(tokens):
	array_of_arrays = []
	for token in tokens: 
		if token in phonetically_similar_segment:
			array_of_arrays.append(phonetically_similar_segment[token])
	return array_of_arrays

def cartesian_product(arrays):
	possibilities_list = []
	for element in itertools.product(*arrays):
		possibilities_list.append(''.join(element))
	return possibilities_list

def permutations_dictionary(tk1, permutations, dist):
	weights_dict = {}
	dist = int(dist.strip())
	for item in permutations:
		weights_dict[item] = (phonetic_distance.min_edit_distance(tokenize(item), tk1))
	return_array = []
	for k,v in weights_dict.items():
		if v == dist:
			return_array.append(k)
	if(len(return_array) == 0):
		return None
	return return_array

		
def find_matching(possibilities_list_1,possibilities_list_2, item_1,item_2, tk1, tk2):
	retString = ""
	print(possibilities_list_1)
	print(item_2)
	if item_2 in possibilities_list_1:
		retString = retString + ("Phonetic Relationship between two items found!\n")
		retString = retString + (str(tk1).replace("𝘝","V") + " - > " + str(tk2).replace("𝘝","V")+"\n")
		retString = retString + ("Weighted Levenshtien Distance...\t" + str(phonetic_distance.min_edit_distance(tk1, tk2))+"\n")
	elif item_1 in possibilities_list_2:
		retString = retString + ("Phonetic Relationship between two items found IN OPPOSITE DIRECTION\n")
		retString = retString + (str(tk2).replace("𝘝","V") + " - > " + str(tk1).replace("𝘝","V")+"\n")
		retString = retString + ("Weighted Levenshtien Distance...\t" + str(phonetic_distance.min_edit_distance(tk1, tk2)))
	else:
		retString = retString + ("No feasable relationship found between " + item_1 + " and " + item_2)
	return retString.replace("𝘝","V")
def generate():
	word = txt.get(1.0, END)
	word = preprocess(word)
	tk = tokenize(word)
	possibilities = return_possibilities(tk)
	possibilities = cartesian_product(possibilities)
	messagebox.showinfo('Generation Success', (str(len(possibilities)) + " similar segments found"))
	result.insert(1.0, str(possibilities))

def find():
	word = txt2.get(1.0, END).strip().lower()
	dist = txt2_1.get(1.0, END)

	word2 = preprocess(word)
	tk = tokenize(word2)
	possibilities = return_possibilities(tk)
	possibilities = cartesian_product(possibilities)
	dic = permutations_dictionary(word, possibilities, dist)
	if dic is not None:
		messagebox.showinfo('Generation Success', (str(len(dic)) + " similar segments found"))
		result2.insert(1.0, str(dic))
	else:
		messagebox.showinfo('Generation Success'," No similar segments of this distance found")

def match():
	original_word_1 = txt3.get(1.0, END).strip().lower()
	original_word_2 = txt3_1.get(1.0, END).strip().lower()
	word_1,word_2 = preprocess(original_word_1), preprocess(original_word_2)
	tk1, tk2 = (tokenize(word_1)),(tokenize(word_2))
	possibilities_1, possibilities_2 = return_possibilities(tk1),return_possibilities(tk2)
	permutations_1, permutations_2 = (cartesian_product(possibilities_1)), (cartesian_product(possibilities_2))
	string = find_matching(permutations_1,permutations_2, original_word_1, original_word_2, tk1, tk2)
	messagebox.showinfo('Generation Success'," Analysis Completed")
	result3.insert(1.0, string)
	



root = Tk()
root.geometry('1000x500')
root.title("Historical Phonetics Analyzer")
n = Notebook(root)
f1,f2,f3,f4,f5 = Frame(n),Frame(n),Frame(n),Frame(n), Frame(n)

n.add(f4, text='IPA Chart')
n.add(f1, text='Generate Phonetically Similar Segment (PSS)')
n.add(f2, text='Phonetic Minimum Edit Distance')
n.add(f3, text='Historical Similarities')
n.add(f5, text='Info')

lbl = Label(f1, text="Enter any word transcribed in the International Phonetic Alphabet to get nearest Neighbors\n")
lbl.pack()
txt = scrolledtext.ScrolledText(f1, width=30, height=5)
txt.insert(INSERT,'Insert Word Here')
txt.pack()
btn = Button(f1, text="Generate", bg="blue", fg="white", command=generate)
btn.pack()
result = scrolledtext.ScrolledText(f1, width=20, height=5)
result.insert(INSERT,'Results')
result.pack()

lbl2 = Label(f2, text="Sort Solutions based on Distance\n")
lbl2.pack()
txt2 = scrolledtext.ScrolledText(f2, width=20, height=5)
txt2.insert(INSERT,'Insert Word Here')
txt2.pack()
txt2_1 = scrolledtext.ScrolledText(f2, width=5, height=1)
txt2_1.insert(INSERT,'DIST')
txt2_1.pack()
btn2 = Button(f2, text="Generate", bg="blue", fg="white", command=find)
btn2.pack()
result2 = scrolledtext.ScrolledText(f2, width=20, height=5)
result2.insert(INSERT,'Results')
result2.pack()

lbl3 = Label(f3, text="Find out if two words are similar\n")
lbl3.pack()
txt3 = scrolledtext.ScrolledText(f3, width=20, height=5)
txt3.insert(INSERT,'Insert First Word')
txt3.pack()
txt3_1 = scrolledtext.ScrolledText(f3, width=20, height=5)
txt3_1.insert(INSERT,'Insert Second Word')
txt3_1.pack()
btn3 = Button(f3, text="Match", bg="blue", fg="white", command=match)
btn3.pack()
result3 = scrolledtext.ScrolledText(f3, width=45, height=10)
result3.pack()

lbl4 = Label(f4, text="The International Phonetic Alphabet Chart\nA guide to Phoneme Similarity\n")
lbl4.pack()

lbl5 = Label(f5, text="Anirudh Chandrashekhar and Kriti Sharma\n")
lbl5.pack()


img = ImageTk.PhotoImage(Image.open("/home/ani/Desktop/historical_analyzer/ipa.jpg"))
panel = Label(f4, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")

n.pack()
root.mainloop()

