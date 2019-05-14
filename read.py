data = []
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
print (len(data))

sum_len = 0
for d in data:
	sum_len += len(d)
print (sum_len/len(data))

new = []
for d in data:
	if len(d.strip())>2 and len(d.strip())<50:
		new.append(d.strip())
		print (new)
print ('一共有',len(new),'筆留言長度介於2到50之間')

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print ('一共有',len(good),'筆留言中提到good')
print (good[0])		