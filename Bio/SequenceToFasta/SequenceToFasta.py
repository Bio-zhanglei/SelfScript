###将原始测序数据(每四行一个read)转为blast等软件需要的fasta格式数据(每两行是一个测序结果)
###同时每个read的ID的@符号转为>符号(可选)

file = 'SequenceData.txt'
ID_symbol = '>'

#读取数据
with open(file,'r') as f1:
  sequence_data = f1.read().splitlines()

#获取id,替换@符号为>符号
sequence_id = sequence_data[0::4]
sequence_id = [ID_symbol+i[1:] for i in sequence_id[:]]

#获取测序read
sequence_read = sequence_data[1::4]

#转为fasta文件格式
fasta_format = sum(list(zip(sequence_id,sequence_read)),())

#输出文件
with open('fasta_{0}'.format(file),'w') as f1:
  f1.write('\n'.join(fasta_format))
