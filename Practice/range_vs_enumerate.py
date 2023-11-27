def fizz_buzz(numbers):
    
    # for i in range(len(numbers)):
    #     #print(i)
    #     num = numbers[i]
    #     if num % 3 == 0:
    #         numbers[i] = "fizz"
    #     if num % 5 == 0:
    #         numbers[i] = "buzz"
    #     if num % 3 == 0 and num % 5 == 0:
    #         numbers[i] = "fizzbuzz"
            
    for i, num in enumerate(numbers):
        #print(i)
        num = numbers[i]
        if num % 3 == 0:
            numbers[i] = "fizz"
        if num % 5 == 0:
            numbers[i] = "buzz"
        if num % 3 == 0 and num % 5 == 0:
            numbers[i] = "fizzbuzz"