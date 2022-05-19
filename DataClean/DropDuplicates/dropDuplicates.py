#你需要安装pandas
#此脚本用于删除某一列的重复项。
#你可以如下执行查看一个示例的结果(更多帮助输入'python dropDuplicates.py -h')
#python dropDuplicates.py -i sample1.xls -c Gene -o result.txt
def main(argv):
	#get command
	try:
		options, args = getopt.getopt(argv, "hi:c:o:m:", ["help","inputFile=","colNames=","outFile=","mode="])
	except getopt.GetoptError:
		print('Error: python dropDuplicates.py -i <rawfile> -c <colnames> -o <outfile> -m <mode>')
		print('   or: python dropDuplicates.py --inputFile=<inputFile> --colNames=<colnams> --outFile=<outfile> --mode=<mode>')
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
This script is for dropping duplicates according to columns.
You need to use the command like: 
	python dropDuplicates.py -i <inputfile> -c <column> -o <outfile> -m <mode>
	Among these:
		-i is needed   (inputFile,such as one of sample1.xls or sample2.xls or sample3.xls)
		-c is needed   (columnName, the column you want to drop duplicates, such as '-c Gene')
                               (If you want to drop duplicates according to two or more columns, please type like '-c Gene,Entry', Warning!!! no space between Gene and Entry)
		-o is optional (outFileName, but it must be end with '.txt/.xls' or '.csv', default is result_inputFile, such as result_sample1.xls).
		-m is optional (mode,default is first).
			       (if you want to keep the first duplicates, plese type '-m first')
			       (if you want to keep the last duplicates, please type '-m last')
			       (if you want to keep those are not duplicated, please type '-m none')
			''')			   
			sys.exit()
		
		if option in ("-i", "--inputFile"):
			para['if'] = value
			para['if_sep'] = suffix(value)
		if option in ("-c", "--colNames"):
			para['col'] = [i.strip() for i in value.split(',')]
		if option in ("-o", "--outFile"):
			para['of'] = value
		if option in ("-m", "--mode"):
			para['md'] = value if value != 'none' else False
			
	#check rawfile, targetfile, merge_colnames and outfile
	if not (('if' in para) and ('col' in para)):
		print('Error:inputfile or colnames is both needed')
		sys.exit(2)
	if ('of' not in para):
		para['of'] = "result_" + para['if']
	if ('md' not in para):
		para['md'] = "first"
		
	return para
	
def dropDuplicates(file, sep, col, out, mode):
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
					drop_duplicates(subset=col, keep=mode).#dropping according to the columns
					to_csv(out, sep=sep_out, index = False)#saved
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
	mode = para['md']
	
	#drop_duplicates
	dropDuplicates(file, sep, col, out, mode)
	
