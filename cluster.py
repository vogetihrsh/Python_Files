import numpy as np #from numpy package
import sklearn.cluster  # from sklearn package
import distance #from distance package
import sys
import nltk 
f = open(sys.argv[1],"r")
read_line  = f.readlines()
words = []	
z=[]
for line in read_line:
	line=line.translate(None,'\n')
	r = line.split(',')
	o = r[0] + r[1]
	z=[]
	z.append(r[0])
	z.append(r[1])
	print nltk.pos_tag(z)
	words.append(o)

lev_similarity = -1*np.array([[distance.nlevenshtein(w1,w2,method=2) for w1 in words] for w2 in words])
affprop = sklearn.cluster.AffinityPropagation(affinity="precomputed", damping=0.5)
affprop.fit(lev_similarity)
for cluster_id in np.unique(affprop.labels_):
		 exemplar = words[affprop.cluster_centers_indices_[cluster_id]]
		 y = np.nonzero(affprop.labels_==cluster_id)
		 output = ""
		 for j in y:
		 	for k in j:
		 		output = output+','+words[k]
		 print exemplar,":",output
# cluster = np.unique(words[np.nonzero(affprop.labels_==cluster_id)])
#		 cluster_str = ", ".join(cluster)
#		 print(" - *%s:* %s" % (exemplar, cluster_str))

