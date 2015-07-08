# THIS PYTHON SCRIPTS USES RAKE METRICS
# DIFFERS FROM RAKE IN CALCULATING THE CANDIDATE KEYWORDS AKA phrase_list
# USES NP_CHUNK TO FIND CANDIDATE KEYWORDS

import nltk
import operator
import sys
from textblob import TextBlob
from rake import RakeKeywordExtractor
from textblob.np_extractors import ConllExtractor
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import WordPunctTokenizer
from textblob.taggers import NLTKTagger
from stopwordList import getList
import codecs
## GLOBAL VARIABLES 
top_fraction = 1
LEMMA_OBJ = WordNetLemmatizer()
tokenizer = WordPunctTokenizer()
nltk_tagger = NLTKTagger()
stopwords = getList()
COLL_OBJ = ConllExtractor()	

def rake_extract(phrase_list):
	RAKE_OBJ = RakeKeywordExtractor(set([]))
	word_scores = RAKE_OBJ._calculate_word_scores(phrase_list)
	phrase_scores = RAKE_OBJ._calculate_phrase_scores(phrase_list, word_scores)
	sorted_phrase_scores = sorted(phrase_scores.iteritems(),key=operator.itemgetter(1), reverse=True)
	n_phrases = len(sorted_phrase_scores)
	return sorted_phrase_scores[0:int(n_phrases)]

	

#FILE = open(sys.argv[1],"r")	
FILE = codecs.open(sys.argv[1],"r","iso8859-15")	
CONTENT = FILE.read()
CONTENT = CONTENT.encode('ascii','ignore')
BLOB_OBJ = TextBlob(CONTENT,tokenizer=tokenizer,pos_tagger = nltk_tagger,np_extractor = COLL_OBJ)	# OBJECT WITH FAST NP CHUNKER 
pos_tags = nltk.pos_tag(BLOB_OBJ.tokens)
BLOB_OBJ.pos_tags = pos_tags
phrase_list = BLOB_OBJ.noun_phrases
newlist =[]
temp =[]
for word in phrase_list:
	words = word.split(' ')
	for x in words:
		x = LEMMA_OBJ.lemmatize(x)
		x = x.lower()
		if x not in stopwords:
			temp.append(x)
	newlist.append(temp)
	temp = []
phrase_list = newlist	
#print COLLBLOB_OBJ.noun_phrases
keywordList = rake_extract(phrase_list)
for keyword in keywordList:
	print str(keyword[0])
	
