df_rel = pd.read_csv("colon_cancer_tumor_vs_normal_paired_FPKM.tsv", sep="\t", index_col=0)
df_rel['ttest']=[ttest_rel(df_rel.loc[gene].iloc[0:5], df_rel.loc[gene].iloc[5:10])[1] for gene in df_rel.index]
df_rel=df_rel.sort_values('ttest').loc[df_rel['ttest']<0.05]
print('число дифференциально экспрессированных генов, парный критерий Стьюдента:',len(df_rel))
rel_genes=df_rel.iloc[0:10].index

df_ind = pd.read_csv("colon_cancer_tumor_vs_normal_paired_FPKM.tsv", sep="\t", index_col=0)
df_ind['ttest']=[ttest_ind(df_ind.loc[gene].iloc[0:5], df_ind.loc[gene].iloc[5:10])[1] for gene in df_ind.index]
df_ind=df_ind.sort_values('ttest').loc[df_ind['ttest']<0.05]
print('число дифференциально экспрессированных генов, непарный критерий Стьюдента:',len(df_ind))
ind_genes=df_ind.iloc[0:10].index

print('Сколько общих генов содержат списки топ-10 наиболее значимо дифференциально экспрессированных генов?',
      len(rel_genes.intersection(ind_genes)))
print(rel_genes.intersection(ind_genes))