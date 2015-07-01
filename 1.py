# PYTHON CODE FOR READING SET OF TWEETS FROM A CSV FILE AND THE THIRD COLUM SHOULD BE THE TWEETS 
# REFER TO THE VODAFONEIN.CSV FOR FURTHER INFORMATION ABOUT THE FORMAT 
# TOKENIZE -> REMOVE STOP WORDS -> STEMMING -> USING FREQUENCY DISTRUBUTION -> PICK THE TOP WORDS

# AUTHOR : SRIHARSHA V
# PURPOSE: FOR IDENTIFYING IMPORTANT WORDS IN A SET OF TWEETS





# IMPORTING REQUIRED MODULES
import nltk as nltk					# MAIN NLTK PACKAGE
from nltk.corpus import stopwords			# PACKAGE FOR STOPWORDS
from nltk.stem.lancaster import LancasterStemmer	# FOR STEMMING
from nltk.collocations import *


f=open("input.csv");				# FILE CONTAINING TWEETS
r = f.readlines();				# READLINES FROM THE FILE 
NUM_TWEETS = len(r);				#NUMBER OF TWEEETS IN THE INPUT 

bigram_measures = nltk.collocations.BigramAssocMeasures()	#BIGRAM OBJECT 
trigram_measures = nltk.collocations.TrigramAssocMeasures()	#TRIGRAM OBJECT 	


# TOKENIZATION AND ADDING TO THE DICTIONARY
# ENTRY FOR A WORD ONLY ONCE PER TWEET 

# LIST OF STOP WORDS
extra_stopwords = set(('we','us','please','-','.',''));		# EXTRA STOP WORDS TO BE REMOVED
stop = set(stopwords.words('english'));
stop=stop.union(extra_stopwords);			# ADDING EXTRA STOP WORDS 
st = LancasterStemmer();			#STEMMER OBJECTS
tweets = []	#ARRAY FOR TWEETS 
words = [] 	# ARRAY AFTER TOKENIZATION AND STOP WORD REMOVAL
for i in range(0,NUM_TWEETS):
	  r[i] = r[i].translate(None,"?.!\r");
	  tweets.append(((r[i].split(','))[2][:-1]).lower())		# STORE ALL TWEETS IN LOWER CASE. REMOVE USERNAME. 
	  s=[z for z in (tweets[i].split(' '))[1:] if z not in stop]	# REMOVING STOP WORDS 
	  # s = [st.stem(i) for i in s]					# FINAL ARRAY FOR THE TWEETS AFTER STEMMING AND STOP WORD REMOVAL 
	  words = words + s;
#print words

# FREQUENCY DISTRIBUTION OF SINGLE WORDS
freq_words = nltk.FreqDist(words);
for i in freq_words.most_common(20):
	print i

#FREQUENCY DISTRIBUTION OF BIGRAM WORDS 	
bigram_finder = BigramCollocationFinder.from_words(words);		#CREATE FINDER OBJECT 
scores = bigram_finder.score_ngrams( bigram_measures.raw_freq );	# WHAT MEASURE TO USE IS MENTIONED BY BIGRAM_MEASURE.RAW_FREQ
for i in range(0,5):
	print scores[i]















