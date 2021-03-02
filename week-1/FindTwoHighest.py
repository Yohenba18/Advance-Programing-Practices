lst = [] 
n = int(input("Enter number of marks : ")) 
  
for i in range(0, n): 
    ele = int(input()) 
  
    lst.append(ele) 
      
for i in range(0, n): 
    for j in range(0, n-i-1): 
        if lst[j] < lst[j+1] : 
                lst[j],lst[j+1] = lst[j+1], lst[j] 

print("highest 2 numbers")
print(lst[0],lst[1])