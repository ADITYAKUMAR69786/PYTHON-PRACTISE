#20BAI10240-Q-2-TUTORIAL-1
squares = [1,4,9,16,25,36,49,64,81,100]
cubes = [1,8,27,64,125,216,343,512,729,1000]
c=[]
for i in squares:
	if (round(i**(1/2)))%2==0:
		c.append(i)
for j in cubes:
	if (round(j**(1/3)))%2==0:
		c.append((j))
print(c)