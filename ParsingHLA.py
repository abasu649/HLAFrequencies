#ParsingHLA
import csv
import pandas as pd 

genesHLA = {}

# Change current working directory 
loc = ("/Users/anamikabasu/Desktop/AFND0003326.csv") 

df = pd.read_csv("/Users/anamikabasu/Desktop/AFND0003326.csv",header=None)

for row in range(0,len(df.index)):
	for col in df.columns: #potential problem, what if the column names are not int
		if isinstance(df.iloc[row,col],str) and "*" in df.iloc[row,col]: 
			allele = df.iloc[row,col]
			gene = allele[0]
			if gene not in genesHLA:
				genesHLA.update({gene : {}})
			if gene in genesHLA:
				if allele not in genesHLA[gene]:
					genesHLA[gene].update({allele:1})
				else:
					genesHLA[gene].update({allele:genesHLA[gene][allele] +1})

print(genesHLA)


