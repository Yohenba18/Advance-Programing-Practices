class Find_pair():
    def pair(self, nums, target):
        l = len(nums)
        for i in range(0,l):
            for j in range(i-1,i+1):
                if nums[i] + nums[j] == target:
                    # print(nums[i],nums[j])
                    print(j+1,i+1)
                    return 
                


    
x = [10,20,10,40,50,60,70]
# x= [15, 20 , 13, 24, 34, 10 , 40 , 45]
target= 50

y = Find_pair()
y.pair(x,target)