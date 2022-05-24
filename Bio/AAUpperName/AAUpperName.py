#此脚本用于将氨基酸全称转为其对应大写字母。
#你可以如下执行查看一个示例的结果(更多帮助输入'python dropDuplicates.py -h')
#python AaName.py -i sample.txt -o result.txt
Name = {
      'Ala':'A',
      'Arg':'G',
      'Asn':'N',
      'Asp':'D',
      'Cys':'C',
      'Gln':'Q',
      'Glu':'E',
      'Gly':'G',
      'His':'H',
      'Ile':'I',
      'Leu':'L',
      'Lys':'K',
      'Met':'M',
      'Phe':'F',
      'Pro':'P',
      'Ser':'S',
      'Thr':'T',
      'Trp':'W',
      'Tyr':'Y',
      'Val':'V',
}
#Translation = {
#        'UUU' : 'F', 'CUU' : 'L', 'AUU' : 'I', 'GUU' : 'V',
#        'UUC' : 'F', 'CUC' : 'L', 'AUC' : 'I', 'GUC' : 'V',
#        'UUA' : 'L', 'CUA' : 'L', 'AUA' : 'I', 'GUA' : 'V',
#        'UUG' : 'L', 'CUG' : 'L', 'AUG' : 'M', 'GUG' : 'V',
#        'UCU' : 'S', 'CCU' : 'P', 'ACU' : 'T', 'GCU' : 'A',
#        'UCC' : 'S', 'CCC' : 'P', 'ACC' : 'T', 'GCC' : 'A',
#        'UCA' : 'S', 'CCA' : 'P', 'ACA' : 'T', 'GCA' : 'A',
#        'UCG' : 'S', 'CCG' : 'P', 'ACG' : 'T', 'GCG' : 'A',
#        'UAU' : 'Y', 'CAU' : 'H', 'AAU' : 'N', 'GAU' : 'D',
#        'UAC' : 'Y', 'CAC' : 'H', 'AAC' : 'N', 'GAC' : 'D',
#        'CAA' : 'Q', 'AAA' : 'K', 'GAA' : 'E', 'CAG' : 'Q',
#        'AAG' : 'K', 'GAG' : 'E', 'UGU' : 'C', 'CGU' : 'R',
#        'AGU' : 'S', 'GGU' : 'G', 'UGC' : 'C', 'CGC' : 'R',
#        'AGC' : 'S', 'GGC' : 'G', 'CGA' : 'R', 'AGA' : 'R',
#        'GGA' : 'G', 'UGG' : 'W', 'CGG' : 'R', 'AGG' : 'R',
#        'GGG' : 'G',
#        'UAG' : 'STOP' , 'UGA' : 'STOP' , 'UAA' : 'STOP',
#}
def main(argv):
    #get command
    try:
        options, args = getopt.getopt(argv, "hi:c:o:m:", ["help","inputFile=","outFile="])
    except getopt.GetoptError:
        print('Error: python AaName.py -i <rawfile> -o <outfile>')
        print('   or: python AaName.py --inputFile=<inputFile> --outFile=<outfile>')
        sys.exit(2)

    para={}
    for option, value in options:
        if option in ("-h", "--help"):
            print('''
Version:miniconda python 3.7
Author:zhanglei, 2022/05/24
This script is for converting full names of AA to their uppercase-format.
You need to use the command like: 
    python AaName.py -i <inputfile>-o <outfile>
    Among these:
        -i is needed   (inputFile,such as one of sample.txt
        -o is optional (outFileName, default is result_inputFile, such as result_sample.txt).
            ''')               
            sys.exit()
        
        if option in ("-i", "--inputFile"):
            para['if'] = value
        if option in ("-o", "--outFile"):
            para['of'] = value
            
    #check rawfile, targetfile, merge_colnames and outfile
    if 'if' not in para:
        print('Error:inputfile is needed')
        sys.exit(2)
    if ('of' not in para):
        para['of'] = "result_" + para['if']
        
    return para

def UpperName(file,out):
    with open(file,'r') as f1:
        faa = f1.read().splitlines()
        ID_index = [i for i in range(len(faa)) if faa[i].startswith('>')]
        ID_fasta = dict.fromkeys([faa[i] for i in ID_index])
        
        ID_index.append(len(faa))
        for i,j in enumerate(ID_index[:-1]):
            FullName = ''.join(faa[ID_index[i]+1:ID_index[i+1]]).replace(' ','')
            for m in Name:
                FullName = FullName.replace(m,Name[m])
            else:
                ID_fasta[faa[j]] = FullName   
    
    with open(out,'w') as f2:
        f2.write('\n'.join(sum(ID_fasta.items(),())))
            

if __name__ == "__main__":
    import sys
    import getopt
    
    #get command parameter
    para = main(sys.argv[1:])
    file = para['if']
    out = para['of']
    
    #drop_duplicates
    UpperName(file, out)
