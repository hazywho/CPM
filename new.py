import pandas as pd
names = list(map(str,input().split(",")))
newname=[]
for i in names:
    newname.append(i)
newname=newname.sort()
df = pd.DataFrame()
df["Names"]=newname
df.to_csv("hi")