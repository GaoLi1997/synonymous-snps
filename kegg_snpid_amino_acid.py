# write by gaoli for operating the kegg file for finding the amino_acid of each gene entrez id
# time:2019/3/5
def kegg_file(snpid_amino_new_txt, kegg_file):
    fo = open('kegg_pathwayid_amino_acid.txt', 'w')
    with open(snpid_amino_new_txt, 'r') as fi:
        entrezid_amino = {}
        for line in fi:
            sep = line.strip().split('\t')
            entrezid = sep[-1]
            if entrezid not in entrezid_amino.keys():
                amino_acid = []
                amino_acid.append(sep[1])
                entrezid_amino[entrezid] = amino_acid
            else:
                entrezid_amino[entrezid].append(sep[1])
        print(entrezid_amino)
# 将每个基因上的突变对应的氨基酸做成字典

    with open(kegg_file, 'r') as filein:
        pathwayid_geneid = {}
        pathwayid_discription = {}
        for line1 in filein:
            if "ID" not in line1:  ##去掉第一行title
                sepa = line1.strip().split(',')
                pathway_id = sepa[0].replace('"', '')
                geneid = sepa[-2].replace('"', '').split('/')
                pathwayid_geneid[pathway_id] = geneid
                # 创建字典，key:pathwayid,value:geneid的list
                pathwayid_discription[pathway_id] = sepa[1].replace('"', '')

    for keys, values in pathwayid_geneid.items():
        li = []
        for gene_id in values:
            if gene_id in entrezid_amino.keys():
                amino_string = '/'.join(entrezid_amino[gene_id])
                li.append(amino_string) #把每个entrezid对应的氨基酸写进去
                string = '/'.join(li)
        fo.write('\t'.join([keys,pathwayid_discription[keys], string])+'\n')
    fo.close()
kegg_file()

