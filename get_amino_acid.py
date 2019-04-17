# write by gaoli for find Ssnps with amino acid and geneid
# time: 2019/2/27
# coding=utf-8
# get the amino acid of each synonymous snps
import re
def snpid_amino_acid(pathogenic_txt):
    fo = open('snpid_amino.txt', 'w')
    snpid_ref = {}
    snpid_gene ={}
    with open(pathogenic_txt) as fi:
        for line in fi:
            sep = line.strip().split()
            snpid,docsum = sep[0],sep[-1]

            HGVS = docsum.strip().split('|')[1].replace('HGVS=', '')
            GENE = docsum.strip().split('|')[-1].replace('GENE=','')
            ref = HGVS.split(',') # creat a list
            protein_ref = []
            for i in ref:
                if "XP" in i or 'NP' in i or 'YP' in i:
                    protein_ref.append(i)# 保留带NP，XP的refrence
            snpid_gene[snpid] = GENE
            snpid_ref[snpid] = protein_ref #将snpid和蛋白质的ref做成字典
    pattern = re.compile(r'^(\wP_\d*.\d:p.)(\w{3})(.*)$')
        # hgvs_protein_np = re.compile(r'^(NP_\d*.\d:p.)(\w{3})(\d*=)$')
        # \w = [a-zA-z0-9_] \d = [0-9] .* 代表匹配除换行符之外的所有字符 
        # eg: XP_016876609.1:p.Tyr1511= or NP_001182502.1:p.Tyr1511=  (很迷的=， 貌似有的有，有的确没有)
        snpid_amoni_acid = {}
        for keys, values in snpid_ref.items():
            for syn_pro_ref in values: #values为XP,NP,YP等形成的字典
                syn_amoni_acid = []
                if pattern.match(syn_pro_ref) != None:
                    amoni_acid = pattern.match(syn_pro_ref).group(2) # 取出对应的氨基酸
                    syn_amoni_acid.append(amoni_acid) 
                    #将匹配上的SNP的氨基酸取出形成列表
                syn_amoni_acid = list(set(syn_amoni_acid))
                #将氨基酸去重复(一般来说只会剩下一个)
            snpid_amoni_acid[keys] = syn_amoni_acid

        for key,value in snpid_amoni_acid.items():
            if len(value) == 1:
                fo.write('\t'.join([key, value[0], snpid_gene[key]])+'\n')
            else:
                print(key)
        fo.close()
snpid_amino_acid('benign.txt')
