def fibgen(limit,fib_list):
    fib_list.append(1)
    temp = 2
    n=1
    while temp < limit:
        fib_list.append(temp)
        n+=1
        temp = fib_list[n-1] + fib_list[n-2]
    #end while
#end prcedure

def find_fib(n,my_list):
    L = 0
    R = len(my_list) 
    while L < R:
        m = (L + R) // 2
        if my_list[m] > n:
            R = m 
        else:
            L = m + 1
    return my_list[R-1]
#end function

def calc_num(n, my_list):
    ans = []
    while n > 0:
        x = find_fib(n,my_list)
        ans.append(x)
        n = n - x
    #end while
    return ans
#end procedure

my_list = []
#fibgen(53316291173,my_list)
fibgen(5000000001,my_list)
print(my_list)
print(len(my_list))

def threes(my_list):
    total = []
    i=0
    while i < len(my_list) - 4:
        j = i + 2
        while j < len(my_list) - 2:
            k = j + 2
            while k < len(my_list):
                total.append(my_list[i]+my_list[j]+my_list[k])
                #total+=1
                k+=1
            j+=1
        i+=1
    #end while
    return total
#end procedure

ans = threes(my_list)
ans.sort()
print(ans[:50])

    
#print(find_fib(514228,my_list))
#print(calc_num(514228,my_list))
# total = 0
# for num in range(999999999,5000000001):
#     a = calc_num(num,my_list)
#     #print(a)
#     if 701408733 not in a:
#         print(a)
#         total += 1


#print(total)
