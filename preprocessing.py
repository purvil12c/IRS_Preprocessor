#static dict of stop-words
stop_dict={ 'a':1, 'an': 1, 'of': 1, 'the': 1}
#static dict of stem words
stems=['ing','s','.']


dict4 = {}


#Reading and tokenizing text1 file
with open('corpus/text1.txt') as file1:
	lines1 = file1.readlines()
content1 = ""
for line in lines1:
	content1+=line

tokens1 = content1.split()

#Reading and tokenizing text2 file
with open('corpus/text2.txt') as file2:
	lines2 = file2.readlines()
content2 = ""
for line in lines2:
	content2+=line

tokens2 = content2.split()
#Reading and tokenizing text3 file
with open('corpus/text3.txt') as file3:
	lines3 = file3.readlines()
content3 = ""
for line in lines3:
	content3+=line

tokens3 = content3.split()

#adding tokens to dict
dict1 = {}
for word in tokens1:
	if dict1.has_key(word):
		dict1[word]+=1
	else:
		dict1[word]=1
dict2 = {}
for word in tokens2:
	if dict2.has_key(word):
		dict2[word]+=1
	else:
		dict2[word]=1
dict3 = {}
for word in tokens3:
	if dict3.has_key(word):
		dict3[word]+=1
	else:
		dict3[word]=1

#Removing stop words
for key,value in stop_dict.iteritems():
	if dict1.has_key(key):	
		del dict1[key]
#if dict1.has_key('the'):
#	print dict1['the']
#else:
#	print 0

for key,value in stop_dict.iteritems():
	if dict2.has_key(key):	
		del dict2[key]


for key,value in stop_dict.iteritems():
	if dict3.has_key(key):	
		del dict3[key]

#stemming 
for key in dict1.keys():
	for s in stems:
		if(key.endswith(s)):
			key1 = key[:-len(s)]
			dict1[key1]=dict1[key]
			del dict1[key]
			break
#print dict1['convey']
for key in dict2.keys():
	for s in stems:
		if(key.endswith(s)):
			key1 = key[:-len(s)]
			dict2[key1]=dict2[key]
			del dict2[key]
			break
for key in dict3.keys():
	for s in stems:
		if(key.endswith(s)):
			key1 = key[:-len(s)]
			dict3[key1]=dict3[key]
			del dict3[key]
			break
#incidence matrix code

dict_incidence = {}
for key in dict1.keys():
	if(dict_incidence.has_key(key)):
		dict_incidence[key]+='1'
	else:
		dict_incidence[key]='1'

for key in dict2.keys():
	if(dict_incidence.has_key(key)):
		dict_incidence[key]+='2'
	else:
		dict_incidence[key]='2'

for key in dict3.keys():
	if(dict_incidence.has_key(key)):
		dict_incidence[key]+='3'
	else:
		dict_incidence[key]='3'

print '\t \t 1 \t \t 2 \t \t 3'
print '\n'
for key in dict_incidence.keys()[:25]:
	
	value = dict_incidence[key]
	flag1 = 0
	flag2 = 0
	flag3 = 0	
	if(value.find('1')):
		flag1=1
	if(value.find('2')):
		flag2=1
	if(value.find('3')):
		flag3=1
	print(key + '\t \t'+str(flag1) +'\t \t' +str(flag2)+'\t \t'+str(flag3))
	print '\n'
