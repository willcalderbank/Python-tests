import os
from timeit import Timer
import hashlib
#import hashlib2

def latex_to_png(eqs,dir,tempdir = "/tmp"):
    command = "texvc " + tempdir + " " + dir + ' \"' + eqs +  '\" iso-8859-1 \"rgb 1.0 1.0 1.0\"'
    return_code = os.popen(command)
    current_name =  dir + "/"+ str(return_code.read())[1:]+".png"
    new_name = dir + "/" + hashlib.md5(eqs).hexdigest() +".png"
    os.rename(current_name,new_name )
    return new_name

def is_cached_latex(eqs, dir = "/tmp"):
    return os.path.isfile(dir + "/"+ hashlib.md5(eqs).hexdigest() +".png")

def get_latex(eqs, dir = "/tmp"):
    hash =  hashlib.md5(eqs).hexdigest()
    if os.path.isfile(dir + "/"+ hash +".png"):
        return dir + "/"+ hash +".png"
    else:
        return latex_to_png(eqs,dir)
