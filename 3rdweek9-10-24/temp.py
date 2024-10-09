l=["apple","mango","lichi"]
a=len(l)
temp=l[0]
l[0]=l[a-1]
l[a-1]=temp

print(l)
