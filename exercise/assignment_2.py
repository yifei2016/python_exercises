def read_file():
	
	fname = '/Users/wangyifei/Downloads/Books.txt'
	with open(fname) as fin:
		lines = fin.readlines()

	delimeter = '#'
	fout = open('/Users/wangyifei/Downloads/NewBook.txt','w')
	
	for line in lines:
		fields = line.split(delimeter)
		if fields[1].isdigit() and fields[6].isdigit() and fields[7].isdigit() and len(fields[2])>0 and len(fields[3])>0 and len(fields[4]) > 0 :
			
			fout.write(line)
	

	fout.close()