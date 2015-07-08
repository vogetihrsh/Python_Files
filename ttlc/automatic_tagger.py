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
		for tag in tags:
			words = tag.split(' ')
			words = words[:-1]
			self.taglist.append([self.lemobj.lemmatize(word) for word in words])
				
	def getKeywordList(self,question,description):
		RAKEOBJ = RakeKeywordExtractor()
		return_list = RAKEOBJ.extract(description,question)
		keywords = [r for r in return_list]
		return keywords
	def getTags(self,keywords):
		predtags=set([])
		keywordlist = []
		for keyword in keywords:
			keywordlist.append(keyword.split(' '))
		print keywordlist
################### check if a tag is completely in a keyword#################################
		for wordlist in self.taglist:
			flag=0
			for keywords in keywordlist:
				if(set(wordlist)<=set(keywords)):
					flag=1
					break
			if(flag==1):
				print "this is in if"
				print wordlist
				tempstr=""
				for s in wordlist:
					tempstr=tempstr+s+ " "
				print tempstr	
				predtags.add(tempstr)
		print predtags		
############################################## step completed###############################		
					
				
		# check if a tag is completely in a keyword
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
	obj.getTags(keywords)
	
		
