#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def randomnumbergenerator(n1,n2):

    import random

    f=[]

    for i in range(n1):

        k=[]

        for j in range(n2):

            k.append(random.randint(0,10))

        f.append(k)

    return(f)





# In[3]:


def calculatedistancematrix(n,source,availabletaximatrix,sourcematrix):

    distancematrix=randomnumbergenerator(n,source)

    for i in range(n):

        for j in range(source):

            distancematrix[i][j]=abs((sourcematrix[j][0]-availabletaximatrix[i][0]))+abs((sourcematrix[j][1]-availabletaximatrix[i][1]))

    return(distancematrix)





# In[4]:





import numpy as np

def pickup(sourcelist,sourcelistn,availabletaximatrix,t,availabletaxi,filledtaxi,remainingrequest,filledrequest,destinationlist1,distancematrix): 

    result=[]

    sum2=[]

    destinationtime=[]

    sourcetime=[]

    length1=len(availabletaximatrix)

    length2=len(sourcelistn)

    distancematrix1=np.array(distancematrix)

    for k in range(length1):

        x=distancematrix1.min()

        y=distancematrix1.max()

        for i in range(length1):

            for j in range(length2):

                if(x==distancematrix1[i][j]):

                    pos1=availabletaxi[i]

                    filledtaxi.append(pos1)

                    pos=remainingrequest[j]

                    filledrequest.append(pos)

                    #remainingrequest.remove(pos)

                    sourcetime.append(x)

                    #destinationdistance.append(destinationlist1[pos])

                    sourcedistance=sourcelist[pos-1]

                    destinationdistance=destinationlist1[pos-1]

                    destinationtime.append(abs(sourcedistance[0]-destinationdistance[0])+abs(sourcedistance[1]-destinationdistance[1]))

                    for l in distancematrix1[i]:

                        distancematrix1[i]=distancematrix1.max()

                    distancematrix1[:,j]=distancematrix1.max()

                    break

            else:

                continue

            break

    #allotedrequest=list(filledrequest)

    #for j in allotedrequest:

        #destinationdistance.append(destinationlist1[j-1])

        #sourcelistn.remove(sourcelistn[j-1])

    #destinationtime=calculatedistancematrix2(length3,sourcedistance,destinationdistance)

    travellingtime=[]

    length3=len(filledrequest)

    for w in range(len(sourcetime)):

        travellingtime.append(sourcetime[w]+destinationtime[w])

    #travellingtime=list(map(lambda time:time+t,travellingtime))

    result.append(filledrequest)

    result.append(availabletaxi)

    result.append(sourcetime)

    result.append(travellingtime)

    result.append(remainingrequest)

    result.append(filledtaxi)

    return(result)





# In[5]:





p=int(input("enter the number of taxis"))

T=int(input("enter the total time of iteration"))

availabletaximatrix=randomnumbergenerator(p,2)

availabletaxi=[]

availabletaxilist=[]

sourcelistn=[]

remainingrequest=[]

for taxim in availabletaximatrix:

    availabletaxilist.append(taxim)

for i in range(p):

    availabletaxi.append(i+1)

filledtaxi=[]

filledrequest=[]

fullfilledrequest=[]

servicetime=[2,3,4]

totaltime=[]

sourcelist=[]

destinationlist=[]

d=0

for t in range(T):

    numsource=20

    destination=20

    sourcematrix=randomnumbergenerator(numsource,2)

    destinationmatrix=randomnumbergenerator(destination,2)

    for source in sourcematrix:

        sourcelist.append(source)

        sourcelistn.append(source)

    for destination in destinationmatrix:

        destinationlist.append(destination)

    g=d+(numsource-1)

    while(d<=g):

        remainingrequest.append(d+1)

        d=d+1

    if(len(availabletaxi)>0):

        distancematrix=calculatedistancematrix(len(availabletaxilist),len(sourcelistn),availabletaxilist,sourcelistn)

        taxirequest=pickup(sourcelist,sourcelistn,availabletaxilist,t,availabletaxi,filledtaxi,remainingrequest,filledrequest,destinationlist,distancematrix)

        filledrequest=taxirequest[0]

        availabletaxi=taxirequest[1]

        filledtaxi=taxirequest[5]

        #servicetime=taxirequest[2]

        #totaltime=taxirequest[3]

        for time in taxirequest[2]:

            servicetime.append(time)

        for time in taxirequest[3]:

            totaltime.append(time)

    #for tim in servicetime:

        #if(t==tim):

            #averageservicetime.append(tim)

        #for time in taxirequest[3]:

            #blocktime.append(time)

    #for tim in totaltime:

        #if(t==tim):

            #inde2=totaltime.index(tim)

            #availabletaxi.append(len(taxirequest[1])%p)

            #availabletaxilist.append(destinationlist[inde2])

            #if(len(availabletaxilist)>3):

                #availabletaxilist.remove(availabletaxilist[inde2%p+1])

            #sourcelist.remove(sourcelist[inde2%p+1])

            #if(len(availabletaxi)>0):

                #distancematrix=calculatedistancematrix(len(availabletaxi),len(remainingrequest),availabletaxilist,sourcelistn)

                #taxirequest=pickup(sourcelist,availabletaxilist,availabletaxi,filledtaxi,remainingrequest,filledrequest,destinationlist,sourcelistn,distancematrix)

    totaltime=list(map(lambda time:time-1,totaltime))

    for time1 in totaltime:

        if(time1==0):

            inden=totaltime.index(time1)

            totaltime.remove(time1)

            if(len(filledtaxi)==0):

                break

            numfilledtaxi=filledtaxi[inden]

            availabletaxi.append(filledtaxi[inden])

            filledtaxi.remove(filledtaxi[inden])

            fullfilledrequest.append(filledrequest[inden])

            re=filledrequest[inden]

            #sourcelistn.remove(sourcelistn[re-1])

            filledrequest.remove(re)

            availabletaxilist.remove(availabletaxilist[numfilledtaxi-1])

            availabletaxilist.append(destinationlist[re-1])

    #print(t)

    

sum1=0

print(len(servicetime))

print(servicetime)

for li in servicetime:

    print(li)

    sum1=sum1+li

print(sum1)

print(sum1/len(servicetime))

