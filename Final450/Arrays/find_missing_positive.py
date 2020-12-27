def missing_po(nums):
        nums.sort()
        found = True
        j = 0
        while found:
            if nums[j] > 0:
                found = False
            if found:
                j+=1
        if found:
            return 1
        new_nums = nums[j:]
        print("New Nums: "+ str(new_nums))
        for i in range(len(new_nums)):
            print("I value: "+str(i))
            if new_nums[i] != i+1:
                print("reached here"+str(i))
                return i+1
        return i+2

print(missing_po([0,1,2]))