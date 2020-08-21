list = [0,1,2,1]

w = 0
r = 0

while r < len(list):

	if(list[r] != 0):
		list[w] = list[r]
		w = w+1
	r = r+1

while w < len(list):
	list[w] = 0
	w = w+1

print(list)			