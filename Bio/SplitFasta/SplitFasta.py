###一些文件会将双端测序结果合并为一个文件
###即交叉出现一条序列的正反测序结果,如下
#####ID1_F
#####ID1_R
#####......
#####IDn_F
#####IDn_R
###我们需要将其分割为两个文件,正向测序结果文件F,反向测序结果文件R

file = 'MergeFasta.txt'
number = 4

with open(file,'r') as f1:
  merge_fasta = f1.read.splitlines()

[merge_fasta[i:i + number] for i in range(0, len(x), number)]
