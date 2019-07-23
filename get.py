data = []
count = 0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完了，總共有', len(data), '筆留言。')

sum_length = 0
for text in data:
	sum_length += len(text)

print('留言的平均長度是 :', sum_length/len(data))

new = []
for text in data:
	if len(text) < 100:
		new.append(text)
print('總共有', len(new), '筆留言長度小於100')
print(new[0])
print(new[1])

good = []
for text in data:
	if 'good' in text:
		good.append(text)
print('總共有', len(good), '筆留言提到good')
print(good[0])

