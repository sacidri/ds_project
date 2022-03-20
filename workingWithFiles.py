import csv

fileName = 'demo2.csv'
accessMode = 'r'

with open(fileName, accessMode) as demoFile:
    myDataFile = csv.reader(demoFile)
    print(myDataFile)



# nameList = open('demo.txt', 'w')
# nameList.write('bill, 22 \n')
# nameList.write('tim, 24 \n')
# nameList.write('jill, 32 \n')
# nameList.close()


# guestFile = 'guestfile.txt'
# WRITE = 'w'
# READ = 'r'
# APPEND = 'a'

# myGuestList = []
# name = ''
# inviteList = open(guestFile, WRITE)
# while name != 'OVER':
#     name = input('Enter guest name: ').upper()
#     myguestList = myGuestList.append(name)
# inviteList.write(str(myGuestList))
# inviteList.close()


# nameFile = open('demo.txt', 'r')

# allNames = nameFile.read()
# print(allNames)

# nameList = []
# data = ''
# while data != 'DONE':
#     data = input('Enter list of names and age separated by a comma: \n').upper()
#     nameList.append(data)
# for name in nameList:
#     myFile = open(fileName, APPEND)
#     myFile.writelines(name)
# myFile.close()

# myFile = open(fileName, mode = WRITE)
# myFile.write('Bill, 32 \n')
# myFile.write('Jill, 30 \n')
# myFile.write('Tim, 29 \n')
# myFile.close()
# print('successfully written to the file')
