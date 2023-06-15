file=open("readtext.txt")
#read n number of character by passing parameter
#print(file.read(4))
#print(file.readline())
# line =file.readline()
# while line!="":
#     print(line)
#     line=file.readline()
# file.close()

for line in file.readlines():
    print(line)
