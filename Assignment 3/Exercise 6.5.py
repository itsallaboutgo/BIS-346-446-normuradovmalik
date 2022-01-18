# Ex 6.5

text = input("Enter text")
d = dict()
for x in text.lower().split():
    if not d.get(x):
        d[x]= 1
    else:
        d[x]+=1
print("WORD\tCount")
for k in d.keys():
    if d[k]>1:
        print(k,"\t\t",d[k])
        