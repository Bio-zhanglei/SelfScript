import os
import sys

#定义一个函数,判断是否没有找到目标类型文件
def isempty(name_list):
  if name_list == []:
    print('未找到{0}文件类型请重新输入'.format(suffix))
    sys.exit(1)
    
#定义一个函数,输出文件
def output(suffix,name_suffix):
  print('\n--------------------------文件结果正在输出--------------------------\n')
  with open('{}_name.tsv'.format(suffix),'w') as f1:
    f1.write('\n'.join(name_suffix))
  print('\n---------------------------文件结果已输出---------------------------\n')

#用户自定义输入文件类型
suffix = input('''============================================================================================================================================\n
------[参数设定：所有文件(输入file);所有文件夹(输入dir),所有文件夹即文件(输入all);一种类型文件(输入如txt或.txt);无后缀的文件名不需要任何输入]\n
------[请输入你需要导出的文件名后缀(参数设定见上,输入完按回车)]:''')

#得到所有文件的分类信息
name = os.listdir()
name_style = {'all':name,
              'dir':[i for i in name if os.path.isdir(i)],
              'file':[i for i in name if os.path.isfile(i)]}
#输出文件
if suffix in ['all','dir','file']:
  isempty(name_style[suffix])
  output(suffix,name_style[suffix])
elif suffix == '':
  name_suffix = [i for i in name_style['file'] if os.path.splitext(i)[1] == '']
  isempty(name_suffix)
  output('nosuffix',name_suffix) 
else:
  suffix = suffix if '.' in suffix else '.'+suffix
  name_suffix = [i for i in name_style['file'] if os.path.splitext(i)[1] == suffix]
  isempty(name_suffix)
  output(suffix.strip('.'),name_suffix)
