# write by gaoli
# time:2019/2/27
# 对snpid_amoni_acid文件进行操作，统计每种氨基酸的数量，
# 为接下来的卡方检验做准备工作
# coding = utf-8
def count_amoni_acid_number(snpid_amino_txt):
    fo = open("amino_acid_num.txt", 'w')
    amino_acid_num = {}
    with open(pa_snpid_amino_txt, 'r') as fi:
        amino_acid = []
        for line in fi:
            sep = line.strip().split()
            amino_acid.append(sep[1])
        for i in amino_acid:
            if i not in amino_acid_num.keys():
                amino_acid_num[i] = amino_acid.count(i)
    for keys, values in amino_acid_num.items():
        fo.write('\t'.join([keys, str(values)]) + '\n')
count_amoni_acid_number()
