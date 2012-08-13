import datetime

def time(time1,time2):
    t1 = time1.split(':')
    t2 = time2.split(':')
	#Calculates average time, as a timedelta
    dt1 = datetime.timedelta(seconds=(int(t1[0])*60)+int(t1[1]),microseconds=int(t1[2]))
    dt2 = datetime.timedelta(seconds=(int(t2[0])*60)+int(t2[1]),microseconds=int(t2[2]))
    av = (dt1 +dt2)/2

	#convert mins secs and hs
    minutes = av.seconds / 60  #int division
    seconds = av.seconds % 60 
    hs = av.microseconds
	
	#convert mins secs and hs to string
	
	#av.seconds/60 and % 60 can be 1 or 2 digits must force to 2
	#hs can be any be any lenght so force to only 2 (round up or down)
    if hs>99:
	    hs = str(round(hs,2-len(str(hs))))[:2]
    else:
	    hs = str(hs).zfill(2)
	
    return '%02d:%02d:%0s'%(minutes,seconds,hs)    


print time('1:1:111',"2:2:2")


