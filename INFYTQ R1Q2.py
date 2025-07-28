l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))

s1 = sum(l1)
s2 = sum(l2)
result = []

for i in range(len(l1)):
    t1 = s1
    t2 = s2
    for j in range(len(l2)):
        t1 -= l1[i]
        t1 += l2[j]
        t2 -= l2[j]
        t2 += l1[i]
        if t1==t2:
            result.append((l1[i],l2[j]))
        t1 = s1
        t2 = s2

    if len(result)==0:
        print(-1)
    even = []
    odd = []
    for i in result:
        if(i[0]*i[1])%2==0:
            even.append(i)
        else:
            odd.append(i)
        even.sort(key = lambda i: i[0]*i[1])
        odd.sort(key = lambda i : i[0]*i[1] , reverse = True)
        if len(even)!=0:
            for i in even:
                print(str(i[0]+','+str(i[1])+',',end=''))
        if len(odd)!=0:
            for i in range(len(odd)):
                if i!= (len(odd)-1):
                    print(str(odd[i][0] + ',' +str(odd[i][1]) + ',', end = ''))
                else:
                    print(str(odd[i][0]) + ',' + str(odd[i][1]))

        #print(odd,even,result)





