from scipy import stats

CON = [1,3,4,2]
TRT = [2,4,5,7]
EMT = [3,4,2,4]

###非参数检验
#独立样本, 秩和检验, 近似显著性(大样本, >30)
stats.ranksums(CON, TRT)
#独立样本, 秩和检验, 精确显著性(小样本, <30)
stats.mannwhitneyu(CON, TRT)
#配对样本, 符号秩检验
stats.wilcoxon(CON, TRT)
#多组独立样本
stats.kruskal(CON, TRT, EMT)

