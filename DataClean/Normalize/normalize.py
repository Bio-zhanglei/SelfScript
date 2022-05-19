def main(argv):
	#get command
	try:
		options, args = getopt.getopt(argv, "hi:c:o:r:", ["help","inputFile=","colNames=","outFile=","rowNames="])
	except getopt.GetoptError:
		print('Error: python normalize.py -i <rawfile> -c <colnames> -o <outfile> -r <rownames>')
		print('   or: python normalize.py --inputFile=<inputFile> --colNames=<colnams> --outFile=<outfile> --rowNames=<rownames>')
		sys.exit(2)
	
	#get sep by filename_suffix
	def suffix(value):
		if value.endswith('.txt') or value.endswith('.xls'):
			return '\t'
		elif value.endswith('.csv'):
			return ','
		else:
			print('Error:the suffix of %s is not .xls, .txt or .csv' %value)
			sys.exit(2)

	#add command -i, -c, -o to para_dict
	para={}
	for option, value in options:
		if option in ("-h", "--help"):
			print('''
Version:miniconda python 3.7
Author:zhanglei, 2022/04/06			
This script is for normalizing to 100 percentage.
You need to use the command like: 
	python normalize.py -i <inputfile> -c <column> -o <outfile> -r <rownames>
	Among these:
		-i is needed   (inputFile,such as sample.xls )
		-c is needed   (columnName, the one column you want normalize, such as '-c A1')
  			       (if you want to count two or more columns, such as '-c A1,A2',Warning!!! no space between A1 and A2)
		-o is optional (outFileName, but it must be end with '.txt/.xls' or '.csv', default is result_inputFile, such as result_sample.xls)
		-r is optional (rowNames, default is False, no any rownames)
			       (If you want to set one or more columns as rownames, please type like '-c Gene' or '-c Gene,Entry', Warning!! no space between Gene and Entry)
			''')			   
			sys.exit()
		
		if option in ("-i", "--inputFile"):
			para['if'] = value
			para['if_sep'] = suffix(value)
		if option in ("-c", "--colNames"):
			para['col'] = [i.strip() for i in value.split(',')]
		if option in ("-o", "--outFile"):
			para['of'] = value
		if option in ("-r", "--rowNames"):
			para['idx'] = [i.strip() for i in value.split(',')]
			
	#check rawfile, targetfile, merge_colnames and outfile
	if not (('if' in para) and ('col' in para)):
		print('Error:inputfile or colnames is both needed')
		sys.exit(2)
	if ('of' not in para):
		para['of'] = "result_" + para['if']
	if ('idx' not in para):
		para['idx'] = False
		
	return para

def percentage(series):
	total = series.sum()
	return series/total

def normalize(file, sep, col, out, idx):
	#acquire the sep of out file
	if out.endswith('.txt') or out.endswith('.xls'):
		sep_out = '\t'
	elif out.endswith('.csv'):
		sep_out = ','
	else:
		print('Error:the format of outfile is not compatible, change .xls or .txt or .csv')
		sys.exit()

	(
	pd.read_csv(file, sep=sep, header=0, index_col=idx).#read
					loc[:,col].#dropping according to the columns
					apply(percentage).
					to_csv(out, sep=sep_out, index = True)#saved
					)
					
if __name__ == "__main__":
	import pandas as pd
	import sys
	import getopt
	
	#get command parameter
	para = main(sys.argv[1:])
	file = para['if']
	sep = para['if_sep']
	col = para['col']
	out = para['of']
	idx = para['idx']
	
	#value_counting
	normalize(file, sep, col, out, idx)
