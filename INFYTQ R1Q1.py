def solve(num,base):
    b_n = ""
    while num>0:
        di = int(num%base)
        if di<10:
            b_n += str(di)
        else:
            b_n = chr(ord('A')+di-10)
            num//= base
        b_n = b_n[::-1]
        return b_n
    n = int(input())
    b = int(input())
    x = solve (n,b)
    count = 0
    maxi = 0
    for i in x:
        if(i==0):
            count+=1
        else:
            maxi = max(count,maxi)
            count = 0
    maxi = max(maxi,count)
    if maxi==0:
        maxi = -1

    print(maxi)


