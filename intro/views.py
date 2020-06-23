from django.shortcuts import render
import csv 
import pandas as pd
import numpy as np
import os
import re

def moviesearch(request):
    dict1=request.POST
    txt=dict1["search"]
    print(dict1)
    with open('moviesearchlist.csv','a') as csvfile:
            wrt=csv.writer(csvfile)
            for key,value in dict1.items():
                wrt.writerow([key,value])
    df=pd.read_csv("newmovies.csv",index_col="imdb_title_id")
    titles=df["title"]
    titles

    outdisp=df[["title","language","year"]]
    outputd=pd.DataFrame(outdisp)

    rating=df[["avg_vote"]]
    ratd=pd.DataFrame(rating)


    search=txt.lower().replace(" ","")
    tilname=[]
    '''
    for i,j in titles.items():
        if(j==search):
            tilname.append(i)
    if(len(tilname)>1):
        resd=outputd[tilname]
    print(tilname)
    '''
    if(len(tilname)==0):
        mout=[];crct="";
        for i,j  in titles.items():
            str=j.split(" ")
            ans=""
            for k in str:
                ans+=k.lower()
            pat="^"+search+".*"
            pat2="^"+search+"$"
            if(re.search(pat2,ans)):
                crct=i
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
        resd=outputd.loc[tilname]

        if(not crct==""):
            bst=outputd.loc[crct]
            print(bst["title"])
            fis=pd.DataFrame({'title':bst["title"],"language":bst["language"],"year":bst["year"]},index=[0])
            resd = pd.concat([fis, resd[:]]).reset_index(drop = True) 
            print(resd.head(5))

    resdf=pd.DataFrame(resd)
    htres=resdf.to_html(index=False)
    f=open('template/intro.js','w') 
    fir=open('template/introfirst.txt',"r")
    sec=open('template/introsec.txt',"r")
    txt1=fir.read()
    txt2=sec.read()
    if(resdf.empty):
        tx=txt1+"<center><h1>No movie found</h1></center>"+txt2
        f.write(tx  )
    else:
        f.write(txt1)
        f.write('<center>')
        f.write(htres)
        f.write('</center>')
        f.write(txt2)


'''
    tli=resd["title"]
    lli=resd["language"]
    yli=resd["year"] 
    print(tli,lli,yli,type(tli))
    base = os.path.dirname(os.path.abspath(__file__))
    html = open(os.path.join('/home/dhuvaraggnajithraj/vscode-project/djangofirst/firstweb/first/template', 'intro.js'))
    soup = BeautifulSoup(html,features="lxml")
    tval=tli.values
    lval=lli.values
    yval=yli.values
    print(tval)
    print(lval)
    print(yval)
   # ,l,lv,y,yv  ,lli.items(),yli.items()

    for i in soup.find(id="t1").find_all():
        i.replace_with(tval[0])
    for i in soup.find(id="t2").find_all():
        i.replace_with(tval[1])
    for i in soup.find(id="t3").find_all():
        i.replace_with(tval[2])

    for i in soup.find(id="l1").find_all():
        i.replace_with(lval[0])
    for i in soup.find(id="l2").find_all():
        i.replace_with(lval[1])
    for i in soup.find(id="l3").find_all():
        i.replace_with(lval[2])
    

    with open("template/intro.js", "wb") as f_output:
        f_output.write(soup.prettify().encode('utf-8'))  

    for i in soup.find(id="y1").find_all():
        i.replace_with(int(yval[0]))
    for i in soup.find(id="y2").find_all():
        i.replace_with(yval[1])
    for i in soup.find(id="y3").find_all():
        i.replace_with(yval[2])
'''    

# Create your views here.
def introget(request):
    if request.method=='POST':
        moviesearch(request)
    return render(request,'intro.js')

def startapp(request):
    return render(request,'index.html')

def getstart(dic):
    yearv=dic["year"];languagev=dic["lang"];genrev=dic["genre"]
    print(yearv,languagev,genrev)
    df=pd.read_csv("newmovies.csv",index_col="imdb_title_id")
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
    dpdf=df.drop(["votes"],axis=1)

    sortoutd=dpdf.loc[top]
    #print(sortoutd)
    resu=pd.DataFrame(sortoutd)

    movie=resu.to_html(index=False)
    searc=open('template/top50sea.txt','r')
    f=open('template/res.html','w') 
    f.write("<html><body>")
    f.write(searc.read())
    f.write(movie)
    f.write("</body></html>")

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
        with open('moviesearchtop.csv','a') as csvfile:
            wrt=csv.writer(csvfile)
            for key,value in dict1.items():
                wrt.writerow([key,value])

        
    return render(request,'res.html')


def searchtop(request):
    dict1=request.POST
    txt=dict1["search"]
    print(dict1)
    with open('moviesearchlist.csv','a') as csvfile:
            wrt=csv.writer(csvfile)
            for key,value in dict1.items():
                wrt.writerow([key,value])
    df=pd.read_csv("newmovies.csv",index_col="imdb_title_id")
    titles=df["title"]
    titles

    rating=df[["avg_vote"]]
    ratd=pd.DataFrame(rating)


    search=txt.lower().replace(" ","")
    tilname=[]

    if(len(tilname)==0):
        mout=[];crct="";
        for i,j  in titles.items():
            str=j.split(" ")
            ans=""
            for k in str:
                ans+=k.lower()
            pat="^"+search+".*"
            pat2="^"+search+"$"
            if(re.search(pat2,ans)):
                crct=i
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
        resrated=ressort.head(7)
        topse=resrated["avg_vote"]
        
        for i,j in topse.items():
            tilname.append(i)
        resd=df.loc[tilname]

        if(not crct==""):
            bst=df.loc[crct]
            fis=pd.DataFrame({'title':bst["title"],"language":bst["language"],"year":bst["year"],"writer":bst["writer"],"director":bst["director"],"date_published":bst["date_published"],"genre":bst["genre"],"country":bst["country"],"actors":bst["actors"],"description":bst["description"],"avg_vote":bst["avg_vote"]},index=[0])
            resd = pd.concat([fis, resd[:]]).reset_index(drop = True) 
          
    outdp=resd.drop(["votes"],axis=1)
    resdf=pd.DataFrame(outdp)
    result=resdf.to_html(index=False)

    s=open('template/topsear.html',"w") 
    sir=open('template/top50sea.txt',"r")
    if(resdf.empty):
        tx=sir.read()+"<center><h1>No movie found</h1></center></form></body></html>"
    else:
        tx=sir.read()+result+'</form></body></html>'
    s.write(tx)

    op=open('template/topsear.html',"r")

    s.close();sir.close();op.close()
    return render(request,'topsear.html')
