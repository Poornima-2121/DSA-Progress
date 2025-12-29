def two_sum(nums,target):
    hashmap={}
    for i in range(len(nums)):
        wanted = target-nums[i]
        if wanted in hashmap:
            return [hashmap[wanted],i]
        hashmap[nums[i]]=i
print(two_sum([2,7,11,15],9))
print(two_sum([3,2,4],6))
print(two_sum([3,3],6))