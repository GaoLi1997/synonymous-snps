# write by gaoli for operating the snpid_amino file
# splite the gene of each snpid
__author__ = 'GaoLi'

def change_snpid_amino(snpid_amino_file):
    fo = open('snpid_amino_new.txt', 'w')
    with open(snpid_amino_file, 'r') as fi:
        for line in fi:
            sep = line.strip().split('\t')
            gene = sep[2].split(',') # a list
            # eg: IGF2:3481,INS-IGF2:723961,MIR483:619552
            for i in range(0,len(gene)):
                geneid = gene[i].split(':')[0]
                entrezid = gene[i].split(':')[1]
                fo.write('\t'.join([sep[0], sep[1], geneid, entrezid])+ '\n')
    fo.close()

change_snpid_amino()
