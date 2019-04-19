synonymous_snps
=======
function: correlation analysis between synonymous and disease
## 1. Download data
* Use Entrez Programming Utilities (E-utilities).
* NCBI had changed the form of snp database, now the data of synonymous data can't be esearched by using entrez-direct. 
## 2. Calculate the frequency of amino acids
I try to get the frequnece of each of amino acid in different Ssnps and use chi-square to calculate the significance. 
### 2.1 capture the amino acid of each Ssnps
Use the python script `get_amino_acid.py` to extract amino acid. 
Use the python script `get_each_amino_acid_num.py` to caculate the number of every amino acid.
### 2.2 chi_square

## 3. KEGG 
Capture all the genes from the Ssnps file
Kegg pathway analysis(R clusterprofiler)
### 3.1 capture genes
Each snp can located in multiple genes. The genes are binded together by the one snpid.
Use the python script 'get_amino_acid_v1.py' to modify the 'snpid_amino.txt'. We can splite the genes for next analysis(kegg pathway).
### 3.2 kegg pathway
```R
library(clusterProfiler)
setwd()
degenes <- read.csv(file, header = F,col.names = c(),stringsAsFactors = F, sep = '\t')
genelist <- degenes$entrezid
#genelist[duplicated(genelist)] 去重
kegg <- enrichKEGG(genelist, organism = "hsa", keyType = "kegg", pvalueCutoff = 0.05,
                   pAdjustMethod = "BH", minGSSize = 10, maxGSSize = 500, qvalueCutoff = 0.2,
                   use_internal_data = FALSE)
write.csv(data.frame(kegg),"all_benign_Ssnps_KEGG_enrich.csv",row.names =F)
dim(kegg) 
dotplot(kegg, showCategory=15, title = "Pathogenic synonymous KEGG")
```
## 4. modify the kegg file
Each row in kegg file concludes the pathway description and the enriched genes(entrez id)
Use the python script `kegg_snpid_amino_acid.py` to extract the amino acids of each entrez id. Next, run `count_all_amino_acid_kegg.py` to caculate the numbers of amino acid of every pathyway.

  


