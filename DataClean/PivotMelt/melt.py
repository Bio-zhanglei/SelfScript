def main(argv):
	#get command
	try:
		options, args = getopt.getopt(argv, "hi:c:v:o:", ["help","inputFile=","colId=","value=","outFile="])
	except getopt.GetoptError:
		print('Error: python melt.py -i <inputfile> -c <colID> -v <value> -o <outfile>')
		print('   or: python melt.py --inputFile=<inputFile> --colId=<colnams> -v <value> --outFile=<outfile>')
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
Author:zhanglei, 2022/04/07		
This script is for conversing pivot table to melt table.
You need to use the command like: 
	python valueCount.py -i <inputfile> -c <column> -o <outfile>
	Among these:
		-i is needed   (inputFile,such as one of sample_melt.xls)
		-c is needed   (columnID, the column be set as id columns, such as '-c Id,parity,group')
		-v is optional (value, default is the columns except those columns in -c)
                      	       (If you want to select the certain column value, please type like '-v day1,day2'. )
		-o is optional (outFileName, but it must be end with '.txt/.xls' or '.csv', default is result_inputFile, such as result_sample1.xls)
			''')			   
			sys.exit()
		
		if option in ("-i", "--inputFile"):
			para['if'] = value
			para['if_sep'] = suffix(value)
		if option in ("-c", "--colId"):
			para['col'] = [i.strip() for i in value.split(',')]
		if option in ("-o", "--outFile"):
			para['of'] = value
		if option in ("-v", "--value"):
			para['value'] = [i.strip() for i in value.split(',')]
			
	#check rawfile, targetfile, merge_colID and outfile
	if not (('if' in para) and ('col' in para)):
		print('Error:inputfile or colId is both needed')
		sys.exit(2)
	if ('of' not in para):
		para['of'] = "result_" + para['if']
	if ('value' not in para):
		para['value'] = None
		
	return para
	
def melt(file, sep, col, out, value):
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
				melt(id_vars=col, value_vars=value).#melt
				to_csv(out, sep=sep_out, index=False)#saved
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
	value = para['value']
	
	#value_counting
	melt(file, sep, col, out, value)
	
