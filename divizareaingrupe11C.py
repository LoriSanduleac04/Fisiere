with open("listaclasei.txt","r") as f:
	linii = f.read()
franceza=[]
nf=[] 
engleza=[]
ne=[] 
for i in linii.split("\n"):
	c=i.split()
	if str(c[3])=='Engleza':ne.append(int(c[2])),engleza.append(c)
	if str(c[3])=='Franceza':nf.append(int(c[2])),franceza.append(c)
with open ("limbaengleza.txt","w") as f: 
	for i in range(0,len(engleza)):
		for l in range(0,len(engleza[0])):f.write(str(engleza[i][l])+str(' '))
		f.write("\n")
	f.writelines("Media: "+ str(sum(ne)/len(ne)))
with open ("limbafranceza.txt","w") as f:
	for i in range(0,len(franceza)): 
		for j in range(0,len(franceza[0])):f.write(str(franceza[i][j])+str(' '))
		f.write("\n")
	f.writelines("Media: "+ str(sum(nf)/len(nf))) 
