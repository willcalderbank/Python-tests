
import pprint

MAXPRIME = 900000
primes = []

def filter_test():
    def f(x): return x % 2 != 0
    return list(filter(f,range(1,MAXPRIME)))

def list_comp_test():
    return[i for i in xrange(1,MAXPRIME) if i%2 ==0 ]


#from timeit import Timer
#t = Timer("filter_test()", "from __main__ import filter_test")
#print "%.5f usec/pass" % (1000000 * t.timeit(number=100000)/100000)
#
#
#from timeit import Timer
#t = Timer("list_comp_test()", "from __main__ import list_comp_test")
#print "%.5f usec/pass" % (1000000 * t.timeit(number=100000)/100000)

def mod_the_list(list,mod):
    return [i for i in list if not i%mod ==0]

pp = pprint.PrettyPrinter(indent=4)

confirmed = 0
p = 2
primes = mod_the_list(xrange(1,MAXPRIME),p)

finished = False
while finished==False:
    for prime in primes:    
        if prime > p:
            p = prime
            break;
    confirmed +=1
    newprime = primes[:confirmed]
    newprime.extend(mod_the_list(primes[confirmed:],p))
    
    if newprime == primes or len(primes)== 10001:
        finished = True  
    else:
        print len(primes)
    
print pp.pprint(primes), len(primes)