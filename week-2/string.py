str = "sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5"
print("Original string: ",str)
str_num=[i for i in str.split(' ')]

n = len(str_num)

numbers=sorted([int(x) for x in str_num if x.isdigit()])

print('Numbers in sorted form:')
for i in ((filter(lambda x:x>n,numbers))):
    print(i,end=' ')