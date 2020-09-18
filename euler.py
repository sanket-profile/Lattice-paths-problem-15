def neighbours(a , n):
	if a[0] < n and a[1] > -n:
		neighbour = [(a[0]+ 1 , a[1]) , (a[0] , a[1]- 1)]
	elif a[0] < n and a[1] == -n:
		neighbour = [(a[0] + 1 , a[1])]
	elif a[0] == n and a[1] > -n:
		neighbour = [(a[0] , a[1] - 1)]
	elif a[0] == n and a[1] == -n :
		neighbour = []
	else:
		pass
	return(neighbour)

def path(a , n):
	stack = [a]
	count = 0
	popped = []
	while stack != []:
		neighbour = neighbours(stack[-1] , n)
		b = stack.pop()
		popped.append(b)
		if len(neighbour)==1:
			if neighbour[0] in popped:
				count = count + 1
			elif neighbour[0] == (n , -n):
				count = count + 1
			else:
				stack.append(neighbour[0])
		else:
			if (neighbour[0] in popped) and (neighbour[1] not in popped):
				c = path(neighbour[0] , n)
				count = count + c		
				stack.append(neighbour[1])
			elif (neighbour[0] not in popped) and (neighbour[1] in popped):
				c = path(neighbour[1] , n)
				count = count + c
				stack.append(neighbour[0])
			elif (neighbour[0] in popped) and (neighbour[1] in popped):
				c = path(neighbour[0] , n) + path(neighbour[1] , n) 
				count = count + c
			else:
				stack.append(neighbour[0])
				stack.append(neighbour[1])
	return(count)

def newneighbours(a):
	if a[0] > 0 and a[1] > 0 :
		neighbour = [(a[0] - 1 , a[1]) , (a[0] , a[1] - 1)]
	elif a[0] == 0 and a[1] > 0:
		neighbour = [(a[0] , a[1] - 1)]
	elif a[0] > 0 and a[1] == 0:
		neighbour = [(a[0] - 1 , a[1])]
	elif a[0] == 0 and a[1] == 0:
		neighbour = []
	else:
		pass
	return(neighbour)

def newpath(a ,n):
	d = {}
	for i in range(0 , n+1):
		for j in range(0, n+1):
			if i==0 and j ==0 :
				d[str((0,0))] = 1
			else:
				neighbour = newneighbours((i , j))
				if len(neighbour) >1:
					d[str((i , j))] = d[str(neighbour[0])] + d[str(neighbour[1])] 
				else:
					d[str((i , j))]  = d[str(neighbour[0])]
	return(d[str((n , n))]) 


