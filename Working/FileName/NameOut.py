import os
import sys

suffix = input('''==========================================================================================================\n
------[参数设定：所有文件(输入file);所有文件夹(输入dir),所有文件夹即文件(输入all);一种类型文件(输入如txt)]\n
------[请输入你需要导出的文件名后缀(参数设定见上)]:''')

if '.' in suffix:
  print('''请去除点(.)''')
  sys.exit(1)
  
Name = os.listdir()
Name_style = {'all':Name,
              'dir':[i for i in Name if os.path.isdir(i)],
              'file':[i for i in Name if os.path.isfile(i)]}

if suffix in ['all','dir','file']:
  with open('{}_name.txt'.format(suffix),'w') as f1:
    f1.writelines(
