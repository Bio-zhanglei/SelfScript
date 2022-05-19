#如果使用linux一行命令也许可以解决
#对于压缩文件
zcat 压缩文件 | awk '{if(NR%4 == 1){print ">" substr($0, 2)}}{if(NR%4 == 2){print}}' > 结果文件
#如果不是压缩文件
awk '{if(NR%4 == 1){print ">" substr($0, 2)}}{if(NR%4 == 2){print}}' 目标文件 > 结果文件
