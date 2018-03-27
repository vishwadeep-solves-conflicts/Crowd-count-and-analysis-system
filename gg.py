import math
threshold=''
finalOut=[]
x,y=0,-10
def ti():
  global x,y
  y= y + 10
  if( y==60):
   x+=1
   y=0
  return  x, y


def plot(threshol,dataFile):
  
   global threshold
   threshold = threshol + math.floor(threshol*5/100)
   global x,y
   remaining = {}
   for a in range(144):
     toup = ti()
     s = toup[0]*100+toup[1]
     remaining[s] = 0

   f     = open(dataFile,"r")
   line = f.readline()
   n=0
   while line :
    for word in line.split():
     rawTime = word[:5]

     det     = word[5]
     hours = int(rawTime[:2])
     mins  = int(rawTime[3:5])

     mins = round(mins,-1)
     if(mins==60):
       mins=0
       hours+=1
       if(hours==24): hours=0
     time=hours*100+mins

     if(det=='0'):
      remaining[time]-=1
     elif(det=='1'):
      remaining[time]+=1
    line = f.readline()

   l1,l2=[],[]; prevSum=remaining[0]
   l1.append(0)
   l2.append(remaining[0])
   for key in remaining.keys():
     if (key==0):continue
     mins = key%100;
     hours= key/100;
     xcoord = '%02d:%2d' % (hours,mins)
     l1.append(xcoord)
     remaining[key]+=prevSum
     prevSum=remaining[key]
     l2.append(remaining[key])
   ii = 0
   while(ii<len(l1)):
     if(l2[ii]>=threshold):
       finalOut.append(l1[ii])
     ii=ii+1
   x,y=0,-10
   return finalOut,l1,l2
