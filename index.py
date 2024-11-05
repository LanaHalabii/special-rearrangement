def special_rearrangement(nums):

    even_nums = []                      #define even array to store even numbers
    odd_nums = []                       #define odd array to store odd numbers

    for i in range(len(nums)):
        if nums[i] % 2 == 0:    
            even_nums.append(nums[i])   #if the number in the original array is divisible by 2, store in even array
        else:
            odd_nums.append(nums[i])    #else, store it in odd array
    
    return even_nums + odd_nums         #return the concatination of the odd array to the even one

nums = [2, 5, 7, 6, 1, 4]
print(special_rearrangement(nums))