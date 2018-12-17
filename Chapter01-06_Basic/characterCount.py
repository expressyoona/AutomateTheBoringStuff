message = 'Hello World'
count = {}
for ch in message:
    count.setdefault(ch, 0)
    count[ch] = count[ch] + 1
for i,v in count.items():
    print(str(i) + ' = ' + str(v))
#print(count)
