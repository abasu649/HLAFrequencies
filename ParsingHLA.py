#ParsingHLA
import csv
import pandas as pd 

genesHLA = {}
counts = {}
af = {}
afSorted = []

# Change current working directory 
loc = ("/Users/anamikabasu/Desktop/AFND0003326.csv") 

df = pd.read_csv("/Users/anamikabasu/Desktop/AFND0003326.csv",header=None)

for row in range(0,len(df.index)):
    for col in df.columns: #potential problem, what if the column names are not int
        if isinstance(df.iloc[row,col],str) and "*" in df.iloc[row,col]: 
            allele = df.iloc[row,col]
            gene = allele.split("*")[0]
#             if genesHLA not in globals():
#                 genesHLA = {}
            if gene not in genesHLA:
                genesHLA.update({gene : {}})
                counts.update({gene : 0})
            if allele not in genesHLA[gene]:
                genesHLA[gene].update({allele:1})
                counts.update({gene : counts[gene] + 1})
            else:
                genesHLA[gene].update({allele:genesHLA[gene][allele] +1})
                counts.update({gene : counts[gene] + 1})
    
for gene in genesHLA.keys():
    af.update({k:(v/counts[gene]) for (k,v) in genesHLA[gene].items()})

sortedValue = sorted(af.values(), reverse=True)
sortedKey = sorted(af, key=af.__getitem__, reverse=True)

for k, v in zip(sortedKey, sortedValue):
    afSorted.append([k,v])

print(afSorted)

print(afSorted)

