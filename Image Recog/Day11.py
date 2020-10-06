from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from statistics import mean
from collections import Counter


def createExample():
    numberArrayExamples = open('numberArExt.txt', 'a')
    numbersWeHave = range(1, 10)
    for eachNum in numbersWeHave:
        for furtherNum in numbersWeHave:
            print(str(eachNum) + '.' + str(furtherNum))
            imgFilePath = 'Images/numbers/' + str(eachNum) + '.' + str(furtherNum) + '.png'
            ei = Image.open(imgFilePath)
            eiar = np.array(ei)
            eiarl = str(eiar.tolist())

            print(eiarl)
            lineToWrite = str(eachNum) + '::' + eiarl + '\n'
            numberArrayExamples.write(lineToWrite)


createExample()


def threshold(imageArray):
    balanceAr = []
    newAr = imageArray

    for eachRow in imageArray:
        for eachPix in eachRow:
            avgNum = mean(eachPix[:3])
            balanceAr.append(avgNum)

    balance = mean(balanceAr)
    for eachRow in newAr:
        for eachPix in eachRow:
            if mean(eachPix[:3]) > balance:
                eachPix[0] = 255
                eachPix[1] = 255
                eachPix[2] = 255
                eachPix[3] = 255
            else:
                eachPix[0] = 0
                eachPix[1] = 0
                eachPix[2] = 0
                eachPix[3] = 255

    return newAr

def whatNumIsThis(filePath):

    matchedAr = []
    loadExamps = open('numberArExt.txt', 'r').read()
    loadExamps = loadExamps.split('\n')

    i = Image.open(filePath)
    iar = np.array(i)
    iarl = iar.tolist()

    inQuestion = str(iarl)

    for eachExample in loadExamps:
        try:
            splitEx = eachExample.split('::')
            currentNum = splitEx[0]
            currentAr = splitEx[1]

            eachPixEx = currentAr.split('],')
            eachPixInQ = inQuestion.split('],')

            x = 0

            while x < len(eachPixEx):
                if eachPixEx[x] == eachPixInQ[x]:
                    matchedAr.append(int(currentNum))

                x += 1
        except Exception as e:
            print(str(e))

    print(matchedAr)
    x = Counter(matchedAr)
    print(x)
    print(x[0])

whatNumIsThis('Images/blank.png')



"""
i = Image.open('Images/numbers/0.1.png')
iar = np.array(i)
i2 = Image.open('Images/numbers/y0.4.png')
iar2 = np.array(i2)
i3 = Image.open('Images/numbers/y0.5.png')
iar3 = np.array(i3)
i4 = Image.open('Images/sentdex.png')
iar4 = np.array(i4)

iar = threshold(iar)
iar2 = threshold(iar2)
iar3 = threshold(iar3)
iar4 = threshold(iar4)


fig = plt.figure()
ax1 = plt.subplot2grid((8, 6), (0, 0), rowspan=4, colspan=3)
ax2 = plt.subplot2grid((8, 6), (4, 0), rowspan=4, colspan=3)
ax3 = plt.subplot2grid((8, 6), (0, 3), rowspan=4, colspan=3)
ax4 = plt.subplot2grid((8, 6), (4, 3), rowspan=4, colspan=3)

ax1.imshow(iar)

ax2.imshow(iar2)

ax3.imshow(iar3)

ax4.imshow(iar4)

plt.show()

i = Image.open('Images/numbers/0.1.png')
iar = np.asarray(i)

plt.imshow(iar)
print(iar)
plt.show()
"""
