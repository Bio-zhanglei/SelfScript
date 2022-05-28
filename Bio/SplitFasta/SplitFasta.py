###一些文件会将双端测序结果合并为一个文件
###即交叉出现一条序列的正反测序结果,如下
#####ID1_F(4行)
#####ID1_R(4行)
#####......
#####IDn_F(4行)
#####IDn_R(4行)
###我们需要将其分割为两个文件,正向测序结果文件F,反向测序结果文件R

#定义一个函数,作用一维数组转为二维数组,如[1,2,3,4]转为
####或[[1],[2],[3],[4]], 即1*4
####或[[1,2],[3,4]], 即2*2
####或[[1,2,3],[4]], 即3*2,但是因为只有四个元素,最后一组只有1个4
####或[[1,2,3,4]], 即4*1
def list_of_groups(init_list, childern_list_len):
  list_of_groups = zip(*(iter(init_list),) *childern_list_len)
  end_list = [list(i) for i in list_of_groups]
  count = len(init_list) % childern_list_len
  end_list.append(init_list[-count:]) if count !=0 else end_list
  return end_list

#自定义数据
#file是原始文件,number是每几行为一个F或R测序结果,如果原始文件上述所说4行为2行,则number改为2
file = 'MergeFasta.txt'
number = 4

#导入原始文件
with open(file,'r') as f1:
  merge_fasta = f1.read().splitlines()

#提取出正反端测序数据,在最后添加空,有利于最后一行也有换行符
merge_fasta_group = list_of_groups(merge_data, number)
F_fasta = sum(merge_fasta_group[::2],[])
F_fasta.append('')
R_fasta = sum(merge_fasta_group[1::2],[])
R_fasta.append('')

#导出正反端测序数据
for i in ('F_fasta','R_fasta'):
  with open('{0}_{1}'.format(i,file),'w') as f1:
    f1.write('\n'.join(eval(i)))
