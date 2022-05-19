#这只是一个笔记,仅供参考
#blast主要用于测序数据集,与nr数据库或者其他数据库进行比对
#也可以将自己的测序数据集作为数据库,查找某一个特定的序列
#我主要需要的是第二种,第一种需要构建的数据库较大,我直接使用了公司的结果

#准备工作,安装blast,建议通过conda安装,同时也(可选)安装perl模块
conda install -c bioconda blast
conda install perl-digest-md5
#准备一个数据集,比如自己的测序数据(也可以是氨基酸序列,可以参照拟南芥原始数据)
#wget ftp://ftp.ensemblgenomes.org/pub/plants/release-36/fasta/arabidopsis_thaliana/dna/Arabidopsis_thaliana.TAIR10.dna.toplevel.fa.gz
#gzip -d Arabidopsis_thaliana.TAIR10.dna.toplevel.fa.gz
#注意,这里的测序数据有格式要求,为一行id一行测序结果,id需要以>开头
#如何把原始测序数据转为blast所需要的数据格式,可以参照Bio/SequenceToFasta内的脚本

#第一步，构建索引数据库
makeblastdb -in <数据库> \
            -dbtype <数据库类型> \
            -out <输出文件的前缀> \
            -parse_seqids
			
	    #以下是参数的解释
	    数据库是一行id一行测序结果的文件
	    数据库类型，与数据库一致，nucl或者prot
	    out 输出结果文件的前缀
		主要的三个文件时库索引(in),头索引(hr),序列索引(sq)，还有三个是si ,sd ,og
	    parse_seqids 不添加最终生成的文件只有三个in,hr,sq文件,另外三个有什么用我也不太清楚
			
#第二步，选择合适blast软件
	查找序列类型	数据库类型	对其数据类型	软件
	n	n	n	blastn
	p	p	p	blastp
	n	p	p	blastx
	p	n	p	tblastn
	n	n	p	tblastx
	
#第三步,运行blast,这里我需要n → n → n,所以选择blastn
blastn -query <查找的序列> \
       -db <数据库> \
       -out <结果文件> \
       -task <搜索算法> \
	   -outfmt 7 \
	   -evalue 1 \
	   -num_thread <线程数>
	   
	   #以下是参数的解释
	   要查找的序列,其数据格式也是一条id一条序列,与数据库格式一致
	   数据库,与makeblastdbde的out参数一致
	   搜索算法,一般建议设置为blastn,其他可选参数为blastn-short,dc-megablast,megablast,rmblastn
				对于特别短的序列例如20bp左右的序列，在查找的时候我们需要使用blastn-short,并多设置参数，如下
										 -task blastn-short
										 -word_size 4 \该参数只能指定4以上的值
										 -evalue 1 \
	   outfmt,输出格式,0-17,建议为7,因为感官最舒服
	   evalue,E值阈值，高于这个E值的序列不输出到结果中，默认值为10，建议设到10-5以下
	   num_thread,支持多线程
	   
#更多使用方法见
makeblastdb -help
