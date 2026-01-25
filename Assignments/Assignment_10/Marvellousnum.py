def ChkPrime(No):     
    if No <= 1:
        return list([])   
    i = 2 
    while(i * i <= No):
        if(No % i == 0):
            return list([])
        i = i +1
    return list([No])