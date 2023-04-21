#20BAI10240-Q-2-TUTORIAL-1
a = [1,2,3]
b = [3,1,4]
c=[]
for i in a:
    for j in b:
        if i!=j:
            c.append((i,j))
print(c)