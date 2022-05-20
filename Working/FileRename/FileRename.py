#本脚本用于文件重命名
#需自行准备一个重命名的文件(csv,txt,tsv格式),第一列为旧文件名,第二列为新文件名
import os
import sys

#定义一个函数,打开文件
def read_file(rename):
  if os.path.splitext(rename)[1] not in ['.txt','.tsv','.csv']:
    print('\n--------------------------文件后缀需为csv,txt,tsv中的一种-------------------------\n')
    print('\n---------------------------------------退出---------------------------------------\n')
    sys.exit(1)
  else:
    sep = '\t' if os.path.splitext(rename)[1] in ['.txt','.tsv'] else ','

  try:
    with open(rename,'r') as f1:
      file = f1.read().splitlines()
      file = sum([i.split(sep) for i in file[:]],[])
      return file
  except FileNotFoundError:
    print('\n---------------------------------未找到改名文件-----------------------------------\n')
    print('\n---------------------------------------退出---------------------------------------\n')
    sys.exit(1)

#定义一个函数,检查旧文件是否存在,新文件是否重命名
def file_exist(old_file,new_file):
  if len(old_file) != len(list(set(old_file))):
    print('\n需要改名的文件有重复,请检查')
    print('\n---------------------------------------退出---------------------------------------\n')
    sys.exit(1)
  
  all_file = os.listdir()
  if len(list(set(old_file) - (set(all_file) & set(old_file)))) != 0:
    print('\n需要改名的文件在本文件夹中不存在,请检查--{0}'.format(list(set(old_file) - (set(all_file) & set(old_file)))))
    print('\n---------------------------------------退出---------------------------------------\n')
    sys.exit(1)
  if len(list(set(all_file) & set(new_file))) != 0:
    print('\n新命名的文件在本文件夹中已存在,请检查--{0}'.format(list(set(all_file) & set(new_file))))
    print('\n---------------------------------------退出---------------------------------------\n')
    sys.exit(1)
  

rename = input('''\n-----------------------------------------------------------------------------------------------------\n
------[参数设定：具体格式参照rename.txt或rename.csv或rename.tsv,第一列为旧文件名,第二列为新文件名]\n
------[请输入改名文件(参数设定见上,输入完按回车)]:''')

#导入文件
file = read_file(rename)
old_file = file[0::2]
new_file = file[1::2]
file_exist(old_file,new_file)

#重命名文件
print('\n---------------------------------------正在改名---------------------------------------\n')
for i in range(int(len(file)/2)):
  os.rename(old_file[i],new_file[i])
else:
  print('\n---------------------------------------改名完成---------------------------------------\n')    
