import os,shutil

day = ['Monday_','Tuesday_','Wednesday_','Thrusday_','Friday_','Saturday_','Sunday_']

def openF(name):
    try:
        day_data = open(name,"r")
        data = day_data.read()
        data = data.split()
        day_data.close()
        return data
    except:
        return 0  

def writeF(aaa,name):
    data = openF(name)
    if data==0:
        return
    path=name[:-4]
    
    if not os.path.exists(path):
        os.mkdir(path)
    data_l = len(data)
    if(data_l==0):
        print("No data available to process")
    i=0
    statusFlag = 0
    
    while(i<data_l):
        if path == aaa+"/"+"Entry":
            statusFlag = 1
        if data[i] in day:
            write_data = open(path+"/"+data[i]+".txt",'w')
        else:
            P_e = data[i]+str(statusFlag)
            write_data.write(P_e+" ")
            i+=1
        i+=1
    write_data.close()
    #shutil.rmtree(path)

def sortlist(datalist):
    for ii in range(len(datalist)):
        for jj in range(len(datalist)):
            aa=int(datalist[ii][:2])*60+int(datalist[ii][3:5])
            bb=int(datalist[jj][:2])*60+int(datalist[jj][3:5])
            if(aa<bb):
               datalist[ii],datalist[jj] = datalist[jj],datalist[ii]
    return datalist
    
def sort(aaa,fileName):
    entryFilePath = aaa+"/"+"Entry/"+fileName+".txt"
    exitFilePath = aaa+"/"+"Exit/"+fileName+".txt"
    if not os.path.exists("out"):
        os.mkdir("out")

    entryData = openF(entryFilePath)
    exitData =  openF(exitFilePath)
    entryData = sortlist(entryData)
    exitData = sortlist(exitData)
    
    data_entryl = len(entryData)
    data_exitl = len(exitData)
    data_l = data_entryl + data_exitl

    i=j=0
    write_data = open("out/"+fileName+".txt",'w')
    while(i+j<data_l):
        exitDataMin = entryDataMin = 1441
        if(i<data_entryl):
            entryDataMin = int(entryData[i][:2])*60+int(entryData[i][3:5])
        if(j<data_exitl):
            exitDataMin = int(exitData[j][:2])*60+int(exitData[j][3:5])
        if(entryDataMin<exitDataMin):
            write_data.write(entryData[i]+" ")
            i+=1
        else:
            write_data.write(exitData[j]+" ")
            j+=1
    write_data.close()

def main(aaa):
    writeF(aaa,aaa+"/"+"Entry.txt")
    writeF(aaa,aaa+"/"+"Exit.txt")
    for iii in day:
        sort(aaa,iii)
