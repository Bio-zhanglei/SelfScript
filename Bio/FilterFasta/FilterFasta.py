###一些测序结果中,每个read的长度是不固定的
###这个脚本帮助我们只保留大于特定碱基数量的read

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

#自定义数据,file原始文件,number为每一条read对应几行,如果只有两行改为2,length即read最小长度
file = 'RawFasta.txt'
number = 4
length = 250

#读取数据
with open(file,'r') as f1:
  raw_fasta = f1.read().splitlines()

#一维转二维,原始数据每四行为一条read结果
raw_fasta_group = list_of_groups(raw_fasta,number)

#筛选大于250nt的read,并添加空字符,有利于最后一行添加换行符
filter_fasta = sum([i for i in raw_fasta_group if len(i[1]) >= length],[])
filter_fasta.append('')

#导出数据
with open('Filter_{0}'.format(file),'w') as f1:
  f1.write('\n'.join(filter_fasta))
