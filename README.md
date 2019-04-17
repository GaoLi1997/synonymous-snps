synonymous_snps
=======
function: correlation analysis between synonymous and disease
## 1. Download data
* Use Entrez Programming Utilities (E-utilities)
* NCBI had changed the form of snp database, now the data of synonymous data can't be esearched by using entrez-direct. 
## 2. Calculate the frequency of amino acids
I try to get the frequnece of each of amino acid in different Ssnps and use chi-square to calculate the significance 
### 2.1 get the amino acid of each Ssnps
Use the python script `get_amino_acid.py` to extract amino acid 
Use the python script `get_each_amino_acid_num` to caculate the number of every amino acid 
### 2.2 chi_square


