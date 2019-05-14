data = []
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
print (len(data))

sum_len = 0
for d in data:
	sum_len += len(d)
print (sum_len/len(data))
		