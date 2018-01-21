prefixes = "JKLMNOPQ"
suffix = "ack"
def print_letters():
    for letter in prefixes:
	    print(letter + suffix)

def print_letters_again():
	for letter in prefixes:
		if letter == 'O' or letter == 'Q':
		     print(letter + "u" + suffix)
		else:
			 print(letter + suffix)

def print_letters_while():
	length = len[prefixes]
	index = 0
	while index < length:
		letter = prefixes[index]
		if letter == 'O' or letter == 'Q':
			print(letter + "u" + suffix)
		else:
			print(letter + suffix)	

def print_p():
	word = 'banana'
	n = 0
	for letter in word:
		if letter == 'a':
			n = n + 1
			print(n)


def find(word, letter, index):
	if index >= len(word):
		print("index is too big and out of length")
	while index < len(word):
		if word[index] == letter:
			return index
		index = index + 1
	return -1 

def find_in_word(word,letter): 
	index = word.find(letter)
	if index == -1:
		print("not found")
		return
	
def is_reverse(word1,word2):
     if len(word1)!=len(word2):
     	return False
     	i = 0
     	j = len(word2)-1
     	while j > 0:
     		print(i,j)
     		if word1[i]!=word2[j]:
     			return False
     			i = i+1
     			j = j-1
     			return True

def is_palindrome(word):
	if len(word) > 2:
		
        
		word[index]=word[-index]
		return True
	else:
		return False

def histogram(s):
	d=dict()
	for c in s:
		if c not in d:
			d[c]=1
		else:
			d[c]+=1
	return d



def sum_list(l):
	sum = 0
	for sublist in l:
		for element in sublist:
			sum = sum + element
	return sum

d = {'xiaoming': 78, 'xiaohong': 34, 'xiaonglv': 90, 'xiaofang': 66, 'huahua': 45}

def average_scores(d):
	sum = 0
	for student in d:
		sum = sum + d[student]

	amount = len(d)
	average = sum / amount
	return average

def highest_score(d):
	max = 0
	for student in d:
		if d[student] > max:
			max = d[student]
	return max

def lowest_score(d):
	min = d.values()[0]
	for student in d:
		if d[student] < min:
			min = d[student]
	return min

[78, 34, 90, 66, 45]
def lowest_score_bylist(d):
	scores = d.values()
	min = scores[0]
	
	for score in scores:
		if score< min:
			min = score
	return min

max=1000
def middle_score(d):
	min = lowest_score(d)
	return (max + min)/2

def print_f(s):
	print(s)
{'a':1,'v':2,'s':3}
def invert_dict(d):
	inverse = dict()
	for key in d:
		val=d[key]
		inverse[val]=key
	return inverse




