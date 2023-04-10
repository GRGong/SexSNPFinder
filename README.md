# SexSNPFinder
Script for sex-linked SNPs identification in VCF


# Usage:
```{python}
python SexFinder.py <female sample file> <male sample file> <vcf>
```
# Note
The script is designed for XX/XY species and the ref is XX.
For ZZ/ZW, please use ZZ as ref to call SNP and swicth the female sample file and male sample file as follow:
```{python}
python SexFinder.py <male sample file> <female sample file> <vcf>
```

feamle and male sample files contain one sample per line

vcf should be gzipped or bgzipped

