def main(argv):
	#get command
	try:
		options, args = getopt.getopt(argv, "hi:c:o:n:d:", ["help","inputFile=","colNames=","outFile=","normalize=","descending="])
	except getopt.GetoptError:
		print('Error: python valueCount.py -i <rawfile> -c <colnames> -o <outfile> -n <normalize> -d <descending>')
		print('   or: python valueCount.py --inputFile=<inputFile> --colNames=<colnams> --outFile=<outfile> --normalize=<normalize> --descending=<descending>')
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

	#add command -r, -t, -c to para_dict
	#calculate sep according -rf and -tf, also added to para_dict
	para={}
	for option, value in options:
		if option in ("-h", "--help"):
			print('''
Version:miniconda python 3.7
Author:zhanglei, 2022/04/06			
This script is for counting the value with the same attribute.
You need to use the command like: 
	python valueCount.py -i <inputfile> -c <column> -o <outfile> -n <normalize> -d <descending>
	Among these:
		-i is needed   (inputFile,such as one of sample1.xls or sample2.xls or sample3.xls)
		-c is needed   (columnName, the column you want to value counting, such as '-c Gene')
			       (if you want to count two or more columns, such as '-c Gene,Entry' Warning!!!no space between Gene and Entry)
		-o is optional (outFileName, but it must be end with '.txt/.xls' or '.csv', default is result_inputFile, such as result_sample1.xls)
		-n is optional (normalize, default is False, calculate the 100 percentage is True.)
		-d is optional (descending,default is True, ascending is False).
			''')			   
			sys.exit()
		
		if option in ("-i", "--inputFile"):
			para['if'] = value
			para['if_sep'] = suffix(value)
		if option in ("-c", "--colNames"):
			para['col'] = [i.strip() for i in value.split(',')]
		if option in ("-o", "--outFile"):
			para['of'] = value
		if option in ("-n", "--normalize"):
			para['norm'] = True if value == 'True' else False
		if option in ("-d", "--descending"):
			para['des'] = False if value == 'False' else True
			
	#check rawfile, targetfile, merge_colnames and outfile
	if not (('if' in para) and ('col' in para)):
		print('Error:inputfile or colnames is both needed')
		sys.exit(2)
	if ('of' not in para):
		para['of'] = "result_" + para['if']
	if ('norm' not in para):
		para['norm'] = False
	if ('des' not in para):
		para['des'] = True
		
	return para
	
def valueCounts(file, sep, col, out, norm, des):
	#acquire the sep of out file
	if out.endswith('.txt') or out.endswith('.xls'):
		sep_out = '\t'
	elif out.endswith('.csv'):
		sep_out = ','
	else:
		print('Error:the format of outfile is not compatible, change .xls or .txt or .csv')
		sys.exit()

	(
	 pd.read_csv(file, sep=sep, header=0).#read
				value_counts(subset=col, ascending=not des, normalize=norm).#value_counts
				to_csv(out, sep=sep_out, index=True)#saved
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
	norm = para['norm']
	des = para['des']
	
	#value_counting
	valueCounts(file, sep, col, out, norm, des)
	
