synonymous_snps
=======
function: correlation analysis between synonymous and disease
## 1. Download data
* Use Entrez Programming Utilities (E-utilities)
* NCBI had changed the form of snp database, now the data of synonymous data can't be esearched by using entrez-direct. 
## 2. Calculate the frequency of amino acids
I try to get the frequnece of each of amino acid in different Ssnps and use chi-square to calculate the significance 
### 2.1 get the amino acid of each Ssnps
Use the python script 
