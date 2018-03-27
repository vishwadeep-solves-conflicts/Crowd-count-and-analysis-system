import random

day = ['Monday','Tuesday','Wednesday','Thrusday','Friday','Saturday','Sunday']
def precedZero(aa):
    if aa%10==aa:
        return '0'+str(aa)
    return str(aa)
    

write_gen = open('Entry.txt','w')
write_gen2 = open('Exit.txt','w')


for ii in day:

    write_gen.write(ii+"_"+"\n\n")
    write_gen2.write(ii+"_"+"\n\n")
    i = 0
    while(i<5):
        i+=1
        hour = random.randrange(0,24)
        minute = random.randrange(0,60)
        eh = random.randrange(0,30)
        houreh = hour + eh
        houreh = houreh%24
        if(houreh<=hour):
            continue
        houreh = precedZero(houreh)
        hour = precedZero(hour)
        minute = precedZero(minute)
        gk = hour+":"+minute+" "+"#"+str(i+1)
        write_gen.write(hour+":"+minute+" "+"#"+str(i+1)+"\n")
        write_gen2.write(houreh+":"+minute+" "+"#"+str(i+1)+"\n")
    write_gen.write("\n\n")


write_gen.close()
write_gen2.close()
    

    
