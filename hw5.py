# Name: Lilian Sheu
# Discussion: Thursdays 3-4 pm

import re

f = open('regex_sum_31740.txt')
list1 = []
sum = 0
for line in f:
	line = line.rstrip()
	y = re.findall('[0-9]+', line)
	if len(y) > 0:	
		for i in y:
			sum += int(i)
print (sum)