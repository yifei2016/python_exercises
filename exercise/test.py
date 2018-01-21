def print_lyrics():
	
	part1 = "rwergwrewrtgwrgwergegafeadfwasd"
	part2 = 'line'
	cat = part1 + part2 
	
	
	print(cat)
	print("I sleep all night and I work all day.")

def rep():
	print_lyrics()
	print_lyrics()
	print_lyrics()
	print_lyrics()
	

def cat_twice(part1, part2):

    cat = part1 + part2
    print_twice(cat)

def print_twice(bruce):
	print(bruce)
	print(bruce)


line1= 'Bing tiddle'
line2= 'tiddle bang'

def get_number(num):
	result = number*10
	print('result is ' + result+' yifei')
	return result
    
 

def print_name(n):
    print(n)



def do_twice(f,val):
    f(val)
    f(val)

def print_spam():
	print('spam')

def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)

def print_n(s,n):
	if n <= 0:
		return
	print(s)
	print_n(s,n-1)


def get_tax():
	print("input your travel expense")
	expense = input()
	if expense <= 90:
		tax = calculate_tax(expense)
		print("Tax you should pay is")
		print(tax)
	else:
		print("your expense is too much,please input again")
		get_tax()

def calculate_tax(expense):
	 if not isinstance(expense,int) and not isinstance(expense,float):
	 	print("only numbers are allowed.")
	 	return
	 else:
	 	tax = expense*0.3
	 	return tax

def print_n(s,n):
	 while n > 0:
	 	print(s)
	 	n = n - 1
	 return

def print_letters():
	prefixes = 'JKLMNOPQ'
	suffix = 'ack'
	for letter in prefixes:
		print(letter + suffix)

def print_letters_again():
	prefixes = 'JKLMNOPQ'
	suffix = 'ack'
	for a in prefixes:
		if a == 'O' or a == 'Q':
			print(a + 'u' + suffix)
		else:
			print(a + suffix)

def print_letters_while():
	prefixes = 'JKLMNOPQ'
	suffix = 'ack'
	length = len(prefixes)
	index = 0

	while index < length:
		letter = prefixes[index]
		if letter == 'O' or letter == 'Q':
			print(letter + 'u' + suffix)
		else:
			print(letter + suffix)
		index = index + 1


	 	
	

