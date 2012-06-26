from datetime import datetime, timedelta
import os

def report_create(filename):
    return open(timeStamped(filename),'w')

def report_get(filename,limit = 10):
    for i in xrange(0,10):
        try:
            return open(timeStamped(filename,i),'r')
        except:
            pass

def timeStamped(fname, tdelta=0,fmt='{fname}_%Y-%m-%d'):
    name, extension = os.path.splitext(fname)
    return (datetime.now()-timedelta(days=tdelta)).strftime(fmt).format(fname=name) + extension

