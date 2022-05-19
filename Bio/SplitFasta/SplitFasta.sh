#使用linux命令更方便
##若每4行为1个read,正反向共占8行
#正向
awk '{if(NR%8 == 1){print}}{if(NR%8 == 2){print}}{if(NR%8 == 3){print}}{if(NR%8 == 4){print}}' 目标文件 > 正向文件
#反向
awk '{if(NR%8 == 5){print}}{if(NR%8 == 6){print}}{if(NR%8 == 7){print}}{if(NR%8 == 0){print}}' 目标文件 > 反向文件

##若每2行为1个read,正反向共占4行
#正向
awk '{if(NR%4 == 1){print}}{if(NR%4 == 2){print}}' 目标文件 > 正向文件
#反向
awk '{if(NR%4 == 3){print}}{if(NR%4 == 0){print}}' 目标文件 > 反向文件
