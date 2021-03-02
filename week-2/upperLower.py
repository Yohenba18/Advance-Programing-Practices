name = input("enter the sentence: ")

count_upper= 0
cout_lower=0
for i in range(len(name)): 
    if(name[i] != " "):
        if(name[i].isupper()):
            count_upper += 1
        else: 
            cout_lower +=1

print("No. of Upper case characters : ",count_upper)
print("No. of Lower case Characters : ",cout_lower)