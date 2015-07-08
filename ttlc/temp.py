f = open("tags","r")
g = open("newtags","w") 
r = f.readlines()
for line in r:
	line = line.split(' ')
	for word in line:
		g.write(word)
	g.write("\n")
f.close()
g.close()	
 	
