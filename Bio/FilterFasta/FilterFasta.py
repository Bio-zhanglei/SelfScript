###一些测序结果中,每个read的长度是不固定的
###这个脚本帮助我们只保留大于特定碱基数量的read

#定义一个函数,作用一维数组转为二维数组,如[1,2,3,4]转为
######[[1,2],[3,4]]
####或[[1],[2],[3],[4]]
####或[[1,2,3],[4]]
def list_of_groups(init_list, childern_list_len):
    list_of_groups = zip(*(iter(init_list),) *childern_list_len)
    end_list = [list(i) for i in list_of_groups]
    count = len(init_list) % childern_list_len
    end_list.append(init_list[-count:]) if count !=0 else end_list
    return end_list


file = 'RawFasta.txt'
number = 4
length = 250

#读取数据
with open(file,'r') as f1:
    raw_fasta = f1.read().splitlines()
#每四个拆分为一组,一维转二维
split_fasta = list_of_groups(raw_fasta,number)

#筛选大于250nt的read
filter_fasta = []
for i in split_fasta:
    #不小于500的序列保留
    if len(i[1]) >=length:
        filter_fasta.append(i)
    else:
        continue
else:
    filter_fasta = sum(clean_fasta,[])

#导出数据
with open('500_%s'%file,'w') as f1:
    f1.write('\n'.join(result_fasta))
