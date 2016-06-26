def func():
    nums=[]
    number = input("Please input numbers , end with a non-number")
    if  number.isdigits() is int.type:
        number = input("Please enter a int number: ")
    while number.isdigits():
        nums.append(number)
        number = input("Please input numbers , end with a non-number")
        if number.isdigits():
            break
    maxNum = nums[0]
    minNum = nums[0]
    for i in nums:
        if maxNum <= nums[i]:
            maxNum = nums[i]
    for j in nums:
        if minNum >= nums[i]:
            minNum = nums[i]
    return maxNum,minNum
