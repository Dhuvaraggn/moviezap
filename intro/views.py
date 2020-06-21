from django.shortcuts import render
import csv 
import pandas as pd
import numpy as np


# Create your views here.
def introget(request):
    return render(request,'intro.html')



def getstart(dic):
    yearv=dic["year"];languagev=dic["lang"];genrev=dic["genre"]
    print(yearv,languagev,genrev)
    df=pd.read_csv("~/Downloads/newmovies.csv",index_col="imdb_title_id")
    #txtfile=open("/template/res.html","w")

    lg=df["language"]
    langid=[]
    for i,j in lg.items():
        if(j==languagev):
            langid.append(i)    
    
    langsortd=df.loc[langid]

    yr=langsortd["year"]    
    yearid=[]
    if(yearv=="2000"):
        for i,j in yr.items():
            if(j>=2000 and j<=2020):
                yearid.append(i)
    elif(yearv=="1980"):
        for i,j in yr.items():
            if(j>=1980 and j<2000):
                yearid.append(i)
    elif(yearv=="1960"):
        for i,j in yr.items():
            if(j>=1960 and j<1980):
                yearid.append(i)
    elif(yearv=="1940"):
        for i,j in yr.items():
            if(j>=1940 and j<1960):
                yearid.append(i)
    elif(yearv=="1900"):
        for i,j in yr.items():
            if(j>=1900 and j<1940):
                yearid.append(i)
    #print(yearid)
    yearsortd=langsortd.loc[yearid]

    gen=yearsortd["genre"]
    genid=[]
    for i,j in gen.items():
        for k in j.split(", "):
            if(k==genrev):
                genid.append(i)
                break

    gensortd=yearsortd.loc[genid]

    rating=gensortd[["avg_vote","votes"]]

    ans=rating.sort_values(["avg_vote"],ascending=False)
    #top=ans.head(30).index
    nov=ans.sort_values(["votes"],ascending=False)
    top=nov.head(50).index

    sortoutd=df.loc[top]
    #print(sortoutd)
    resu=pd.DataFrame(sortoutd)
    movie=resu.to_html()
    f=open('template/res.html','w') 
    f.write("<html><body>")
    f.write('<form action="/intro/" method="POST"> <input class="gNO89b" aria-label="Google Search" name="btnK" type="submit" data-ved="0ahUKEwjbk4ul5orqAhX0xzgGHYlmAREQ4dUDCAo" value="MovieZap Search">  {% csrf_token %}</input>   </form>      ')
    f.write(movie)
    f.write("</body></html>")
    print(movie)
    return movie
    
  

def getmovie(request):
    print("start")
    if request.method=='POST':
        dict1=request.POST
        y=dict1["year"]
        g=dict1["genre"]
        l=dict1["lang"]
        dic={"year":y,"genre":g,"lang":l}
        getstart(dic)
        with open('moviesearch.csv','a') as csvfile:
            wrt=csv.writer(csvfile)
            for key,value in dict1.items():
                wrt.writerow([key,value])

        
    return render(request,'res.html')

