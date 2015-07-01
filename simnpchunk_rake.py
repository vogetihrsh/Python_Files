#### GRAMMER FROM SU NAM KIM AND MIN-YEN KAN ###########
########## USING RAKE TO SCORE THE KEYWRODS ###########

import nltk
import sys
import operator
from stopwordList import getList
from nltk.stem import WordNetLemmatizer
from rake import RakeKeywordExtractor

def extractNP(CONTENT):
	stopwords = getList()
	grammer = r"""
		NBAR:
			{<NN.*|JJ>*<NN.*>}  
		NP:
			{<NBAR>}
			{<NBAR><IN><NBAR>} 

		"""
	chunker = nltk.RegexpParser(grammer)	# create a chunker with the parser
	words = [w.lower() for w in nltk.word_tokenize(CONTENT)]
	taggedwords = nltk.pos_tag(words)
	tree = chunker.parse(taggedwords)
	words  = []
	temp = [] 
	lemmaobj = WordNetLemmatizer()
	for subtree in tree.subtrees():
		if subtree.label() == "NP":
			for leaves in subtree.leaves():
				w = leaves[0].lower()
				if w not in stopwords:
					w = lemmaobj.lemmatize(w)
					temp.append(w)
			if temp!=[]:		
				words.append(temp)
			temp = [] 
	return words 			

def extractKeywords(phrase_list):
	RAKE_OBJ = RakeKeywordExtractor(set([]))
	word_scores = RAKE_OBJ._calculate_word_scores(phrase_list)
	phrase_scores = RAKE_OBJ._calculate_phrase_scores(phrase_list, word_scores)
	sorted_phrase_scores = sorted(phrase_scores.iteritems(),key=operator.itemgetter(1), reverse=True)
	n_phrases = len(sorted_phrase_scores)
	return sorted_phrase_scores[0:int(n_phrases)]

if __name__=="__main__":
	f = open(sys.argv[1],"r")
	CONTENT = f.read()
	words = extractNP(CONTENT)
	keywords = extractKeywords(words)
	print keywords
	

