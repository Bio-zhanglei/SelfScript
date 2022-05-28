#这只是一个笔记,仅供参考
#DIAMOND与BLAST具有相似功能,C+语言开发，所以其比BLAST快500到20,000倍
#其功能是将蛋白序列或者其翻译后的核苷酸和蛋白质数据库进行比对，与blast相比功能单一，但也让它的使用格外的简单。

#准备工作,安装diamond,下载源文件直接解压就能用(注意自己把他添加到环境变量中)
wget http://github.com/bbuchfink/diamond/releases/download/v2.0.14/diamond-linux64.tar.gz
#网络不好,直接去https://github.com/bbuchfink/diamond/releases下载linux版本
tar -zxzf diamond-linux64.tar.gz

#把diamond添加进环境变量,否则下面命令都需要在diamond安装目录下使用./diamond才能启动diamond
diamond makedb --in Arabidopsis_thaliana.TAIR10.pep.all.fa --db nr
#--in: 后面跟蛋白质数据库
#--db： 指定生成的diamond数据库名称

#只有两个子命令，blastx和blastp，前者比对DNA序列，后者比对蛋白
diamond blastx --db nr -q query.fa -o dna.txt --outfmt 6
diamond blastp --db nr -q query.fa -o protein.txt --outfmt 6

#但好像结果与blast不一致,我更推荐用blast,结果更多,blast的evalue默认是0.001
