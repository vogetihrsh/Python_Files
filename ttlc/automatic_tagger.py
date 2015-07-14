#AUTOMATIC TAGGER REQUEIRES MAPS A TTLC QUERY TO ONE OR MANY GIVEN 

from modified_Rake import RakeKeywordExtractor
import nltk
import distance
from nltk.stem import WordNetLemmatizer
import sys
class AssignTags:
	def __init__(self,tags):
		self.tags = tags
		self.lemobj = WordNetLemmatizer()
		self.worddict = {}
		self.taglist = []
		self.taglem = []
		for tag in tags:
			words = tag.split(' ')
			words = words[:-1]
			wordlist=[self.lemobj.lemmatize(word) for word in words]
			self.taglist.append(wordlist)
			tempstr=""
			for word in wordlist:
				tempstr=tempstr+word+" "
			self.taglem.append(tempstr[:-1])	
				
	def getKeywordList(self,question,description):
		RAKEOBJ = RakeKeywordExtractor()
		return_list = RAKEOBJ.extract(description,question,True)
		keywords = [r for r in return_list]
		return keywords

	def getTags(self,keywords):
		predtags=set([])
		keywordlist = []
		for keyword in keywords:
			keywordlist.append(keyword.split(' '))
################### check if a tag is completely in a keyword#################################
		for wordlist in self.taglist:
			flag=0
			for keyword in keywordlist:
				if(set(wordlist)<=set(keyword)):
					flag=1
					break
			if(flag==1):
				tempstr=""
				for s in wordlist:
					tempstr=tempstr+s+ " "
				predtags.add(tempstr[:-1])
		#print predtags
############################################## step completed###############################		
		predtags_for_each=set([])
		for keyword in keywords:
			for tag in self.taglem:
				score = distance.nlevenshtein(tag,keyword)
				if(0.2 > score):
			  		predtags.add(tag)
		return predtags	
				
		# for each keyword see the tag with minimum value, 
					

if __name__=="__main__":
	f1 = open(sys.argv[1],"r")
	f2 = open(sys.argv[2],"r")
	l1 = f1.readlines()
	question = f2.readline()
	description = f2.read()
	tags=[]
	for line in l1:
		tags.append(line[:-1])
	obj = AssignTags(tags)
	keywords=obj.getKeywordList(question,description)
	print keywords
#	tags=obj.getTags(keywords)
#	for tag in tags:
#		print tag
		
