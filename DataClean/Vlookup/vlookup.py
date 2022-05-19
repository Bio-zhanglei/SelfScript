def main(argv):
	#get command
	try:
		options, args = getopt.getopt(argv, "hr:t:c:o:", ["help","rawFile=","targetFile=","colNames=","outFile="])
	except getopt.GetoptError:
		print('Error: python vlookup.py -r <rawfile> -t <targetfile> -c <colnames> -o <outfile>')
		print('   or: python vlookup.py --rawFile=<rawfile> --targetFile=<targetfile> --colNames=<colnams> --outFile=<outfile>')
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
Author:zhanglei, 2022/03/30
This script is for finding needed column from the total table, which is similar as 'VLookUp' in Excel.
        You need to use the command like: 
            python vlookup.py -r <rawfile> -t <targetfile> -c <column> -o <outfile>
        Among these:
            -r is needed   (rawFile,such as rawFile.xls)
            -t is needed   (targetFile, such as targetFile.csv)
            -c is needed   (columnName,it must be both in rawFile and targetFile,such as '-c Entry')
                           (Meanwhile, the column content is duplicate allowed, but the best is not)
            -o is optional (outFileName, default is result_targetFileName,such as 'result_find_KO.csv').          
            ''')
            
			sys.exit()
		if option in ("-r", "--rawFile"):
			para['rf'] = value
			para['rf_sep'] = suffix(value)
		if option in ("-t", "--targetFile"):
			para['tf'] = value
			para['tf_sep'] = suffix(value)
		if option in ("-c", "--colNames"):
			para['col'] = value
		if option in ("-o", "--outFile"):
			para['of'] = value
	
	#check rawfile, targetfile, merge_colnames and outfile
	if not (('rf' in para) and ('tf' in para) and ('col' in para)):
		print('Error:rawfile or targetfile or colnames is all needed')
		sys.exit(2)
	if ('of' not in para):
		para['of'] = "result_" + para['tf']

	return para
	
def read_data(file,sep):
	raw_data = pd.read_csv(file[0], header=0, sep=sep[0])
	target_data = pd.read_csv(file[1], header=0, sep=sep[1])
	return raw_data,target_data

def value_counts(target_data, col):
	counts = target_data[col].value_counts()
	counts = counts.reset_index()
	counts.columns = [col, 'counts']
	return counts

def data_merge(data,counts):
	raw_data = data[0]
	target_data = data[1]
	result = (
			target_data
				.merge(counts, on=col, how='left')
				.merge(raw_data,on=col, how='left')
			)
	
	return result

def saved(result,out):
	if out.endswith('.txt') or out.endswith('.xls'):
		result.to_csv(out,sep='\t',index=False)
	elif out.endswith('.csv'):
		result.to_csv(out,sep=',',index=False)
	else:
		print('Error:the format of outfile is not compatible, change .xls or .txt or .csv')
		sys.exit()
	
if __name__ == "__main__":
	import pandas as pd
	import sys
	import getopt
	
	#get command parameter
	para = main(sys.argv[1:])
	file = [para['rf'], para['tf']]
	sep = [para['rf_sep'],para['tf_sep']]
	col = para['col']
	out = para['of']
	
	#input raw_ and target_ file, list
	data = read_data(file,sep)
	
	#the counts of entry, df
	counts = value_counts(data[1],col)
	
	#merged results containing counts and targeted entry, df
	result = data_merge(data,counts)
	
	#saved to file
	saved(result,out)
