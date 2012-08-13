import re
import collections

def sort(text):
	#removes whitespace
	text=re.sub(r'\s','',text)
	
	#counts letters
	# counter=collections.Counter()
	# for letter in text:
	# 	counter[letter] +=1

	counter = {}
	for letter in text:
		counter[letter] = counter.get(letter,0) +  1
		
		
	#convert to list sorted by key
	lst = sorted(counter.items())
	
	for i in lst:
		print i[0], i[1]

sort("wtfjsdfh")