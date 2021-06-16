import PyPDF2 as pdf
import pandas as pd
from sqlalchemy import create_engine
import sqlite3

conn = sqlite3.connect('products.db')


file = open('Price-Monitoring-June-10-2021.pdf', 'rb')
fileReader = pdf.PdfFileReader(file)
page = fileReader.getPage(0)
textPage = page.extractText()
#forbidden = ['NFA RICE',  'SPICES', 'LOCAL COMMERCIAL RICE', 'LIVESTOCK & POULTRY PRODUCTS', 'LOWLAND VEGETABLES','HIGHLAND VEGETABLES', 'OTHER BASIC COMMODITIES', ',NOT AVAILABLE']
forbidden = ['NFA RICE', 'NOT AVAILABLE']
convertedPage = []

splitPage = textPage.splitlines()



for i in splitPage:
	if i not in forbidden:
		convertedPage.append(i)
	
#print(textPage)
#print(splitPage)
del convertedPage[0:8] 
  
livestock = convertedPage[76:113]
lowvegetables = convertedPage[113:151]
high_vegetable = convertedPage[151:188]
spices = convertedPage[188:268]
commodities = convertedPage[268:299]
 
#print(convertedPage.index('LIVESTOCK & POULTRY PRODUCTS'))
#print(convertedPage.index('LOWLAND VEGETABLES'))
#print(convertedPage.index('HIGHLAND VEGETABLES'))
#print(convertedPage.index('SPICES'))
#print(convertedPage.index('OTHER BASIC COMMODITIES'))
#print(convertedPage.index('.'))

print(lowvegetables)


df = pd.DataFrame(
[[ livestock[1], livestock[4], livestock[5], livestock[6]],
[livestock[7], livestock[10], livestock[11], livestock[12] ],
[livestock[13], livestock[16], livestock[17], livestock[18] ],
[ livestock[20], livestock[22], livestock[23], livestock[24] ],
[ livestock [25], livestock[28], livestock[29], livestock[30] ],
[ livestock [31], livestock[34], livestock[35], livestock[36] ]],
columns = ['Product', 'High', 'Low', 'Prevailing']
)


low_vegetableDF = pd.DataFrame(
[[ lowvegetables[1], lowvegetables[4], lowvegetables[5], lowvegetables[6] ],
[ lowvegetables[7], lowvegetables[10], lowvegetables[11], lowvegetables[12]],
[ 'Pechay Native' , lowvegetables[17], lowvegetables[18], lowvegetables[19] ],
[ lowvegetables[20], lowvegetables[23], lowvegetables[24], lowvegetables[25] ],
[ lowvegetables[26], lowvegetables[29], lowvegetables[30], lowvegetables[31] ],
[ lowvegetables[32], lowvegetables[35], lowvegetables[36], lowvegetables[37] ]],
columns = ['Product', 'High', 'Low', 'Prevailing'])
 
dtf = pd.DataFrame(high_vegetable)
 
high_vegetableDF = pd.DataFrame(
[ [ high_vegetable[32], high_vegetable[34], high_vegetable[35], high_vegetable[36] ],
[ high_vegetable[1], high_vegetable[5], high_vegetable[6], high_vegetable[7] ],
[ high_vegetable[11], high_vegetable[12], high_vegetable[13] ],
[ high_vegetable[14], high_vegetable[17], high_vegetable[18], high_vegetable[19] ],
[ high_vegetable[20], high_vegetable[23], high_vegetable[24], high_vegetable[25] ],
[ high_vegetable[26], high_vegetable[29], high_vegetable[30], high_vegetable[31] ]],
columns = ['Product', 'High', 'Low', 'Prevailing']
)

high_vegetableDF.columns.str.split
low_vegetableDF.columns.str.split
df.columns.str.replace(' ', '') 


print(high_vegetableDF)
print(df)
print(low_vegetableDF)

print(df.columns)
#Do Not Touch!!
#high_vegetableDF.to_sql(name="produkto", con = conn, if_exists = 'replace', index = False)
#low_vegetableDF.to_sql(name="produkto", con = conn, if_exists = 'append', index = False)
#df.to_sql(name="produkto", con = conn, if_exists = 'append', index = False)
file.close()