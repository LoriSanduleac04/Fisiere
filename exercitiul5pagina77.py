with open('text.txt','r') as f:
    x=f.read()
with open('vocale.txt','w') as f:
    for i in range(0,len(x)):
        if x[i] in ('e', 'u','i','o','a','E','U','I','O','A'):
            f.write(x[i])
