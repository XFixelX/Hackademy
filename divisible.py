def divisible(a,b,c):
    new_list=[]
    if a > b:
        x = a
        a = b
        b = x
    for i in range(a,b+1):
        if i % c == 0:
            new_list.append(i)
        else:
            continue
    return new_list
            
