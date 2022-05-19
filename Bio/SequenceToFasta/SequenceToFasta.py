###将原始测序数据(每四行一个read)转为blast等软件需要的fasta格式数据(每两行是一个测序结果)
###同时每个read的ID的@符号转为>符号(可选)

file = 'SequenceData.txt'
ID_symbol = '>'

with open(file,'r') as f1:
  sequence_data = f1.read().splitlines()

#获取id
sequence_id = sequence_data[0::4]

#获取测序read
sequence_read = sequence_data[1::4]
