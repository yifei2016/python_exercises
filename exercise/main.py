def count(s,l):
	c=0
	for letter in s:
		if letter == l:
			c=c+1
	print(c)

def capitalize_all(t):
	res = []
	for s in t:
		res.append(s.capitalize())
	return res

def only_upper(t):
	res = []
	for s in t:
	    if s.isupper():
	        res.append(s)
	return res

def histogram(s):
	d = dict()
	for c in s:
		d[c] = d.get(c,0) + 1
	return d