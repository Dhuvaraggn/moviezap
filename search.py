import pandas as pd 
import numpy as np
import re

df=pd.read_csv("newmovies.csv",index_col="imdb_title_id")
titles=df["title"]
titles

outdisp=df[["title","language","year"]]
outputd=pd.DataFrame(outdisp)
lang=df["language"]
for i,j in lang.items():
    if(j=="Tamil"):
        print(df.loc[i])
rating=df[["avg_vote"]]
ratd=pd.DataFrame(rating)

search="hey".lower().replace(" ","")
tilname=[]
for i,j in titles.items():
    if(j==search):
        tilname.append(i)
print(tilname)

if(len(tilname)==0):
    mout=[];
    for i,j  in titles.items():
        str=j.split(" ")
        ans=""
        for k in str:
            ans+=k.lower()
        pat="^"+search+".*"
        if(re.search(pat,ans)):
            mout.append(i)
    if(len(mout)==0):
        for i,j  in titles.items():
            str=j.split(" ")
            ans=""
            for k in str:
                ans+=k.lower()
            pat=".*"+search+".*"
            if(re.search(pat,ans)):
                mout.append(i)
        
    resrat=ratd.loc[mout]
    ressort=resrat.sort_values(["avg_vote"],ascending=False)
    resrated=ressort.head(5)
    topse=resrated["avg_vote"]
    
    for i,j in topse.items():
        tilname.append(i)
    res=outputd.loc[tilname]
    print(res)  
