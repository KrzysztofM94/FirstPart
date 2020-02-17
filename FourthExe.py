inData = int(input("Give a number: "))
table = range(1,inData+1)
divided=[]

for i in table:
    if(inData%i==0):
        divided.append(table[i-1])
print(divided)

