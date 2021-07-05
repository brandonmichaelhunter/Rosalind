parent, child = 1,1

for itr in range(35-1):
	  child, parent = parent, parent+(child*4)
print(child)
	  
