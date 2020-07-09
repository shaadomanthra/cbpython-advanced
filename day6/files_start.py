## operating with files

#read and print lines
r = open('sample.txt','r')
list = []
for l in r:
    list.append(l.strip())
    print(l.strip())
print(list)

line = r.read()
print(line)

# write files
text = "The is a sample line"
w = open('new.txt','w')
w.writelines(text)

# close files
r.close()
w.close()

