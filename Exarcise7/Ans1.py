with open("D:\All_Python_Program\Exarcise7\poem.txt","r") as f:
    d = dict()

    for line in f:
        line = line.strip()

        line = line.lower()

        words = line.split()
        # print(line)

        for word in words:
            if word in d:
                d[word] = d[word] + 1
            else:
                d[word] = 1

for key in list(d.keys()):
    print(key, ":" , d[key])

print('masudalom')
    