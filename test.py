#day=['Monday_','Tuesday_','Wednesday_','Thrusday_','Friday','Saturday','Sunday']
import gg
import matplotlib.pyplot as plt
new_sum = 0
new_day = ''
##def maxday(aa,name):
##    finalOut,l1,l2=gg.plot(aa,'out/'+name+'.txt')
##    global new_sum
##    week_t=sum(l2)
##    if(week_t>new_sum):
##        new_sum = week_t
##        new_day = name
##        print(name,max_day)
##        return new_day
    
def main(aa,name):
    aa=aa
    finalOut,l1,l2=gg.plot(aa,'out/'+name+'.txt')
        
    print(finalOut)    
    overcrowd = []

    for i in l1:
        overcrowdFlag = 0
        if i in finalOut:
            overcrowdFlag = 1
        if(overcrowdFlag == 1):
            plt.plot(i,overcrowdFlag,'rx')
        else:
            plt.plot(i,overcrowdFlag,'r-')
        
    plt.grid(color='b', linestyle='--', linewidth=0.5)
    plt.show()
