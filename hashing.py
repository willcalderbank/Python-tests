import hashlib, random
from timeit import Timer

#md5(), sha1(), sha224(), sha256(), sha384(), and sha512()
'''
Tests hash functions
As expected md5 is fastest
sha224 and above are fairly similar, not too surprising as they are similar 
'''


class HashTests():
    def __init__(self,*args,**kargs):
        f = open('/usr/share/dict/words', 'r')
        self.dictionary = []
        for line in f:
            self.dictionary.append(line)
            
        #Randomise it
        random.shuffle(self.dictionary)
            
    def md5(self, number):
        for word in self.dictionary[:number]:
            hashlib.md5(word).hexdigest()
    
    def sha1(self, number):
        for word in self.dictionary[:number]:
            hashlib.sha1(word).hexdigest()
            
    def sha224(self, number):
        for word in self.dictionary[:number]:
            hashlib.sha224(word).hexdigest()
            
    def sha256(self, number):
        for word in self.dictionary[:number]:
            hashlib.sha256(word).hexdigest() 
    
    def sha384(self, number):
        for word in self.dictionary[:number]:
            hashlib.sha256(word).hexdigest() 
            
    def sha512(self, number):
        for word in self.dictionary[:number]:
            hashlib.sha256(word).hexdigest()             
            

    def speedtests(self,number):
        print "Starting speed tests..."
        print "md5: %.2f sec/word" % (Timer(lambda: self.md5(number)).timeit()/number)
        print "sha1: %.2f sec/word" % (Timer(lambda: self.sha1(number)).timeit()/number)
        print "sha224: %.2f sec/word" % (Timer(lambda: self.sha224(number)).timeit()/number)
        print "sha256: %.2f sec/word" % (Timer(lambda: self.sha256(number)).timeit()/number)
        print "sha384: %.2f sec/word" % (Timer(lambda: self.sha384(number)).timeit()/number)
        print "sha512: %.2f sec/word" % (Timer(lambda: self.sha512(number)).timeit()/number)
        print "finished"


tests = HashTests()
tests.speedtests(1)

                