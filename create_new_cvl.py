import random
import math

cvltrain = open("imagelist/cvltrain.txt")
cvltest = open("imagelist/cvltest.txt")

# content: 5, 10, 15, 20, 26
# writer: 50, 100, 150, 200, 250, 308

cvlcontentlist = {}
cvlwriterlist = {}
alllist = []

for image in cvltrain.readlines():
    alllist.append(image.strip())
for image in cvltest.readlines():
    alllist.append(image.strip())

for i in alllist:
    writer = i.split("-")[1]
    content = i.split("-")[0].split("/")[-1]
    cvlwriterlist.setdefault(writer, []).append(i.strip())
    # cvlwriterlist[writer] += i.strip()
    cvlcontentlist.setdefault(content, []).append(i.strip())
# cvlcontentlist[content] = i.strip()

print(len(cvlwriterlist))
# print(cvlwriterlist)
print(len(cvlcontentlist))
cvlwriter_train = open("cvlwriter50_train.txt", "w+")
cvlwriter_test = open("cvlwriter50_test.txt", "w+")
cvlwritertrainlist = []
cvlwritertestlist = []
imagenum = 0
writernum = 50
numperwriter = math.ceil(1262/writernum)
print(numperwriter)
print(len(list(set(cvlwriterlist))))
print(len(list(set(cvlcontentlist))))
for (i,k) in cvlwriterlist.items():
    tmpnum = len(k)
    random.shuffle(k)
    if imagenum < 1261:
        #print(i, k)
        if imagenum+tmpnum < 1261:
            imagenum += tmpnum
            for j in range(0,tmpnum):
                cvlwriter_train.writelines(k[j] + "\n")
                cvlwritertrainlist.append(k[j].strip())
        else:
            sub = 1262 - imagenum
            print(sub)
            imagenum = 1262
            for j in range(0, sub):
                cvlwriter_train.writelines(k[j] + "\n")
                cvlwritertrainlist.append(k[j].strip())
    else:
        break
print(len(alllist), len(cvlwritertrainlist))
tmmp = []
for i in alllist:
    tmmp.append(i.split(" ")[0].split("/")[-1])
    #print(i.split(" ")[0].split("/")[-1])
cvlwritertestlist = list(set(alllist).difference(cvlwritertrainlist))
print(len(cvlwritertestlist))
print(len(list(set(cvlwritertrainlist))))

print(len(list(set(alllist))))
print(len(list(tmmp)))
"""
for i in alllist:
    for j in cvlwritertrainlist:
        if i.split("/")[-1].split(" ")[0] != j.split("/")[-1].split(" ")[0]:
            cvlwritertestlist.append(i)
"""
for item in cvlwritertestlist:
    cvlwriter_test.writelines(item+"\n")