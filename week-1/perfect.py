def perfect( n ): 
    sum = 1   
    i = 2
    while i * i <= n: 
        if n % i == 0: 
            sum = sum + i + n/i 
        i += 1
    if sum == n and n != 1: 
        return True
    else:
        return False
  
n = 1
for n in range (7,10000): 
    if perfect (n): 
        print(n) 