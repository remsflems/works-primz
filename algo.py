import re, os, sys
def replacenth(string, sub, wanted, n):
	where = [m.start() for m in re.finditer(sub, string)][n-1]
	before = string[:where]
	after = string[where:]
	after = after.replace(sub, wanted, 1)
	newString = before + after
	return newString


file=open(sys.argv[1]).read()

cpt_cd=file.count(sys.argv[2])
print cpt_cd
sub=sys.argv[2]
wanted=sys.argv[3]
folder=sub+wanted
if not os.path.exists(folder):
	os.makedirs(folder)

from itertools import permutations
from itertools import combinations

if cpt_cd == 2:
	comb = list(permutations([0,1], 2))
if cpt_cd == 3:
	comb = list(permutations([0,0,1], cpt_cd))
	comb.extend(list(permutations([0,1,1], cpt_cd)))
if cpt_cd == 4:
	comb = list(permutations([0,0,0,1], cpt_cd))
	comb.extend(list(permutations([0,0,1,1], cpt_cd)))
	comb.extend(list(permutations([0,1,1,1], cpt_cd)))
else:
	comb=[]

fcpt=0
while os.path.isfile(folder+'/primen'+str(fcpt)):
	fcpt=fcpt+1

for obj in comb:
	strings=file
	newf=open(folder+'/primen'+str(fcpt),'w')
	if cpt_cd == 2:
		s1=obj[0]
		s2=obj[1]
		if s1 == 1 and s2 == 0:
			strings = replacenth(strings, sub, wanted, 1)
		if s1 == 0 and s2 == 1:
			strings = replacenth(strings, sub, wanted, 2)
	if cpt_cd == 3:

		s1=obj[0]
		s2=obj[1]
		s3=obj[2]
		if s1 == 0 and s2 == 0 and s3 == 1:
			strings = replacenth(strings, sub, wanted, 3)
		if s1 == 0 and s2 == 1 and s3 == 0:
			strings = replacenth(strings, sub, wanted, 2)
		if s1 == 1 and s2 == 0 and s3 == 0:
			strings = replacenth(strings, sub, wanted, 1)
		if s1 == 0 and s2 == 1 and s3 == 1:
			strings = replacenth(strings, sub, wanted, 3)
			strings = replacenth(strings, sub, wanted, 2)
		if s1 == 1 and s2 == 0 and s3 == 1:
			strings = replacenth(strings, sub, wanted, 3)
			strings = replacenth(strings, sub, wanted, 1)
		if s1 == 1 and s2 == 1 and s3 == 0:
			strings = replacenth(strings, sub, wanted, 2)
			strings = replacenth(strings, sub, wanted, 1)

	if cpt_cd == 4:
		s1=obj[0]
		s2=obj[1]
		s3=obj[2]
		s4=obj[3]
		#1 to change
		if s1 == 0 and s2 == 0 and s3 == 0 and s4 == 1:
			strings = replacenth(strings, sub, wanted, 4)
		if s1 == 0 and s2 == 0 and s3 == 1 and s4 == 0:
			strings = replacenth(strings, sub, wanted, 3)
		if s1 == 0 and s2 == 1 and s3 == 0 and s4 == 0:
			strings = replacenth(strings, sub, wanted, 2)
		if s1 == 1 and s2 == 0 and s3 == 0 and s4 == 0:
			strings = replacenth(strings, sub, wanted, 1)

		#2 to change
		if s1 == 0 and s2 == 0 and s3 == 1 and s4 == 1:
			strings = replacenth(strings, sub, wanted, 4)
			strings = replacenth(strings, sub, wanted, 3)
		if s1 == 0 and s2 == 1 and s3 == 0 and s4 == 1:
			strings = replacenth(strings, sub, wanted, 4)
			strings = replacenth(strings, sub, wanted, 2)
		if s1 == 1 and s2 == 0 and s3 == 0 and s4 == 1:
			strings = replacenth(strings, sub, wanted, 4)
			strings = replacenth(strings, sub, wanted, 1)
		if s1 == 0 and s2 == 1 and s3 == 1 and s4 == 0:
			strings = replacenth(strings, sub, wanted, 3)
			strings = replacenth(strings, sub, wanted, 2)
		if s1 == 1 and s2 == 0 and s3 == 1 and s4 == 0:
			strings = replacenth(strings, sub, wanted, 3)
			strings = replacenth(strings, sub, wanted, 1)
		if s1 == 1 and s2 == 1 and s3 == 0 and s4 == 0:
			strings = replacenth(strings, sub, wanted, 2)
			strings = replacenth(strings, sub, wanted, 1)

		#3 to change
		if s1 == 0 and s2 == 1 and s3 == 1 and s4 == 1:
			strings = replacenth(strings, sub, wanted, 4)
			strings = replacenth(strings, sub, wanted, 3)
			strings = replacenth(strings, sub, wanted, 2)
		if s1 == 1 and s2 == 0 and s3 == 1 and s4 == 1:
			strings = replacenth(strings, sub, wanted, 4)
			strings = replacenth(strings, sub, wanted, 3)
			strings = replacenth(strings, sub, wanted, 1)
		if s1 == 1 and s2 == 1 and s3 == 0 and s4 == 1:
			strings = replacenth(strings, sub, wanted, 4)
			strings = replacenth(strings, sub, wanted, 2)
			strings = replacenth(strings, sub, wanted, 1)
		if s1 == 1 and s2 == 1 and s3 == 1 and s4 == 0:
			strings = replacenth(strings, sub, wanted, 3)
			strings = replacenth(strings, sub, wanted, 2)
			strings = replacenth(strings, sub, wanted, 1)

	newf.write(strings)
	newf.close()
	fcpt=fcpt+1

#rien
newf=open(folder+'/primen'+str(fcpt),'w')
newf.write(file)
#tout
strings=file
if cpt_cd == 1:
	strings = replacenth(strings, sub, wanted, 1)
if cpt_cd == 2:
	strings = replacenth(strings, sub, wanted, 1)
	strings = replacenth(strings, sub, wanted, 1)
if cpt_cd == 3:
	strings = replacenth(strings, sub, wanted, 1)
	strings = replacenth(strings, sub, wanted, 1)
	strings = replacenth(strings, sub, wanted, 1)
if cpt_cd == 4:
	strings = replacenth(strings, sub, wanted, 1)
	strings = replacenth(strings, sub, wanted, 1)
	strings = replacenth(strings, sub, wanted, 1)
	strings = replacenth(strings, sub, wanted, 1)

fcpt=fcpt+1
newf=open(folder+'/primen'+str(fcpt),'w')
newf.write(strings)
newf.close()

