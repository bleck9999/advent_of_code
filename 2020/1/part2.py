with open("input","r") as f:
    nums = f.readlines()
    for num1 in nums:
        for num2 in nums:
            for num3 in nums:
                if int(num1) + int(num2) + int(num3)  == 2020: 
                    print(int(num1) * int(num2) * int(num3))
