def divisible(a,b,c):
    new_list=[]
    for i in range(a,b+1):
        if i % c == 0:
            new_list.append(i)
        else:
            continue
    return new_list
            
