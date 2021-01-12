import sys
import pandas as pd

gene_ID_file = sys.argv[1]
input_vcf_file = sys.argv[2]
output_subset_file = sys.argv[3]

df1 = pd.read_csv(gene_ID_file)
#df2 = pd.read_csv(input_vcf_file, sep = "\t", header= None, low_memory=False)
df2 = pd.read_excel(input_vcf_file)
#df2.columns = ['chr','start','end','REF','ALT','rsID']


df_2_subset = df2[df2.Gene_refGene.isin(df1.Gene_Names)]
df_2_subset.to_excel(output_subset_file)


# df_2_subset = df2[df2.Gene_refGene.isin(df1.Gene_ID)]
# df_2_subset.to_excel(output_subset_file)






