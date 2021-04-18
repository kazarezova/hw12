import pandas as pd
import numpy as np
from scipy.stats import shapiro

df = pd.read_csv("breast_cancer_1000_genes.tsv", sep="\t", index_col=0)
df['shapiro']=[shapiro(df.loc[gene].iloc[0:100])[1] for gene in df.index]
len_before=len(df)
df=df.loc[df['shapiro']>0.05]
print(round(len(df)/len_before*100,3),'%')