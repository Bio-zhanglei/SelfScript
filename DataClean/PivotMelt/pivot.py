#你需要安装pandas
#此脚本用于将长表(melt)转换为宽表(pivot),数据透视。
#你可以输入执行如下查看一个实例的结果(更多说明输入'python pivot.py -h')
#python pivot.py -i sample_pivot.csv -c Age,Sex -r Dose -v Weight,Height -o result_sample_pivot.csv
def main(argv):
	#get command
	try:
		options, args = getopt.getopt(argv, "hi:c:r:v:o:", ["help","inputFile=","colNames=","rowNames=","value=","outFile="])
	except getopt.GetoptError:
		print('Error: python pivot.py -i <inputfile> -c <colNames> -r <rowNames> -v <value> -o <outfile>')
		print('   or: python pivot.py --inputFile=<inputFile> --colNames=<colnames> --rowNames=<rowNames> -v <value> --outFile=<outfile> ')
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
This script is for conversing melt table to pivot table.
You need to use the command like: 
	python valueCount.py -i <inputfile> -c <column> -o <outfile>
	Among these:
		-i is needed   (inputFile,such as one of sample_pivot.csv)
		-c is needed   (colnames, such as '-c Age,Sex' or '-c Age')
		-r is needed   (rownames, such as '-r Dose' or '-r Sex,Dose')
		-v is needed   (value, the value columns you want to pivot, such as '-v Weight' or '-v Weight,Height')
		-o is optional (outFileName, but it must be end with '.txt/.xls' or '.csv', default is result_inputFile, such as result_sample_pivot.csv)
        Warning!!!
        Warning!!!
        Warning!!!
            if the combination of '-c' and '-r' is duplicated, the value of -v will be joined with comma together
            That is to say, if '-c' and '-r' is three factors, such as '-c Sex,Age -r Dose'
                            but you only consider two factors, such as '-c Sex -r Dose', the duplicated value will be join like 'value1,value2'
			''')			   
			sys.exit()
		
		if option in ("-i", "--inputFile"):
			para['if'] = value
			para['if_sep'] = suffix(value)
		if option in ("-c", "--colNames"):
			para['col'] = [i.strip() for i in value.split(',')]
		if option in ("-r", "--rowNames"):
			para['idx'] = [i.strip() for i in value.split(',')]
		if option in ("-v", "--value"):
			para['value'] = [i.strip() for i in value.split(',')]
		if option in ("-o", "--outFile"):
			para['of'] = value
			
	#check rawfile, targetfile, merge_colID and outfile
	if not (('if' in para) and ('col' in para) and ('idx' in para) and ('value' in para)):
		print('Error:inputfile or colNames or rowNames or value is all needed')
		sys.exit(2)
	if ('of' not in para):
		para['of'] = "result_" + para['if']
		
	return para

def join(pivot_value):
	value = [str(i) for i in pivot_value]
	return ','.join(value)

def pivot(file, sep, col, idx, value, out):
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
				pivot_table(columns=col, index=idx, values=value,aggfunc=join).#pivot_table
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
	idx = para['idx']
	value = para['value']
	out = para['of']
	
	#pivot_table
	pivot(file, sep, col, idx, value, out)
	
