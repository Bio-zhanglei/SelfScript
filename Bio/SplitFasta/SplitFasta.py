###一些文件会将双端测序结果合并为一个文件
###即交叉出现一条序列的正反测序结果,如下
#####ID1_F(4行)
#####ID1_R(4行)
#####......
#####IDn_F(4行)
#####IDn_R(4行)
###我们需要将其分割为两个文件,正向测序结果文件F,反向测序结果文件R

#自定义数据
#file是原始文件,number是每几行为一个F或R测序结果,如果原始文件上述所说4行为2行,则number改为2
file = 'MergeFasta.txt'
number = 4

#导入原始文件
with open(file,'r') as f1:
  merge_fasta = f1.read().splitlines()

#提取出正反端测序数据
merge_fasta_temp = [merge_fasta[i:i + number] for i in range(0, len(merge_fasta), number)]
F_fasta = sum(merge_fasta_temp[::2],[])
R_fasta = sum(merge_fasta_temp[1::2],[])

#导出正反端测序数据
for i in ('F_fasta','R_fasta'):
  with open('{0}_{1}'.format(i,file),'w') as f1:
    f1.write('\n'.join(eval(i)))
