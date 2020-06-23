import pandas as pd
import numpy as np
df=pd.read_csv("newmovies.csv",index_col="imdb_title_id")
df 

lg=df["language"]
langid=[]
for i,j in lg.items():
    if(j=="Tamil"):
        langid.append(i)
len(langid)    

langsortd=df.loc[langid]
langsortd

yr=langsortd["year"]
yr
d2000=[]
d1980=[]
d1960=[]
d1940=[]
d1900=[]
for i,j in yr.items():
    if(j>=2000 and j<=2020):
        d2000.append(i)
    if(j>=1980 and j<2000):
        d1980.append(i)
    elif(j>=1960 and j<1980):
        d1960.append(i)
    elif(j>=1940 and j<1960):
        d1940.append(i)
    elif(j>=1900 and j<1940):
        d1900.append(i)
len(d2000)

yearsortd=langsortd.loc[d2000]
yearsortd

gen=yearsortd["genre"]
gen
drama=[]
myst=[]
roman=[]
action=[]
comedy=[]
for i,j in gen.items():
    for k in j.split(", "):
        if(k=="Comedy"):
            comedy.append(i)
            break;
comedy

gensortd=yearsortd.loc[comedy]
gensortd

rating=gensortd[["avg_vote","votes"]]
rating


ans=rating.sort_values(["avg_vote"],ascending=False)
#top=ans.head(30).index
nov=ans.sort_values(["votes"],ascending=False)
top=nov.head(50).index

sortoutd=df.loc[top]
print(sortoutd)


