#你需要安装pandas
#此脚本用于对数据分组和执行数学计算，如总和、平均值、最小/最大值、中值、标准差等。
#输入'python groupby_mathCalculate.py -h'查看使用说明
def main(argv):
	#get command
	try:
		options, args = getopt.getopt(argv, "hi:g:m:o:", ["help","inputFile=","groupByColumns=","math=","outFile="])
	except getopt.GetoptError:
		print('Error: python groupby_mathCalculate.py -i <rawfile> -g <groupby> -m <math> -o <outfile>')
		print('   or: python groupby_mathCalculate.py --inputFile=<inputFile> --groupBy=<groupByColumns> --math=<math> --outFile=<outfile>')
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
This script is for grouping data and performing math calculation, such as sum, mean, min/max, median, std, et al.
You need to use the command like: 
	python groupby_mathCalculate.py -i <inputfile> -g <groupByColumns> -m <math> -o <outFile>
	Among these:
		-i is needed   (inputFile,such as sample.csv)
 			       (It is better to input pure digital text, except for the columns you need to groupby)
		-g is needed   (groupByColumns, the column for grouping data, such as '-g taxonomy')
			       (if you want to group data according to two or more columns, such as '-c Entry,taxonomy' Warning!!!no space between Entry and taxonomy)
		-m is needed   (mathematical method, such as 'sum, mean, min, max, median, std')
                 	       (if you want to all, please type like '-c all')
                       	       (when you type -c all, the 'sum' result is not included, but we have count and mean, you can calculate by yourselve)
		-o is optional (outFileName, but it must be end with '.txt/.xls' or '.csv', default is result_inputFile, such as result_sample.csv)
			''')			   
			sys.exit()
		
		if option in ("-i", "--inputFile"):
			para['if'] = value
			para['if_sep'] = suffix(value)
		if option in ("-g", "--groupByColumns"):
			para['group'] = [i.strip() for i in value.split(',')]
		if option in ("-o", "--outFile"):
			para['of'] = value
		if (option in ("-m", "--math")) and (value in ['sum','mean','min','max','std','median','std', 'all']):
			para['math'] = value if value != 'all' else 'describe'
			
	#check rawfile, targetfile, merge_colnames and outfile
	if not (('if' in para) and ('group' in para)):
		print('Error:inputfile or groupByColumns is both needed')
		sys.exit(2)
	if ('math' not in para):
		print('Error:mathematical method is needed, and must be in one of sum, mean, min, max, std, median, std')
		sys.exit(2)
	if ('of' not in para):
		para['of'] = "result_" + para['if']
		
	return para
	
def groupby(file, sep, group, math, out):
	#acquire the sep of out file
	if out.endswith('.txt') or out.endswith('.xls'):
		sep_out = '\t'
	elif out.endswith('.csv'):
		sep_out = ','
	else:
		print('Error:the format of outfile is not compatible, change .xls or .txt or .csv')
		sys.exit(2)
	
	#eval to execute the pandas pipe, must be type as follow
	eval("(pd.read_csv(file, sep=sep, header=0).groupby(group).%s().to_csv(out, sep=sep_out, index=True))"%math)
			#read data		  #groupby	#math   #saved  			      #math_format
			
if __name__ == "__main__":
	import pandas as pd
	import sys
	import getopt
	
	#get command parameter
	para = main(sys.argv[1:])
	file = para['if']
	sep = para['if_sep']
	group = para['group']
	math = para['math']
	out = para['of']
	
	#value_counting
	groupby(file, sep, group, math, out)
	
