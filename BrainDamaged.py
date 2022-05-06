value = []
n = int(input())
search1 = []
result = []

for i in range(n):
    x = input()
    value.append(x)

y = int(input())
for j in range(y):
    search = input()
    search1.append(search)

for k in range(len(value)):
    count = 0
    for l in range(len(search1)):

        if search1[l].lower() in value[k].lower():
            count += 1
            if len(search1) > 1:
                if count == len(search1):
                    result.append(value[k])
            elif len(search1) == 1:
                if count >= 1:
                    result.append(value[k])

for value1 in result:
    print(value1)
#for num in range(len(value)):
    #print(num)
    #if search1.lower() in value[num].lower():
       #print(value[num])
