with open("input","r") as f:
    nums = f.readlines()
    for num1 in nums:
        for num2 in nums:
            if int(num1) + int(num2) == 2020: 
                print(int(num1) * int(num2))
